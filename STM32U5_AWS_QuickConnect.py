from ast import Interactive
import sys
import subprocess
from tokenize import Name
from utils.getDeviceName import *
import getopt
import getpass
import platform

SSID = 'st_iot_demo'
PSWD = 'stm32u585'
KEY = 'AKIAQC3VOUARXGGMWHHO'
SECRET_KEY = '7QbU0RSsSquT9Hv3SGO9VJIBfINysxmRjadiqGsS'
DUMMY_SSID = '0'
DUMMY_PSWD = '0'
BUCKET_URL = 'https://main.d3mkj47qkab3qo.amplifyapp.com'

if platform.system() == 'Windows': 
    BIN_FILE = '.\\bin\\b_u585i_iot02a_ntz.bin'
else:
    BIN_FILE = './bin/b_u585i_iot02a_ntz.bin'


HELP = ['openDashboard.py options:', 
        '\n\t-h or --help for help',
        '\n\t-i for interactive mode',
        '\n\t--ssid=[WiFi SSID]', 
        '\n\t--password=[WiFi Password]',
        '\n\t--aws-region=[AWS_REGION]',
        '\n\t--aws-access-key-id=[AWS Access Key]',
        '\n\t--aws-access-key-secret=[AWS Secret Key]']

# Run path in command line and output it to output.txt if logging level is greater than debug
def cmd(path: list):
    proc = subprocess.Popen(path)
    proc.communicate()
    retState = proc.poll()

    if retState != 0:
        print('Error: ' + path[1])
        sys.exit(1)


def getParam(curParam, label):
    param = input(label + " [" + curParam + "]: ").strip()

    if param:
        return param
    else:
        return curParam

def getHiddenParam(curParam, label):
    hidden = '*' * len(curParam)
    param = getpass.getpass(prompt=label + " [" + hidden + "]: ").strip()

    if param:
        return param
    else:
        return curParam


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi", ["help", "interactive", "ssid=", "password=", "key=", "secret-key="])
    except getopt.GetoptError:
        print("Parameter Error")
        sys.exit(1)

    name = get_name()
    ssid = SSID
    pswd = PSWD
    key = KEY
    secretKey = SECRET_KEY
    url = BUCKET_URL
    interactiveMode = False


    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(*HELP)
            sys.exit(1)

        elif opt in ("--ssid"):
            ssid  = arg

        elif opt in ("--password"):
            pswd = arg

        elif opt in ("--key"):
            key = arg

        elif opt in ("--secret-key"):
            secretKey = arg

        elif opt in ("--url"):
            url = arg

        elif opt in ("--device-name"):
            name = arg

        elif opt in ("-i", "--interactive"):
            interactiveMode = True



    if interactiveMode:
        ssid = getParam(ssid, "Wi-Fi SSID")
        pswd = getHiddenParam(pswd, "Wi-Fi Password")

    
    cmd(['python3', 'utils/flash.py', '--bin-file='+BIN_FILE])
    cmd(['python', 'utils\\setWiFiParam.py', '--ssid=' + DUMMY_SSID, '--password='+ DUMMY_PSWD])
    cmd(['python', 'utils\\provision.py', '--thing-name=' + name, '--wifi-ssid=' +  ssid, '--wifi-credential=' + pswd])
    cmd(['python', 'utils\\openDashboard.py', '--device-id='+ name, '--key-id='+ key,  '--secret-key='+ secretKey, '--bucket-url='+ url])
    cmd(['python', 'utils\\readSerial.py'])



if __name__ == "__main__":
    main(sys.argv[1:])