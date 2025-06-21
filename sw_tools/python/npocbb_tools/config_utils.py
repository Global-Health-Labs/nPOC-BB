import time

def getConfigFileText(TEMPLATE_CONFIG_FILE_PATH,set_time=True,unitid='blahblah'):
    # Read template config file into memory
    print('Reading',TEMPLATE_CONFIG_FILE_PATH);
    with open(TEMPLATE_CONFIG_FILE_PATH, 'r') as file:
        # read existing file into memory as string
        strconfig = file.read();

    # split into lines
    configlines = strconfig.split('\n');

    # find and alter appropriate lines: mmddyy
    line_number = [s.find('mmddyy:')==0 for s in configlines].index(True);
    configlines[line_number] = time.strftime('mmddyy:%m%d%y');
    # find and alter appropriate lines: mmhhss
    line_number = [s.find('hhmmss:')==0 for s in configlines].index(True);
    configlines[line_number] = time.strftime('hhmmss:%H%M%S');
    # find and alter appropriate lines: set_time_date
    line_number = [s.find('set_time_date:')==0 for s in configlines].index(True);
    configlines[line_number] = 'set_time_date:true';

    # rejoin into a single string
    strconfig_new = '\n'.join(configlines);

    if False:
        # add a whoami line at the beginning
        strconfig_new = 'whoami:{:s}\n'.format(unitid) + strconfig_new;

    return strconfig_new;
