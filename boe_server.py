from flask import Flask
import serial

app = Flask('BOE Server')

@app.route('/<command>')
def w(command):
    ser = serial.Serial(port = 'USB-SERIAL CH340', baudrate= 9600)  # open serial port
    print(ser.name)         # check which port was really used
    ser.write(bytes(command))     # write a string
    ser.close() 
    return 'Command Completed'


if __name__ == '__main__':
    app.run('0.0.0.0', port = 8080)
    