import serial
import time

ser = serial.Serial(port = 'COM8', baudrate= 9600)  # open serial port
print(ser.name)         # check which port was really used
time.sleep(1)
ser.write(bytes('w', 'utf-8'))     # write a string
ser.close() 