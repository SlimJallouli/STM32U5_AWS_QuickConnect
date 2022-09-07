#******************************************************************************
# * @file           : STM32U5_AWS_QuickConnect.py
# * @brief          : Automatically registers new thing to AWS associated with connected STM32.
# ******************************************************************************
# * @attention
# *
# * <h2><center>&copy; Copyright (c) 2022 STMicroelectronics.
# * All rights reserved.</center></h2>
# *
# * This software component is licensed by ST under BSD 3-Clause license,
# * the "License"; You may not use this file except in compliance with the
# * License. You may obtain a copy of the License at:
# *                        opensource.org/licenses/BSD-3-Clause
# ******************************************************************************
from ast import Interactive
import sys
import subprocess
from tokenize import Name
from utils.getDeviceName import *
import getopt
import getpass
import platform

VERSION = "1.2.0"

SSID = 'st_iot_demo'
PSWD = 'stm32u585'

DUMMY_SSID = '0'
DUMMY_PSWD = '0'

DASHBOARD_KEY        = 'AKIAQC3VOUARXGGMWHHO'
DASHBOARD_SECRET_KEY = '7QbU0RSsSquT9Hv3SGO9VJIBfINysxmRjadiqGsS'
DASHBOARD_URL        = 'https://main.d3mkj47qkab3qo.amplifyapp.com'

PROVISION_AWS_PROFILE = 'default'

if platform.system() == 'Windows': 
    BIN_FILE = '.\\bin\\b_u585i_iot02a_ntz.bin'
else:
    BIN_FILE = './bin/b_u585i_iot02a_ntz.bin'

HELP = ['openDashboard.py options:', 
        '\n\t-h or --help for help',
        '\n\t-i for interactive mode',
        '\n\t--ssid=[WiFi SSID]', 
        '\n\t--password=[WiFi Password]', 
        '\n\t--version for the file version']

# Run path in command line and output it to output.txt if logging level is greater than debug
def cmd(path: list):
    proc = subprocess.Popen(path)
    proc.communicate()
    retState = proc.poll()

    if retState != 0:
        print('Error: ' + path[1])
        sys.exit(1)

################################
def getParam(curParam, label):
    param = input(label + " [" + curParam + "]: ").strip()

    if param:
        return param
    else:
        return curParam

################################
def getHiddenParam(curParam, label):
    hidden = '*' * len(curParam)
    param = getpass.getpass(prompt=label + " [" + hidden + "]: ").strip()

    if param:
        return param
    else:
        return curParam

################################
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi", ["help", "interactive", "ssid=", "password="])
    except getopt.GetoptError:
        print("Parameter Error")
        sys.exit(1)

    name = get_name()
    ssid = SSID
    pswd = PSWD
    interactiveMode = False

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(HELP)
            sys.exit(1)

        elif opt in ("--ssid"):
            ssid  = arg

        elif opt in ("--password"):
            pswd = arg

        elif opt in ("-i", "--interactive"):
            interactiveMode = True
        
        elif opt in ("--version"):
            print("STM32U5_AWS_QuickConnect.py version: " + VERSION)
            sys.exit(1)

    if interactiveMode:
        ssid = getParam(ssid, "Wi-Fi SSID")
        pswd = getHiddenParam(pswd, "Wi-Fi Password")

    
    #cmd(['python3', 'utils/flash.py', '--bin-file='+BIN_FILE])
    cmd(['python3', 'utils/setWiFiParam.py', '--ssid=' + DUMMY_SSID, '--password='+ DUMMY_PSWD])
    cmd(['python3', 'utils/provision.py', '--thing-name=' + name, '--wifi-ssid=' +  ssid, '--wifi-credential=' + pswd, '--aws-profile=' + PROVISION_AWS_PROFILE])
    cmd(['python3', 'utils/openDashboard.py', '--device-id='+ name, '--key-id='+ DASHBOARD_KEY,  '--secret-key='+ DASHBOARD_SECRET_KEY, '--bucket-url='+ DASHBOARD_URL])
    cmd(['python3', 'utils/readSerial.py'])

################################
if __name__ == "__main__":
    main(sys.argv[1:])

 #************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/           