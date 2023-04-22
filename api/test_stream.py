import socket
import time

# # Orange Pi Pins imports
from pyA20.gpio import gpio
from pyA20.gpio import port

# #initialize the gpio module
gpio.init()

# #initialize GPIO pin
gpio.setcfg(port.PA12,gpio.INPUT)
gpio.pullup(port.PA12,gpio.PULLUP)
gpio.pullup(port.PA12,gpio.PULLDOWN)

def read_gpio():
    return gpio.input(port.PA12)


HOST = '0.0.0.0'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        try:
            value = read_gpio()
            conn.sendall(str(value).encode() + b'\n')
            time.sleep(1)
        except BrokenPipeError:
            print("Client socket closed unexpectedly.")
            conn, addr = s.accept()
            print('Connected by', addr)
