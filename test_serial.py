import serial
import time

ser = serial.Serial(port = 'COM8', baudrate= 115200)  # open serial port
print(ser.name)         # check which port was really used
time.sleep(3)
ser.write(b'www')     # write a string
ser.write(b'sss')
ser.close() 