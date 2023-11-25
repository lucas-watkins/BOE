from flask import Flask
import serial

try:
    app = Flask('BOE Server')
    ser = serial.Serial(port = '/dev/bus/usb/001/004', baudrate= 115200)  # open serial port

    @app.route('/<command>')
    def slash(command):
        if command != 'favicon.ico': # passes favicon.ico for some reason as an argument
            print(bytes(command, 'utf-8'))
            ser.write(bytes(command, 'utf-8'))     # write a string 
            return 'Command Completed'
        return 'no favicon'


    if __name__ == '__main__':
        app.run('0.0.0.0', port = 8080)

except KeyboardInterrupt as e:
    print('Exiting...')
    ser.close()
