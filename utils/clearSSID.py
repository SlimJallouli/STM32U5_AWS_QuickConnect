import serial, serial.tools.list_ports
import time


def get_com():
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if "VID:PID=0483:374" in p.hwid:
            return p.device
    
    return " PORT ERR "


def clear_ssid(com):
    ser = serial.Serial(com, 115200)

    ser.write(bytes('conf set wifi_ssid\r\n', 'utf-8'))
    time.sleep(2)
    ser.write(bytes('conf commit\r\n', 'utf-8'))
    time.sleep(2)
    ser.write(bytes('reset\r\n', 'utf-8'))
    time.sleep(1)

    ser.close()
    




def main():
    clear_ssid(get_com())


if __name__ == "__main__":
    main()