How to upload bootloader and a firmware to the device with J-Link
-----------------
#1. Use NORDIC Connect / Device Programmer
#2. It works with functional J-Link debugger
#3. Connect device, powered up, with the JLINK on the Tag-Connect header near USB.
#4. Copy a relocated .hex file compiled with SEGGER Embedded Studio, to here.
#5. Run make_settings.bat
#6. Drag these four files to NORDIC Device Programmer:
	- mbr_nrf52_24.1_mbr.hex
	- npoc-bb_bootloader_settings.hex
	- npoc-bb_bootloader_SG_compilerelease_NORELOC.hex
	- npoc-bb_fw.hex
#7. Click "Erase and Write All" in Device Programmer.
#8. There should be no red messages in the status indication, to indicate success
