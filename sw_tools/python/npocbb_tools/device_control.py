#%% imports
import serial
import serial.tools.list_ports
import time
import subprocess

import npocbb_tools.usb_file_utils_lite

def _findCDCport(keep_waiting=False):
    vid="1915";
    pid="520D";
    while(True):
        ports = list(serial.tools.list_ports.comports());
        thedev = None;
        for cnt,p in enumerate(ports):
            if((pid in p.hwid) and (vid in p.hwid)):
                thedev = p.device;

        if(thedev is None and keep_waiting):
            print('Waiting for device with VID:{:s} PID:{:s}...'.format(vid,pid))
            time.sleep(0.5);
            continue;
        else:
            #print('Found',p.hwid);
            if(thedev is None):
                p = None;
            return thedev,p;

class NPOCBB_CONTROLLER:
    _sercdc = None;
    status_data = {};
    def __init__(self):
        pass;
    def opencdc(self,keep_waiting=False):
        comportserial,portinfo = _findCDCport(keep_waiting);
        if(portinfo is not None):
            print('Found',portinfo.hwid);
        time.sleep(0.25);
        try:
            self._sercdc = serial.Serial(comportserial,115200,timeout=1);
        except serial.SerialException as e:
            print('Did you forget to close this serial port ({:s}) in another program?'.format(comportserial));
            raise(e);

    def closecdc(self):
        if(self._sercdc is not None):
            print('Closing port');
            self._sercdc.close();
    
    def toMSCandWait(self):
        drivelist_pre = npocbb_tools.usb_file_utils_lite.getDriveList2();
        print('Current Drive List:',[x['DeviceID'] for x in drivelist_pre]);

        # transition to MSC mode
        self.mode_tomsc();

        # wait for a new drive to appear
        while(True):
            print('Wait for drive...')
            time.sleep(1.0);
            drivelist_post = npocbb_tools.usb_file_utils_lite.getDriveList2();

            newdrive = set([x['DeviceID'] for x in drivelist_post])-set([x['DeviceID'] for x in drivelist_pre]);
            if(len(newdrive)>0):
                # new drive appeared
                newdrive = newdrive.pop();
                print('Device MSC appeared at',newdrive);
                newdriveinfo = [x for x in drivelist_post if x['DeviceID']==newdrive][0];
                break;
            else:
                # no new drive yet, keep waiting
                continue;

        # new driveinfo
        print(newdriveinfo);
        return newdriveinfo['DeviceID'];

    def query_STATUS(self):
        sercdc = self._sercdc;

        # query for status
        sercdc.flush(); # eliminate everything in read buffer
        sercdc.write(b'STATUS,\n');
        time.sleep(0.05);
        rxdata = sercdc.read_all();

        #% parse rx
        rxlines = [l for l in rxdata.decode().strip().splitlines() if l != ''] # skip blank lines
        #print(rxlines)
        #print([l.find('=') for l in rxlines])
        # pick lines which contain an '=' sign
        rxlines_sel = [l for l in rxlines if l.find('=')>0]
        print(rxlines_sel)

        status_data = {};
        for s in rxlines_sel:
            #print('s',s)
            # split with space
            s2 = s.split(' ')
            #print('s2',s2[2:])
            for s3 in s2[2:]:
                #print('s3',s3)
                s4 = s3.split('=');
                #print('s4',s4)
                if(len(s4)==2):
                    key = s4[0];
                    val = s4[1];
                    val = val.replace('\"','');

                    status_data[key] = val;
                elif(s.find('TS')>=0):
                    # special handling for the space in the "ts" field
                    val = s4[0].replace('\"','');
                    #print('val',val);

                    status_data['TS']+=' '+val;
                else:
                    #print("Hello i'm here!");
                    pass;
        self.status_data = status_data;
        return status_data;

    def setClock(self):
        sercdc = self._sercdc;

        cmdstr = time.strftime('SETCLK,%Y-%m-%d %H:%M:%S\n');
        # send command
        sercdc.write(cmdstr.encode());
        time.sleep(0.25);
        # read
        lines = [];
        keep_readinglines_until_rx = 'Readback time';
        while(True):
            time.sleep(0.05);
            try:
                rxdata = sercdc.read_all();
            except serial.SerialException as e:
                print('Serial port dissapeared before we could read it! That is fine here...')
                break;

            rxdecoded = rxdata.decode();
            if(rxdecoded !=''):
                print(rxdecoded.strip());
                lines+=rxdecoded.splitlines();
            if(keep_readinglines_until_rx is not None):
                if(rxdecoded.find(keep_readinglines_until_rx)>=0):
                    break;
                else:
                    continue;
            else:
                break;
        # check we got a reception of "Readback time"
        # print(rxdata.decode().splitlines()[-2])
        # if 'Readback time' not in rxdata.decode():
        #     print('COULD NOT SET TIME')

    def _transition_modes(self,command='TOMSC',keep_readinglines_until_rx=None):
        #% TOMSC,EXITMSC,REFORMAT
        sercdc = self._sercdc;

        # send command
        sercdc.write(command.encode()+b',');

        #sercdc.write(b'{:s},'.format(command));
        #boolContinue = True if keep_readinglines_until_rx is None else keep_readinglines_until_rx;
        #while(boolContinue)
        while(True):
            time.sleep(0.05);
            try:
                rxdata = sercdc.read_all();
            except serial.SerialException as e:
                print('Serial port dissapeared before we could read it! That is fine here...')
                break;

            rxdecoded = rxdata.decode();
            if(rxdecoded !=''):
                print(rxdecoded.strip());
            if(keep_readinglines_until_rx is not None):
                if(rxdecoded.find(keep_readinglines_until_rx)>=0):
                    break;
                else:
                    continue;
            else:
                break;

        # wait for COM available
        while(True):
            try:
                sercdc.in_waiting
            except serial.SerialException as e:
                print('Device Was Removed')
                while(True):
                    comportserial = _findCDCport()
                    if comportserial is not None:
                        print('Device re-opened comport')
                        break;
                break;
        time.sleep(1.0);
        #sercdc = serial.Serial(comportserial,115200,timeout=1);
        self.opencdc(keep_waiting=True);

    def mode_tomsc(self):
        self._transition_modes('TOMSC');

    def mode_exitmsc(self):
        self._transition_modes('EXITMSC');

    def mode_reformat(self):
        self._transition_modes('REFORMAT','SUCCESS');

    def dfu_fw_update(self,workingdir=None):
        import serial.tools.list_ports

        sercdc = self._sercdc;

        # send command
        sercdc.write(b'TODFU,');

        #sercdc.write(b'{:s},'.format(command)); 
        time.sleep(0.01);
        rxdata = sercdc.read_all();
        print(rxdata.decode())

        # device will now enter DFU mode, windows mounts to a new location
        # so begin to query the ports
        dfu_vid = '1915';
        dfu_pid = '521F';
        print('Waiting for DFU device ({:s}:{:s})'.format(dfu_vid,dfu_pid));
        dfudev = None;
        while(dfudev is None):
        #for i in range(50):
            ports = list(serial.tools.list_ports.comports());
            time.sleep(0.01);
            for cnt,p in enumerate(ports):
                #print('Enumerate {:d} = {:s}'.format(cnt,p.description))
                #print('\tUSBINFO: {:s}'.format(p.usb_info()))
                #print('Enumerate {:d} = {:s} [{:s}]'.format(cnt,p.description,p.usb_info()))
                if((dfu_pid in p.hwid) and (dfu_vid in p.hwid) and (p.description != 'n/a')):
                    #print('Found DFU --> {:s}'.format(dfudev));
                    print('Found Details -> {:s} [{:s}]'.format(p.description,p.usb_info()))
                    dfudev = p.device;
                    break;
        print('Found DFU --> {:s}'.format(dfudev));

        # Launch uploadImage.bat script in background
        print('Launching uploadImage.bat...')
        # phandle = subprocess.Popen(
        #     #["start", "cmd", "/k", CFG_NRF_UTILS_BATCH_FOLDER+'\\uploadImage.bat'],
        #     # /k - This option tells the command prompt to keep running after the batch file finishes
        #     # /c - Carries out the command specified by string and then terminates
        #     ["start", "/wait", "cmd", "/c", 'uploadImage.bat',dfudev],
        #     cwd=workingdir,
        #     shell=True
        # )
        # lots of nuance with start and cmd and return codes
        # https://stackoverflow.com/questions/50315227/cannot-get-exit-code-when-running-subprocesses-in-python-using-popen-and-start
        # this below seems to work
        phandle = subprocess.Popen(
            # CMD options
            # /k - This option tells the command prompt to keep running after the batch file finishes
            # /c - Carries out the command specified by string and then terminates
            #["start", "/wait", "cmd", "/c", 'uploadImage.bat',dfudev],
            ['cmd','/c','uploadImage.bat',dfudev],
            cwd=workingdir,
            creationflags=subprocess.CREATE_NEW_CONSOLE,    # so we can see the shell terminal window
            shell=False
        )
        print('command launched. Delaying slightly for 5seconds...')
        for i in range(5,0,-1):    print(i);time.sleep(1);

        # find and re-open the USBCDC port
        print('Waiting to re-open USB CDC port...')
        self.opencdc(keep_waiting=True);
        sercdc = self._sercdc;
        sercdc.flush();

        # SEND TODFU AGAIN, this time uploadImage nrfutil script should be running in background
        # send command
        print('Sending TODFU to device...')
        time.sleep(0.5);
        sercdc.write(b'TODFU,');
        time.sleep(0.01);
        rxdata = sercdc.read_all();
        sercdc.close();
        print(rxdata.decode())

        # WAIT For nrfutil to end
        print('Waiting for uploadImage.bat to complete...')
        retcode = phandle.wait();
        print('DFU update script returned',retcode);
        if(retcode==0):
            # success
            pass;
        else:
            print('DFU update did not succeed!! Abort our entire script here...')
            raise RuntimeError("DFU update did not succeed!! Firmware not updated.")


        # find and re-open the USBCDC port
        print('Waiting for USB CDC port... (this may take a bit after fw update)')
        self.opencdc(keep_waiting=True);
        time.sleep(0.1);
        sercdc = self._sercdc;