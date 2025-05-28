How to upload bootloader and a firmware to the device with J-Link
-----------------
#1. Use NORDIC Connect / Device Programmer
#2. It works with functional J-Link debugger
#3. Connect device, powered up, with the JLINK on the Tagconnect header near USB.
#4. Copy a relocated .hex file compiled with SEGGER Studio, to here.
#5. Run make_settings_this.bat
#6. Drag these 4 files to Nordic Device Programmer:
	- mbr_nrf52_24.1_mbr.hex
	- naatos_bootloader_settings.hex
	- NAATOS_bootloader_SG_compilerelease_NORELOC.hex
	- NAATOS_fw.hex
#7. Click "Erase and Write All" in Device Programmer.
#8. There should be no red messages in the status indication, to indicate success
