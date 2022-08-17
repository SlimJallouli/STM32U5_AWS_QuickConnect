import sys
import subprocess


NAME = 'G213801835'
SSID = 'Ziply-3970'
PSWD = 'clarycantusethis206'
KEY = 'AKIAQC3VOUARXGGMWHHO'
SECRET_KEY = '7QbU0RSsSquT9Hv3SGO9VJIBfINysxmRjadiqGsS'
DUMMY_SSID = '0'
DUMMY_PSWD = '0'

# Run path in command line and output it to output.txt if logging level is greater than debug
def cmd(path: list):
    proc = subprocess.Popen(path)
    proc.communicate()
    retState = proc.poll()

    if retState != 0:
        print('Error: ' + path[1])
        sys.exit(1)



def main():
    cmd(['python', 'utils\\flash.py'])
    cmd(['python', 'utils\\setWiFiParam.py', '--ssid=' + DUMMY_SSID, '--password='+ DUMMY_PSWD])
    cmd(['python', 'utils\\provision.py', '--thing-name=' + NAME, '--wifi-ssid=' +  SSID, '--wifi-credential=' + PSWD])
    cmd(['python', 'utils\\openDashboard.py', '--device-id='+ NAME, '--key-id='+ KEY,  '--secret-key='+ SECRET_KEY])
    cmd(['python', 'utils\\readSerial.py'])



if __name__ == "__main__":
    main()