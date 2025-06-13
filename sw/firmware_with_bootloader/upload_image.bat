@echo off
REM Check if the COM port parameter is provided
if "%1"=="" (
    echo Usage: dfu_update.bat COM_PORT
    echo Example: dfu_update.bat COM24
    exit /b 1
)

REM Assign the first parameter to COM_PORT variable
set COM_PORT=%1

REM Run the nrfutil command with the specified COM port
.\nrfutil.exe dfu usb-serial -pkg npoc-bb_dfu_package.zip -p %COM_PORT% -b 115200

REM Exit the script
exit /b 0