import subprocess
import npocbb_tools.npocbb_paths as npocbb_paths
import serial.tools.list_ports



CFG_NRF_UTILS_BATCH_FOLDER = npocbb_paths.CFG_PATH_NRF_UTILS_BATCHFILES;
if(CFG_NRF_UTILS_BATCH_FOLDER == ''):
    raise RuntimeError("check npocbb_paths.py, CFG_NRF_UTILS_BATCH_FOLDER was blank")



def run_nrfutil_batch_and_wait(DFU_COMPORT):
    """Launches the uploadImage.bat file and passes as argument the com port

    Args:
        DFU_COMPORT (str): COM port (e.g., "COM4")
    """    

    # get comport
    #CFG_DFU_COMPORT = loop_until_dfu_comport_found();
    # There is not enough time to do this!!!
    # By the time we launch the below .bat file the com port dissapeared :-(

    subprocess.run(
        #["start", "cmd", "/k", CFG_NRF_UTILS_BATCH_FOLDER+'\\uploadImage.bat'],
        # /k - This option tells the command prompt to keep running after the batch file finishes
        # /c - Carries out the command specified by string and then terminates
        ["start", "/wait", "cmd", "/c", CFG_NRF_UTILS_BATCH_FOLDER+'\\uploadImage.bat',DFU_COMPORT],
        cwd=CFG_NRF_UTILS_BATCH_FOLDER
        , shell=True
    )

def run_nrfutil_batch_return_process(DFU_COMPORT):
    """Launches the uploadImage.bat file and passes as argument the com port

    Args:
        DFU_COMPORT (str): COM port (e.g., "COM4")
    """    

    # get comport
    #CFG_DFU_COMPORT = loop_until_dfu_comport_found();
    # There is not enough time to do this!!!
    # By the time we launch the below .bat file the com port dissapeared :-(

    ret = subprocess.Popen(
        #["start", "cmd", "/k", CFG_NRF_UTILS_BATCH_FOLDER+'\\uploadImage.bat'],
        # /k - This option tells the command prompt to keep running after the batch file finishes
        # /c - Carries out the command specified by string and then terminates
        ["start", "/wait", "cmd", "/c", CFG_NRF_UTILS_BATCH_FOLDER+'\\uploadImage.bat',DFU_COMPORT],
        cwd=CFG_NRF_UTILS_BATCH_FOLDER
        , shell=True
    )
    return ret;

def loop_until_dfu_comport_found():
    print('Waiting (infinite loop) for a comport that has description "nRF52 SDFU USB" ...');
    while True:
        for i in serial.tools.list_ports.comports():
            if(i.description.startswith("nRF52 SDFU USB")):
                print('Found it on ',i.name,'!');
                return i.name;
            else:
                # keep waiting
                pass;

def windowsDeleteNRFSDFUComPorts():
    """
    Launch a powershell as Administrator and launch a .ps1 script which will delete the NRF SDFU com ports on the windows system

    This will allow it to always enumerate NRF DFU serial port on the same COM port across all the units
    
    """
    p = subprocess.run(
        [
            "powershell.exe", 
            "-noprofile", "-c",
            # r"""
            # Start-Process -Verb RunAs -Wait powershell.exe -ArgumentList ('-NoExit','-ExecutionPolicy','remotesigned','-C', '& \"C:\\Users\\SimonGhionea\\OneDrive - Global Health Labs, Inc\\ProjectsCloud\\NAATOS\\sgpyanalysisnaatos\\windowsUninstallNRF51COMPORTS.ps1\"')
            # """
            r"""
            Start-Process -Verb RunAs -Wait powershell.exe -ArgumentList ('-ExecutionPolicy','remotesigned','-C', '& \"C:\\Users\\SimonGhionea\\OneDrive - Global Health Labs, Inc\\ProjectsCloud\\NAATOS\sgpyanalysisnaatos\\windowsUninstallNRF51COMPORTS.ps1\"')
            """
        ]
    );
