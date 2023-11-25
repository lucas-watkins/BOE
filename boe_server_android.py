# When this script is run for the first time, it might prompt you for 
# permission. Accept the permission and run this script again, then it should 
# send the data as expected.
 
# Kivy is needed for pyjnius behind the scene.
import kivy
import click
from usb4a import usb
from usbserial4a import serial4a
from pprint import pprint
 
usb_device_list = usb.get_usb_device_list()
usb_device_name_list = [device.getDeviceName() for device in usb_device_list]
usb_device_dict = {
    device.getDeviceName():[            # Device name
        device.getVendorId(),           # Vendor ID
        device.getManufacturerName(),   # Manufacturer name
        device.getProductId(),          # Product ID
        device.getProductName()         # Product name
        ] for device in usb_device_list
    }
pprint(usb_device_dict)
 
if usb_device_list:
    global serial_port
    serial_port = serial4a.get_serial_port(
        usb_device_list[0].getDeviceName(), 
        115200,   # Baudrate
        8,      # Number of data bits(5, 6, 7 or 8)
        'N',    # Parity('N', 'E', 'O', 'M' or 'S')
        1)      # Number of stop bits(1, 1.5 or 2)
    if serial_port and serial_port.is_open:
        print(type(serial_port))
        from time import sleep
        from flask import Flask
 
        app = Flask('BOE Server')
 
        sleep(3)
        @app.route('/<command>')
        def slash(command):
            if command != 'favicon.ico':
            	serial_port.write(bytes(command,'utf-8'))
            return 'command completed'
        print("after defined route")
        #app.run('0.0.0.0', 8080)
        from gevent.pywsgi import WSGIServer
        server=WSGIServer(('0.0.0.0',8080), app)
        server.serve_forever()
        print("after run")