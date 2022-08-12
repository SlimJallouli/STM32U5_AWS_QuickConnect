import serial, serial.tools.list_ports
import time
import getopt, sys


HELP = ['openDashboard.py options:', 
        '\n\t-h or --help for help',
        '\n\t--ssid=[WiFi SSID]', 
        '\n\t--password=[WiFi Password]']

def get_com():
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if "VID:PID=0483:374" in p.hwid:
            return p.device
    
    return " PORT ERR "


def set_param(com, key, value):
    ser = serial.Serial(com, 115200)

    ser.write(bytes('conf set ' + key + ' ' + value + '\r\n', 'utf-8'))
    print('conf set ' + key + ' ' + value + '\r\n')
    time.sleep(2)
    ser.write(bytes('conf commit\r\n', 'utf-8'))
    time.sleep(2)
    ser.write(bytes('reset\r\n', 'utf-8'))
    time.sleep(3)

    ser.close()
    




def main(argv):

    com = get_com()

    try:
        opts, args = getopt.getopt(argv,"h", ["help", "ssid=", "password="])
    except getopt.GetoptError:
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(*HELP)
            sys.exit()

        elif opt in ("--ssid"):
            set_param(com, 'wifi_ssid', arg)

        elif opt in ("--password"):
            set_param(com, 'wifi_credential', arg)



if __name__ == "__main__":
    main(sys.argv[1:])