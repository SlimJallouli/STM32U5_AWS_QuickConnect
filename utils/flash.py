import serial
import os
import platform
import string
import sys
import time
import serial.tools.list_ports


#BIN File name
BIN_FILE = '.\\bin\\b_u585i_iot02a_ntz.bin'

# List of possible board labels
boards = ["DIS_U585AI"]



def flash_board(flashing_file, USBPATH):

    session_os = platform.system()

    # In Windows
    if session_os == "Windows":
        cmd = 'copy "'+flashing_file+'" "'+USBPATH+'File.bin"'
    else:
        cmd = 'cp "'+flashing_file+'" "'+USBPATH+'File.bin"'

    print(cmd)

    os.system(cmd)


def find_path(op_sys):
    USBPATH = ''
    if "windows" in op_sys.lower():
        # Find drive letter
        for l in string.ascii_uppercase:
            if os.path.exists('%s:\\MBED.HTM' % l):
                USBPATH = '%s:\\' % l
                break
        
    elif "linux" in op_sys.lower():
        user = os.getlogin()
        for board in boards:
            temp_path = '/media/%s/%s' % (user, board)
            if os.path.exists(temp_path):
                USBPATH = temp_path
                break
    elif "darwin" in op_sys.lower(): # Mac
        for board in boards:
                temp_path = '/Volumes/%s/' % board
                if os.path.exists(temp_path):
                    USBPATH = temp_path
                    break
    else:
        print("Operating System error")
        sys.exit()
    
    return USBPATH

# Finds and returns the port for the connected board.
def get_com():
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if "VID:PID=0483:374" in p.hwid:
            return p.device
    
    return " PORT ERR "



if __name__ == "__main__":
    com = get_com()
    flash_board(BIN_FILE, find_path(platform.platform()))

    time.sleep(5)

    # Wait until data comes through
    port = serial.Serial(com, 115200)
    while (port.in_waiting == 0):
        time.sleep(0.01)
    port.close()