from pathlib import Path
import platform
import os

# username
_mylogin = os.environ.get('USER', os.environ.get('USERNAME'));
# win32 or linux
_myplatform = platform.sys.platform;
# computer name
_mycomputer = platform.node();

# paths
CFG_PATH_NRF_UTILS_BATCHFILES = '';
CFG_PATH_TEAMS_BETA_SAMPLEPREPTESTDATA = '';

if(_mylogin=="SimonGhionea"):
    print('Hi Simon')
    if(_myplatform == "win32" and _mycomputer=="GHL-5N0T5M3"):
        print('you are on your 64gb laptop')
        # simon 64gb laptop

        CFG_PATH_NRF_UTILS_BATCHFILES = r'D:\\SGProjects\\NAATOS\\V1\\FW_PRODUCTION_Shared_by_ODIC_OneDrive_2024-10-29\\sample prep';
        CFG_PATH_TEAMS_BETA_SAMPLEPREPTESTDATA = r'C:\\Users\\SimonGhionea\\Global Health Labs, Inc\\NAATOS Product Feasibility - General - Internal - Electronic Control Module\\Beta design\\SamplePrepTestData';
else:
    pass;
