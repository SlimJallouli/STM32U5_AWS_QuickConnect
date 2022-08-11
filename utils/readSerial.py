import serial
import serial.tools.list_ports
import atexit
import os

# Finds and returns the port for the connected board.
def get_com():
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if "VID:PID=0483:374" in p.hwid:
            return p.device
    
    return " PORT ERR "
            

# Indefinitely read serial communication
def serial_reader(COM):
    ser = serial.Serial(COM, 115200)

    #reading serial port indefinitely
    while 1:
        print(ser.readline().decode("utf-8", errors='ignore'), end = '')

    #closing port on script exit
    atexit.register(ser.close())


if __name__ == "__main__":
    serial_reader(get_com())



