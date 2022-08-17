import sys
import subprocess
from tokenize import Name
from utils.getDeviceName import *

SSID = 'STTestN750'
PSWD = '9a1v2r73027'
KEY = 'AKIAQC3VOUARXGGMWHHO'
SECRET_KEY = '7QbU0RSsSquT9Hv3SGO9VJIBfINysxmRjadiqGsS'
DUMMY_SSID = '0'
DUMMY_PSWD = '0'
BUCKET_URL = 'http://stm32u5-dashboard.s3-website-us-west-1.amazonaws.com'

# Run path in command line and output it to output.txt if logging level is greater than debug
def cmd(path: list):
    proc = subprocess.Popen(path)
    proc.communicate()
    retState = proc.poll()

    if retState != 0:
        print('Error: ' + path[1])
        sys.exit(1)



def main():
    
    NAME = get_name()
    
    cmd(['python', 'utils\\flash.py'])
    cmd(['python', 'utils\\setWiFiParam.py', '--ssid=' + DUMMY_SSID, '--password='+ DUMMY_PSWD])
    cmd(['python', 'utils\\provision.py', '--thing-name=' + NAME, '--wifi-ssid=' +  SSID, '--wifi-credential=' + PSWD])
    cmd(['python', 'utils\\openDashboard.py', '--device-id='+ NAME, '--key-id='+ KEY,  '--secret-key='+ SECRET_KEY, '--bucket-url='+ BUCKET_URL])
    cmd(['python', 'utils\\readSerial.py'])



if __name__ == "__main__":
    main()