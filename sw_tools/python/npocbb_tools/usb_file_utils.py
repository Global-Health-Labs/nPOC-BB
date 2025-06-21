#import wmic
import io
import time
import os
import shutil
from pathlib import Path

import pandas as pd

import npocbb_tools.npocbb_paths as npocbb_paths


CFG_PATH_TEAMS_BETA_SAMPLEPREPTESTDATA = npocbb_paths.CFG_PATH_TEAMS_BETA_SAMPLEPREPTESTDATA;
if(CFG_PATH_TEAMS_BETA_SAMPLEPREPTESTDATA == ''):
    raise RuntimeError("check npocbb_paths.py, CFG_PATH_TEAMS_BETA_SAMPLEPREPTESTDATA was blank")
# DATA DESTINATION
CFG_DATA_FOLDER = os.path.join(CFG_PATH_TEAMS_BETA_SAMPLEPREPTESTDATA,'by_exp');


####### USB DRIVE OPERATIONS
def checkDrive(driveletter):
    #Usb = os.popen("wmic logicaldisk get Name,DriveType,FreeSpace,Size").read()
    Usb = os.popen("wmic logicaldisk").read()
    dfdrives = pd.read_fwf(io.StringIO(Usb))
    print(dfdrives['DeviceID'])
    return driveletter in dfdrives['DeviceID'].values;

def waitForDrive(drive_letter):
    driveMounted = False;
    while True:
        driveMounted = checkDrive(drive_letter);
        if driveMounted:
            print('Found drive',drive_letter);
            break;
        else:
            print('Waiting for',drive_letter);
            time.sleep(0.5);
    return driveMounted;



####### nPOC-BB FILE OPERATIONS
def idDevice(DRIVE_LETTER):
    CFG_UNITID = 'blah blah blah';
    if False:
        # check for WHOAMI.txt on the device (press enter to use it), or ask for our UNITID
        whoami_file = Path(DRIVE_LETTER)/'whoami.txt';
        if(whoami_file.exists()):
            with open(whoami_file,'rt') as file:
                CFG_UNITID = file.read();
            inputit = input("Enter UNITID (device claims it is '{:}' leave blank and press ENTER to accept it): ".format(CFG_UNITID));
            if(inputit != ''):
                # you actually entered something (not just pressing enter)
                CFG_UNITID = inputit;
        else:
            CFG_UNITID = input("Enter UNITID (none on unit): ");
        # if not CFG_UNITID:
        #     CFG_UNITID = "N"  # Default value if input is empty
    if True:
        # check for whoami: config entry in the logfile on device
        # (press enter to use it), or ask for our UNITID
        config_files = [];
        parsed_unit_id = None;
        if( (Path(DRIVE_LETTER)/'/config').exists() ):
            config_files = [x for x in (Path(DRIVE_LETTER)/'/config').iterdir() if x.name.startswith('config_')];
            assert(len(config_files) == 1);
            # read first config file in directory
            with open(config_files[0],'rt') as file:
                cfgstr = file.read();
            # parse config file
            cfgdict = {k:v for k,v in [tuple(x.split(':')) for x in cfgstr.rstrip().split('\n')]};
            if('whoami' in cfgdict):
                parsed_unit_id = cfgdict['whoami'];
        if(parsed_unit_id is not None):
            CFG_UNITID = parsed_unit_id;
            inputit = input("Enter UNITID (device claims it is '{:}' leave blank and press ENTER to accept it): ".format(CFG_UNITID));
            if(inputit != ''):
                # you actually entered something (not just pressing enter)
                CFG_UNITID = inputit;
        else:
            CFG_UNITID = input("Enter UNITID (none on unit): ");
    return CFG_UNITID;


def copyAllFromDevice(DRIVE_LETTER,EXPERIMENT_NAME,UNITID,DELETE_LOGS_AFTER_COPYALL=True):
    #pc_destination_path = Path(CFG_DATA_FOLDER_BYUNIT)/('unit{:}'.format(CFG_UNITID))/CFG_DATA_FILE_EXPNAME;
    pc_destination_path = Path(CFG_DATA_FOLDER)/EXPERIMENT_NAME/('unit{:}'.format(UNITID));
    print('Destination:');
    print(pc_destination_path);

    # recursive copy of the drive
    print('Copy in progress from device...');
    # # copy recursively (shows no status, not nice warm feeling)
    # shutil.copytree(
    #     src=DRIVE_LETTER ,
    #     dst=pc_destination_path,
    #     ignore=shutil.ignore_patterns("System Volume Information"),
    #     dirs_exist_ok=True
    # )
    
    # copy recursively (and show status)
    src= Path(DRIVE_LETTER+'\\');
    def copyRecursiveWithOutput(path : Path):
        nonlocal pc_destination_path;
        nonlocal src;

        dstfolder = pc_destination_path/path.relative_to(src);
        os.makedirs(dstfolder,exist_ok=True); # make folder on pc

        exclude = {'System Volume Information'};
        for item in path.iterdir():
            if item.name in exclude:
                continue; # skip
            
            if(item.is_dir()):
                copyRecursiveWithOutput(item);
            elif(item.is_file()):
                #print(item.name)
                #destination = 
                #dst = pc_destination_path/item.relative_to(src);
                dst = dstfolder/item.name;
                print('copy {:s} ({:d} bytes) -->to--> PC'.format(item.as_posix(),item.lstat().st_size));
                shutil.copy(item,dst);
    copyRecursiveWithOutput(src);

    
    if( os.path.exists(DRIVE_LETTER+'\\logs') ):
        # get listing of logs folder on the device, so we can check later all files exist on pc
        device_logfile_listing = os.listdir(DRIVE_LETTER+'\\logs');

        # ensure that all the logs ended up over onto the PC-side
        pc_logfile_listing = os.listdir(pc_destination_path/'logs')
        copy_was_good = all([name in pc_logfile_listing for name in device_logfile_listing]);
        print('Files were all copied?',copy_was_good);

        # delete from device if copy was good
        if(copy_was_good and DELETE_LOGS_AFTER_COPYALL):
            print('Deleting logs from device...');
            # shutil.rmtree(DRIVE_LETTER+'\\logs\\*');

            # 1 at a time and display
            for x in Path(DRIVE_LETTER+'\\logs').iterdir():
                print('deleted',x);
                x.unlink();
    else:
        print('logs folder was not on device');

def writeConfigFile(drive_letter,config_filename,strconfig_new):
    #config_filename = os.path.basename(CFG_TEMPLATE_CONFIG_FILE);
    #config_filename = CONFIG_FILENAME;

    # write to the device
    os.makedirs(drive_letter+'\\config\\',exist_ok=True);   # ensure folder exists
    dstconfigpath = drive_letter+'\\config\\'+config_filename;
    #os.makedirs(CFG_DRIVE_LETTER+'\\logs\\',exist_ok=True);
    with open(dstconfigpath, 'wb') as file:
        # read existing file into memory as string
        # must write as binary so that windows python doesn't add crlf endings, only lf
        file.write(strconfig_new.encode());
    print('New config written!',dstconfigpath)

    if False:
        # write a whoami.txt file to the device \config folder
        # write to the device
        with open(CFG_DRIVE_LETTER+'\\'+'whoami.txt', 'w') as file:
            file.write(str(CFG_UNITID));
        print('Wrote WHOAMI with unitid:',CFG_UNITID)