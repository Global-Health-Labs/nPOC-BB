# app.py
from gooey import Gooey, GooeyParser
import time
import tkinter.simpledialog
from pathlib import Path
import os

#%%
# import wx

# app=wx.App()
# def ask(question):
#     dlg = wx.MessageDialog(None, question,'App Title',wx.YES_NO | wx.ICON_QUESTION)
#     result = dlg.ShowModal()

#     if result == wx.ID_YES:
#         return True
#     else:
#         return False

#%%
import npocbb_tools.device_control
import npocbb_tools.usb_file_utils_lite

devicectl = npocbb_tools.device_control.NPOCBB_CONTROLLER();

#%% globals
pre_status = None;
unitid = None;
PC_USERNAME = os.environ.get('USER', os.environ.get('USERNAME'));

#%%
def do_part1(args=None):
    global unitid;
    global pre_status;

    print('-------------------------------')
    print('STARTING PART 1: Identification');
    print('-------------------------------')


    # identification
    status = devicectl.query_STATUS();
    pre_status = status;
    print('Status:')
    print(status);
    if(('FGREWORK' in status) or (('T' in status) and (status['T']=='SP')) ):
        type='SAMPLEPREP';
        typeprefix='SP';
    elif( ('FGREWORK' not in status) or (('T' in status) and (status['T']=='PM'))):
        type='POWER';
        typeprefix='PM';
    else:
        raise RuntimeError('Unexpected response from device, to find device type')
    sn = status['SN'];

    print('Device: {:s}'.format(type))
    print('FWVER: {:s} SN: {:}'.format(status['V'],sn))

    # find where the npocbb_sn_mapping.csv file is located
    filenamecsv1 = Path("npocbb_sn_mapping.csv");
    if(not filenamecsv1.exists()):
        # try 1 level up
        print('trying 1 level up for mapping file')
        filenamecsv = (filenamecsv1.absolute().parent.parent)/'npocbb_sn_mapping.csv'
        if(not filenamecsv.exists()):
            # try 2 level up
            print('trying 2 level up for mapping file')
            filenamecsv = (filenamecsv1.absolute().parent.parent.parent)/'npocbb_sn_mapping.csv'
    else:
        filenamecsv = filenamecsv1;


    snmap = {};
    with open(filenamecsv,mode='rt') as myfile:
        for line in myfile:
            name, var = line.partition(",")[::2]
            snmap[name.strip()] = var.strip();
    filemodified = False;

    if(sn in snmap):
        #print('WE THINK IS UNIT: {:s}'.format(snmap[sn]));
        # device is already known and named! accept?
        unitid = snmap[sn];
        prompt = "Enter UNITID (we think {:s}, press enter to just accept): {:s}".format(snmap[sn],typeprefix);
        #inputit = input("Enter UNITID (we think {:s}, press enter to just accept): {:s}".format(snmap[sn],typeprefix));
        if(not args.id_silent):
            inputit = tkinter.simpledialog.askstring('Title Title Title Title', prompt)
            if(inputit != ''):
                # you actually entered something (not just pressing enter)
                unitid = inputit;
                unitid = typeprefix+unitid;
                snmap[sn] = unitid;
                filemodified = True;
        else:
            # forced-accept
            pass;
    else:
        prompt = "Enter UNITID (none found): {:s}".format(typeprefix);
        #unitid = input("Enter UNITID (none found): {:s}".format(typeprefix));
        unitid = tkinter.simpledialog.askstring('Title2 Title2 Title2 Title2', prompt);
        unitid = typeprefix+unitid;
        snmap[sn] = unitid;
        filemodified = True;
    print('UNIT: {:s}'.format(unitid));

    # if snmap modified write back to file (truncating first)
    if(filemodified):
        with open(filenamecsv,mode='wt') as myfile:
            for k,v in snmap.items():
                myfile.write('{:s},{:s}\n'.format(k,v))

def do_part2(args=None):
    newdrive = None;

    print('-------------------------------')
    print('STARTING PART 2: Copy existing data (and optionally delete from device)');
    print('-------------------------------')

    # switch device to MSC and wait for driveletter
    newdrive = devicectl.toMSCandWait();

    # copy
    npocbb_tools.usb_file_utils_lite.copyAllFromDevice(
        DRIVE_LETTER=newdrive,
        DATAFOLDER=args.datadl_path,
        EXPERIMENT_NAME=args.datadl_expname,
        UNITID=unitid,
        DELETE_LOGS_AFTER_COPYALL=args.datadl_deleteafter,
    )

    # eject drive
    print('Ejecting drive gracefully...')
    npocbb_tools.usb_file_utils_lite.windowsEjectDrive(newdrive);
    print('Drive {:s} Ejected!'.format(newdrive));

    # exist MSC mode
    time.sleep(1);
    devicectl.mode_exitmsc();

def do_part3(args=None,fw_path=''):
    print('-------------------------------')
    print('STARTING PART 3: Firmware Update');
    print('-------------------------------')
    devicectl.dfu_fw_update(workingdir=fw_path.as_posix());

def do_part4(args=None):
    if(args.device_set_time != 'no'):
        print('-------------------------------')
        print('STARTING PART 4a: Set clock on device');
        print('-------------------------------')
        if(args.device_set_time=='localtime'):
            print('Setting to localtime')
            devicectl.setClock();
            time.sleep(0.1);
        else:
            print('Could not set to',args.device_set_time);
    else:
        print('')


    if(args.device_reformat):
        print('-------------------------------')
        print('STARTING PART 4b: Reformat');
        print('-------------------------------')
        time.sleep(0.1);
        print('Sending reformat command to device...')
        devicectl.mode_reformat();
        time.sleep(1.0);
        # print('Sending reformat command to device... a second time (workaround for V3.2rc4 problem)')
        # devicectl.mode_reformat();
    else:
        print('')


def do_stuff(args=None):
    print('ARGS:')
    print(args)
    #return;

    # verify uploadImage.bat exists
    #if(args.fw_path)
    fw_path = Path('');
    if(args.fw_path) is not None:
        fw_path = Path(args.fw_path);
    if(args.doPart3FW):
        if((fw_path.absolute()/'uploadImage.bat').exists()):
            print('found uploadImage.bat');
        else:
            #print('need uploadImage.bat in fw folder');
            raise RuntimeError('need uploadImage.bat in fw folder')

    # STEP 0 - waiting for device to be plugged in
    print('-----------------------------------------')
    print('waiting for device to be plugged in....')
    print('-----------------------------------------')
    
    devicectl.opencdc(keep_waiting=True); # will hold forever

    # STEP 1 - DEVICE ID
    do_part1(args);
    #devicectl.closecdc();

    # STEP 2 - COPY EXISTING FILES
    if args.doPart2Download:
        # should already be opened
        #devicectl.opencdc(keep_waiting=False); # will hold forever

        do_part2(args);
    else:
        print('-----------------------------------------')
        print('SKIPPING PART2 ...')
        #devicectl.closecdc();

    # STEP 3 - FIRMWARE UPDATE
    if args.doPart3FW:
        # should already be opened
        #devicectl.opencdc(keep_waiting=False); # will hold forever

        do_part3(args,fw_path);
    else:
        print('-----------------------------------------')
        print('SKIPPING PART3 ...')

    # STEP 4 - DO OTHER DEVICE OPS
    do_part4(args);



    # FINAL
    print('-----------------------------------------')
    print('PROGRAM DONE !!!')
    print('-----------------------------------------')
    print('Final device status query:');
    print(devicectl.query_STATUS());

    # RELEASE COM PORT
    print('');
    devicectl.closecdc();

    # print(f"The file you chose is {args.file_path}")
    # print(f"The folder you chose is {args.directory_path}")
    # print(f"The first checkbox value is {args.checkbox_1}")
    # print(f"The second checkbox value is {args.checkbox_2}")

    # if args.checkbox_1:
    #     print(f"The first checkbox is unchecked")

    # else:
    #     print(f"The first checkbox is checked")

    # if args.checkbox_2:
    #     print(f"The second checkbox is checked")
        
    # else:
    #     print(f"The second checkbox is unchecked")   

    #print("All done!")

@Gooey(
    program_name="nPOC-BB Module Device Wrangler V0.4",
    program_description="A tool to do any or all of the following: automatically identify, download data, update firmware, and/or set device settings.",
    default_size=(700, 800),
)

def main():
    parser = GooeyParser()

    #-- group 1 - device identification
    group1 = parser.add_argument_group("Step 1. Device ID");
    group1.add_argument(
        "--id-silent",
        metavar="Silent",
        help="Do not ask for device id if it was previously known",
        widget="BlockCheckbox",
        gooey_options=dict(checkbox_label='Auto accept confirmed ID'),
        default=True,  action="store_false"
        #default=True,  
    );


    #-- group 2 - download existing data from the device
    group2 = parser.add_argument_group("Step 2. Download / save existing data on the device",
        gooey_options={
                #'columns': 3,
                #'show_border':True
            }
    );
    group2.add_argument(
        "--doPart2Download",
        metavar="ENABLE",
        help="If checked this step will download all from filesystem.",
        widget="CheckBox",
        default=True,  action="store_false"
    );
    group2b = group2.add_argument_group("Options",
        gooey_options={
                'columns': 2,
                'show_border':True
            }
    );
    group2b.add_argument(
        "--datadl-expname",
        metavar="Experiment Name",
        help="Name of the experiment. This will become a subfolder in the root folder below.",
        #widget="CheckBox",
        #action="store_false",
        #default=True,  
        default=time.strftime('%Y%m%d_{:s}_autodl'.format(PC_USERNAME)),
    );
    group2b.add_argument(
        "--datadl-deleteafter",
        metavar="Delete log files after",
        help="If checked this step will delete logfiles from device after ensureing they've been downloaded",
        widget="CheckBox",
        action="store_true",
    );
    group2b.add_argument(
        "--datadl-path",
        metavar="Data Dest Root Path",
        help="Choose root folder where you will download the data. Subfolder with unit-name will contain the data. Folders (and parents) will automatically be created if they do not exist.",
        widget="DirChooser",
        gooey_options={
                    'full_width': True
                },
        default=r'C:\\TEMP\\NPOCBB_AUTODOWNLOADS'
    );

    #-- group 3 - firmware update
    group3 = parser.add_argument_group("Step 3. Firmware Update")
    group3.add_argument(
        "--doPart3FW",
        metavar="ENABLE",
        help="If checked, this step will update the firmware on the device.",
        widget="CheckBox",
        action="store_true",
    );
    group3b = group3.add_argument_group("Options",
        gooey_options={
                'columns': 2,
                'show_border':True
            }
    );
    group3b.add_argument(
        "--fw-path",
        metavar="FW Path",
        help="""Choose a folder where the firmware you want to flash is at.
If this is blank, it will be calling uploadImage.bat in the current folder (current folder is {:s}).""".format(Path().absolute().as_posix()),
        widget="DirChooser",
        gooey_options={
                    'full_width': True
                },
    );

    #-- group 4 - other device actions
    group4 = parser.add_argument_group("Step 4. Other device actions")
    group4.add_argument(
        "--device-set-time",
        metavar="4a. Set device RTC time",
        help="Set the device clock through CDC command",
        choices=['no', 'localtime','zulutime (not implemented)'],
        default='localtime',  
    )
    # group4a = group4.add_mutually_exclusive_group()
    # group4a.add_argument('--verbozze', dest='verbose',
    #                        action="store_true", help="Show more details")
    # group4a.add_argument('--set-rtc-list', dest='quiet',
    #                        action="store_true", help="Only output on error")
    group4.add_argument(
        "--device-reformat",
        metavar="4b. Reformat",
        help="Reformat filesystem (config will default, logs will be purged)",
        widget="BlockCheckbox",
        gooey_options=dict(checkbox_label='Reformat'),
        action="store_true",
        #default=False,
    );

    #-- group 5 - copy a customized config to the device
    group5 = parser.add_argument_group("Step 5. Copy a customized config onto the device")
    group5.add_argument(
        "--doPart5",
        metavar="ENABLE (NOT IMPLEMENTED YET)",
        help="If checked this step will copy a specialty config onto the device.",
        widget="CheckBox",
        action="store_false",
        default=False
    );

    #-- group 6 - copy a customized config to the device
    group6 = parser.add_argument_group("Step 6. Other program actions")
    group6.add_argument(
        "--loop",
        metavar="Loop (NOT IMPLEMENTED YET)",
        help="When program completes successfully, it will wait for a new device.",
        widget="CheckBox",
        action="store_true"
    );



    
    args = parser.parse_args()

    # checkbox workaround; negative the ones that default to "checked"
    # https://github.com/chriskiehl/Gooey/issues/148
    args.id_silent = not args.id_silent;
    args.doPart2Download = not args.doPart2Download;

    do_stuff(args)

if __name__ == "__main__":
    main()