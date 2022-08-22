from ast import Interactive
import sys
import subprocess
from tokenize import Name
from utils.getDeviceName import *
import getopt
import getpass

SSID = 'STTestN750'
PSWD = '9a1v2r73027'
KEY = 'AKIAQC3VOUARXGGMWHHO'
SECRET_KEY = '7QbU0RSsSquT9Hv3SGO9VJIBfINysxmRjadiqGsS'
DUMMY_SSID = '0'
DUMMY_PSWD = '0'
BUCKET_URL = 'http://stm32u5-dashboard.s3-website-us-west-1.amazonaws.com'

HELP = ['openDashboard.py options:', 
        '\n\t-h or --help for help',
        '\n\t-i for interactive mode',
        '\n\t--ssid=[WiFi SSID]', 
        '\n\t--password=[WiFi Password]',
        '\n\t--device-name=[Device Name]',
        '\n\t--key=[AWS Access Key]',
        '\n\t--secret-key=[AWS Secret Key]',
        '\n\t--url=[Website URL]']

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
        opts, args = getopt.getopt(argv,"hi", ["help", "interactive", "ssid=", "password=", "name=", "device-name=", "key=", "secret-key=", "url="])
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

    
    cmd(['python', 'utils\\flash.py'])
    cmd(['python', 'utils\\setWiFiParam.py', '--ssid=' + DUMMY_SSID, '--password='+ DUMMY_PSWD])
    cmd(['python', 'utils\\provision.py', '--thing-name=' + name, '--wifi-ssid=' +  ssid, '--wifi-credential=' + pswd])
    cmd(['python', 'utils\\openDashboard.py', '--device-id='+ name, '--key-id='+ key,  '--secret-key='+ secretKey, '--bucket-url='+ url])
    cmd(['python', 'utils\\readSerial.py'])



if __name__ == "__main__":
    main(sys.argv[1:])