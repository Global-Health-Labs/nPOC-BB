#
# Simon Ghionea
# 01/27/2025
#
# Place into this module, tools to read nPOC-BB log-files
#
# adapted from some Andy Miller starting code
# 

import os
from pathlib import Path

import pandas as pd
import numpy as np

badfolders = ['_ignore','archive'];

def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def as_timestamp_with_quirks(time_str):
    # if time is unset on RTC, the year and month is weirdly 2000-00, which cannot be parsed by pandas because the month is 0
    time_str = time_str.replace('2000-00','2000-01');
    #df_in['Time'] = df_in['Time'].apply(lambda x: pd.Timestamp(x))

    # # quirks observed on weekend test 2024-11-25
    # # 2024-11-22 19:12:06,44.04,100.00,0.00,0.00,87,3.95,23.46 
    # # 2080-00-00 24:11:02,46.72,100.00,0.00,0.00,87,3.95,23.56 
    # # 2024-11-22 19:12:08,49.35,100.00,0.00,0.00,87,3.95,23.78 
    # # notice the year 2080 and month 00 !!! and the times are weird
    # # let's deal with this by returning None, so the line is skipped
    # if(time_str.startswith("2080-00-00")):
    #    return None;

    # quirks observed on weekend test 2024-11-25
    # 2024-11-22 19:12:06,44.04,100.00,0.00,0.00,87,3.95,23.46 
    # 2080-00-00 24:11:02,46.72,100.00,0.00,0.00,87,3.95,23.56 
    # 2024-11-22 19:12:08,49.35,100.00,0.00,0.00,87,3.95,23.78 
    #
    # 2009-11-00 00:00:00,0.00,43.90,0.00,0.00,34,3.74,12.64,Cycle 1 Started.
    # 2024-11-23 09:11:07,64.34,100.00,0.00,0.00,34,3.68,12.64 
    #
    # another example: 2080-00-11 03:23:19
    #
    # notice the year 2080, 2009 and month 00 !!! and the times are weird
    # let's deal with this by returning NaN, so the line is skipped
    #if(time_str.startswith("2080-00-00")):
    if(time_str.split(" ")[0].split('-')[2]=="00"):
       # day slot was 0, invalid
       return np.nan;
    if(time_str.split(" ")[0].split('-')[1]=="00"):
       # month slot was 0, invalid
       return np.nan;
    

    # now cast to timestamp
    return pd.Timestamp(time_str);

def scanALogfile(filepath, unit='nounit', expname='noexp'):
    file = os.path.basename(filepath); 
    if( os.path.getsize(filepath) == 0 ):
        print('File',file,'had zero-size! Ignoring')
        return (None,None);

    df_in = pd.read_csv(filepath);

    #df_in['Time'] = df_in['Time'].str.replace('2000-00','2000-01');
    #df_in['Time'] = df_in['Time'].apply(lambda x: pd.Timestamp(x))
    df_in['Time'] = df_in['Time'].apply(as_timestamp_with_quirks);

    # bad times????
    # report rows with NaN for time (quirks that we will deem unusable for now)
    n_bad_rows = df_in[ df_in['Time'].isna() ].shape[0];
    # if(n_bad_rows>0):
    #     print('file',file,'had {:d} rows with bad times that we are ignoring'.format( n_bad_rows ) )
    # #drop rows with NaN for time (seems to occur at start of logfile)
    # df_in = df_in[ df_in['Time'].notna() ]
    if(n_bad_rows>0):
        print('file',file,'had {:d} rows with bad times, we will use prior time'.format( n_bad_rows ) )
    badtimes_idx = df_in[df_in['Time'].isna()].index;
    if(0 in badtimes_idx):
        # for the bad timestamps, assume the time from the line immediately preceeding
        # note, this will fail if the very first line in the file had a bad time. For that, we'll catch and substitute the NEXT time
        print('file',file,'had a bad time in first row, use the next'.format( n_bad_rows ) )
        # replace the first index value of 0 with 2
        idxvals = badtimes_idx.values;
        idxvals[0] = 2;
        badtimes_idx = pd.Index(idxvals);
    df_in.loc[badtimes_idx,'Time'] = df_in.loc[badtimes_idx-1,'Time']

    #label with run and unit
    run = file[:-4]#[file[-9:-4] for x in range(len(df_in))] # can cheat because didn't end up making a 10th run
    df_in['run'] = run;
    df_in['unit']= unit;
    df_in['expname']= expname;
    

    # were there any rows?
    # if not, skip this file completely
    if(df_in.shape[0]==0):
        print('File',file,'had no rows! ignoring it')
        #continue;
        return (None,None);
    
    
    #normalize time
    #df_in['Time'] = [datetime.strptime(x, '%Y-%m-%dT%H:%M:%S') for x in df_in['Time']]
    #get year/month/day from config file and append to list? Defaults to 1900
    #testing_offset =  datetime.strptime(offset_datetimes[folder], '%Y-%m-%d %H:%M:%S.%f') #pull the actual test start time off the RTC here
    #f_in['Time'] = [x - df_in['Time'].iloc[0] + testing_offset for x in df_in['Time']]
    df_in['Time_str'] = [str(x) for x in df_in['Time']]#record for human readibility
    
    start_time = df_in['Time'].iloc[0]

#    df_in['runtime'] = [get_sec(time) for time in df_in['Time']] #use for the x-axis labels
    df_in['runtime'] = [(x - start_time).total_seconds() for x in df_in['Time']]

    events = [x for x in df_in['Event'] if type(x) is str] #gets evenst but need associated time for it

    #scrape events and add as text to Bokeh
    #drop all rows that are whitespace
    df_events = df_in[df_in['Event'].apply(lambda x: False if (type(x) is not str) else True)] #keep only rows with events populated
    #Now turn those into manual points to display on Bokeh
    #manual_points provide a list of points to be added to the graph along with optional text ([[x,y],[kind],text(optional)]
    offset = 0
    for row, event in df_events.iterrows():
        offset = offset + 5
        #manual_points.append([[event['runtime'], offset], 'text', event['Event']]) #append the text
        #manual_points.append([[event['runtime'], offset], 'diamond', '']) #add a glyph too


    #df_list.append(df_in) #for all runs in one plot
    #df_list_all_folders.append(df_in) #for all runs in one plot

    #print('Done loading log {:s}'.format(os.path.basename(file)))
    return (df_in,df_events);


def scanAUnitFolder(unitfolder):
    global config_string;
    global config_file;

    #open each logfile and import into Pandas df
    folders = [ name for name in os.listdir(unitfolder) if os.path.isdir(os.path.join(unitfolder, name)) ]

    #drop any folders with names we don't like such as "archive" or "_ignore"
    #badfolders = ['_ignore','archive','LowerStallThreshold','IssueLogs'];
    #badfolders = ['_ignore','archive'];
    # this is set a module-level
    for badfolder in badfolders:        
        if(badfolder in folders):
            folders.remove(badfolder);
    print(folders);

    if( ('config' in folders) and ('logs' in folders)):
        # we are pointed towards a single-device run
        folders = ['logs'];

        # go ahead and load the config!
        config_file = [f for f in (Path(unitfolder)/'config').iterdir() if (f.name.startswith('config_') and f.name.endswith('txt'))][0]
        with open(config_file, 'r') as f:
            config_string = f.read()
    elif( ('logs' in folders) ):
        # we are pointed towards a single-device run
        folders = ['logs'];

        # there is not config files

        # # go ahead and load the config!
        # config_file = [f for f in (Path(unitfolder)/'config').iterdir() if (f.name.startswith('config_') and f.name.endswith('txt'))][0]
        # with open(config_file, 'r') as f:
        #     config_string = f.read()
        config_string = '';
        config_file = 'noconfigfile';

    elif(len(folders)==0):
        # there were no folders in the unit folder

        # assume that there are a bunch of run logfiles in here
        config_string = '';
        config_file = 'noconfigfile';
        folders = ['.']
    else:
        print('Badfolders',badfolders);
        raise RuntimeError("Folder not in expected format")

    
    df = pd.DataFrame()
    df_in = pd.DataFrame()
    df_list_all_folders = []

    for folder in folders:
        files = [ name for name in os.listdir(os.path.join(unitfolder,folder)) if name[-4:] == '.csv' ]
        print('Folder ' + folder)

        #unit = (Path(root)/folder).parent.parent.name;
        #expname = (Path(root)/folder).parent.name;
        unit = os.path.basename(unitfolder);
        expname = (Path(unitfolder)).parent.name;

        manual_points = []
        #df_in = pd.DataFrame()
        #df_tc = pd.DataFrame()
        #df_list = []

        for file in files:
            #try:
            #doesn't account for the two flavors of files
            #print('Loading ' + file)

            if file[0:6] == 'sample': #from the logfile
                df_in,df_events = scanALogfile(os.path.join(unitfolder,folder,file),unit,expname);
            #     #print('Loading sample prep logfile')
            #     df_in = pd.read_csv(os.path.join(unitfolder, folder, file))

            #     #df_in['Time'] = df_in['Time'].str.replace('2000-00','2000-01');
            #     #df_in['Time'] = df_in['Time'].apply(lambda x: pd.Timestamp(x))
            #     df_in['Time'] = df_in['Time'].apply(as_timestamp_with_quirks);

            #     # bad times????
            #     # report rows with NaN for time (quirks that we will deem unusable for now)
            #     #df_in.dropna()
            #     n_bad_rows = df_in[ df_in['Time'].isna() ].shape[0];
            #     if(n_bad_rows>0):
            #         print('file',file,'had {:d} rows with bad times that we are ignoring'.format( n_bad_rows ) )

            #     #drop rows with NaN for time (seems to occur at start of logfile)
            #     df_in = df_in[ df_in['Time'].notna() ]

            #     #label with run and unit
            #     run = file[:-4]#[file[-9:-4] for x in range(len(df_in))] # can cheat because didn't end up making a 10th run
            #     df_in['run'] = run
            #     df_in['unit']= unit
            #     df_in['expname']= expname
                

            #     # were there any rows?
            #     # if not, skip this file completely
            #     if(df_in.shape[0]==0):
            #         print('File',file,'had no rows! ignoring it')
            #         continue;
                
                
            #     #normalize time
            #     #df_in['Time'] = [datetime.strptime(x, '%Y-%m-%dT%H:%M:%S') for x in df_in['Time']]
            #     #get year/month/day from config file and append to list? Defaults to 1900
            #     #testing_offset =  datetime.strptime(offset_datetimes[folder], '%Y-%m-%d %H:%M:%S.%f') #pull the actual test start time off the RTC here
            #     #f_in['Time'] = [x - df_in['Time'].iloc[0] + testing_offset for x in df_in['Time']]
            #     df_in['Time_str'] = [str(x) for x in df_in['Time']]#record for human readibility
                
            #     start_time = df_in['Time'].iloc[0]
            
            # #    df_in['runtime'] = [get_sec(time) for time in df_in['Time']] #use for the x-axis labels
            #     df_in['runtime'] = [(x - start_time).total_seconds() for x in df_in['Time']]
            
            #     events = [x for x in df_in['Event'] if type(x) is str] #gets evenst but need associated time for it
            
            #     #scrape events and add as text to Bokeh
            #     #drop all rows that are whitespace
            #     df_events = df_in[df_in['Event'].apply(lambda x: False if (type(x) is not str) else True)] #keep only rows with events populated
            #     #Now turn those into manual points to display on Bokeh
            #     #manual_points provide a list of points to be added to the graph along with optional text ([[x,y],[kind],text(optional)]
            #     offset = 0
            #     for row, event in df_events.iterrows():
            #         offset = offset + 5
            #         manual_points.append([[event['runtime'], offset], 'text', event['Event']]) #append the text
            #         manual_points.append([[event['runtime'], offset], 'diamond', '']) #add a glyph too
            
                if(df_in is not None and df_events is not None):
                    #df_list.append(df_in) #for all runs in one plot
                    df_list_all_folders.append(df_in) #for all runs in one plot

                    print('Done loading log {:s}'.format(os.path.basename(file)))
                else:
                    print('Skipped log {:s}'.format(os.path.basename(file)))
                
            else:
                print('Unknown csv: ' + file)

    if(len(df_list_all_folders)>0):
        df = pd.concat(df_list_all_folders)
    else:
        df = pd.DataFrame();
    df = df;
    return df;

def processADirectory(dirpath):
    #get listing of the given root directory
    folders = [ name for name in os.listdir(dirpath) if os.path.isdir(os.path.join(dirpath, name)) ]

    data_unit_list = [];
    if( ('config' in folders) and ('logs' in folders)):
        # we are pointed towards a single-device run
        print('The folder had one device run (unsupported now)');

    else:
        print('The folder we will assume each folder are UNITS')

        for unitfolder in folders:
            print('folder "{:s}"'.format(unitfolder));
            dfunit = scanAUnitFolder(os.path.join(dirpath,unitfolder));
            data_unit_list.append(dfunit);

    # concatenate across all units
    df = pd.concat(data_unit_list);

    return df;

def processRootFolder(
        rootpath = r'C:\\Users\\SimonGhionea\\Global Health Labs, Inc\\NAATOS Product Feasibility - General - Internal - Electronic Control Module\\Beta design\\SamplePrepTestData\\by_exp',
        experiments_to_plot = [ '20250123_3.0_ghlhack_1b']
        ):
    print('Processing rootfolder',rootpath);
    dfs_collected = [];
    for exp in experiments_to_plot:
        print('Experiment',exp);
        
        dfraw = processADirectory( dirpath=(rootpath/exp).as_posix() );
        dfs_collected.append(dfraw);
    return pd.concat(dfs_collected);


def getFilesByExpUnitRun(
        rootpath = r'C:\\Users\\SimonGhionea\\Global Health Labs, Inc\\NAATOS Product Feasibility - General - Internal - Electronic Control Module\\Beta design\\SamplePrepTestData\\by_exp',
        #experiments_to_plot = [ '20250123_3.0_ghlhack_1b']
        experiment='20250404_PM_fromDX',
        unit='Unit 20',
        run='sample_03-28-25_162713',
    ):
    # print('Processing rootfolder',rootpath);
    # dfs_collected = [];
    # for exp in experiments_to_plot:
    #     print('Experiment',exp);
        
    #     dfraw = processADirectory( dirpath=(rootpath/exp).as_posix() );
    #     dfs_collected.append(dfraw);
    # return pd.concat(dfs_collected);
    folder=(Path(rootpath)/experiment)/unit;
    
    return_logfile = (None,None);
    if( (folder/'logs').exists() ):
        logfolder = folder/'logs';
        logfilename = logfolder/(run+'.csv');
        if( logfilename.exists() ):
            with open(logfilename, 'r') as f:
                return_logfile = ( logfilename,    f.read());
    else:
        logfolder = folder;
        logfilename = logfolder/(run+'.csv');
        if( logfilename.exists() ):
            with open(logfilename, 'r') as f:
                return_logfile = ( logfilename,    f.read());

    
    # TODO: also get config file info
    return_configfiles = (None,None);
    
    return (return_logfile, return_configfiles);