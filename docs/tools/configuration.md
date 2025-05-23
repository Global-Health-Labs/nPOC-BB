# File System

The file system on the exposed mass storage device and NOR flash 1Gbit storage apart of the GHL Sample Preparation NAATOS device. 
The file system contains two sub directories containing all necessary files for the configuration of the device and all logs created by the device. 


    /
    ├─ logs
    │   ├─ sample_12-03-24_121449.csv
    |   └─ sample_12-05-24_120343.csv
    └─ config
        └─ config_2.3b.txt

Configs Subdirectory
The “configs” subdirectory will contain the device specifications (e.g. sample rate, log rate, etc.). These device specifications will be inside of the configuration file inside of the config subdirectory directory. 
Device parameters inside of the configuration file and their function:

…
The configuration file that is created is named after the current revision of the software that is on the unit. The created configuration file will follow the format of config_XX.txt where XX is the version of the software on the unit.  For example, if the firmware version of the unit was 2.3b, the created configuration file would be config_2.3b.txt.

When a new firmware version is uploaded to a unit, the unit will cross check the current firmware version against the configuration file in storage. If the version of the firmware and the configuration file do not match, the device will delete the current configuration file in storage and create a new one for the current version. This is done so that if the configuration parameters are updated/changed between versions the firmware is guaranteed a good configuration file.
Logs Subdirectory
The “logs” subdirectory will contain all the logs of each sample preparation run on the device. Every time a sample run is performed a new sample log will be created and put into the “logs” directory. The created log file will be named in the format: sample_MM-DD-YY_HHMMSS.csv
The log files will keep track of the current time, heater board temperature, heater board normalized PWM, motor speed, motor normalized PWM, battery percentage, battery voltage, battery temperature and events. They will also be a .csv file so that the stored data can be easily opened in excel and used for graphing and data analysis. The logs will follow the following format.
Time,HeaterTemp,HeaterPWM,MotorSpeed,MotorPWM,Battery,BatteryV,BatteryT,Event
2024-12-05 12:04:34,24.01,100.00,0.00,0.00,19,3.57,25.03,Cycle 1 Started.
2024-12-05 12:04:35,26.39,100.00,0.00,0.00,19,3.63,25.05
2024-12-05 12:04:36,29.77,100.00,0.00,0.00,19,3.64,25.60

When opened in excel the data will look like:

Time	HeaterTemp	HeaterPWM	MotorSpeed	MotorPWM	Battery	BatteryV	BatteryT	Event
2024-12-05 12:04:34	24.01	100.00	0.00	0.00	19	3.57	25.03	Cycle 1 Started
2024-12-05 12:04:35	26.39	100.00	0.00	0.00	19	3.63	25.05	
2024-12-05 12:04:36	29.77	100.00	0.00	0.00	19	3.64	25.60	

Logs will also be created for events that occur in the system. These created log files will be two lines, one with the csv header, and another with all the logging information plus the event that has occurred. An example of a log file that is created in this way is the power on log file which creates a log file when the device has been powered on to show the starting battery voltage.
