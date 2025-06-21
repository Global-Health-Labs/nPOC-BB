import win32api
import os
import subprocess
import csv
import shutil
from pathlib import Path

def csv_to_list_of_dicts(filename):
    """
    Reads a CSV file and returns a list of dictionaries.
    Each dictionary represents a row, with keys as column headers.
    """
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def getDriveList():
    drives = [drivestr for drivestr in win32api.GetLogicalDriveStrings().split('\000') if drivestr]
    return drives;
def getDriveList2():
    s = os.popen("wmic logicaldisk list BRIEF /format:csv").read().strip()
    lines = [line for line in s.strip().splitlines() if line!=''];
    # parse the csv into a list of dicts
    listofdicts = [{k:v for k,v in zip(lines[0].split(','), aline.split(','))} for aline in lines[1:]];
    return listofdicts;

def copyAllFromDevice(DRIVE_LETTER,DATAFOLDER,EXPERIMENT_NAME,UNITID,DELETE_LOGS_AFTER_COPYALL=False):
    #pc_destination_path = Path(CFG_DATA_FOLDER_BYUNIT)/('unit{:}'.format(CFG_UNITID))/CFG_DATA_FILE_EXPNAME;
    pc_destination_path = Path(DATAFOLDER)/EXPERIMENT_NAME/UNITID;
    
    print('Destination on PC:');
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



def windowsEjectDrive(letter='E:'):
    ps_command = '(New-Object -comObject Shell.Application).Namespace(17).ParseName("{:s}").InvokeVerb("Eject")'.format(letter);
    
    print(ps_command);

    p = subprocess.run(
        [
            "powershell.exe", 
            "-noprofile", "-c",
            # r"""
            # Start-Process -Verb RunAs -Wait powershell.exe -ArgumentList ('-NoExit','-ExecutionPolicy','remotesigned','-C', '& \"C:\\Users\\SimonGhionea\\OneDrive - Global Health Labs, Inc\\ProjectsCloud\\NAATOS\\sgpyanalysisnaatos\\windowsUninstallNRF51COMPORTS.ps1\\"')
            # """
            ps_command
        ], shell=True
    );