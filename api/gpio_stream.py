from flask import Flask, Response

# Orange Pi Pins imports
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep

#initialize the gpio module
gpio.init()

#initialize GPIO pin
gpio.setcfg(port.PA12,gpio.INPUT)
gpio.pullup(port.PA12,gpio.PULLUP)
gpio.pullup(port.PA12,gpio.PULLDOWN)

def read_gpio():
    return gpio.input(port.PA12)


app = Flask(__name__)

@app.route('/stream')
def stream():
    def generate():
        while True:
            yield str(read_gpio())

    return Response(generate(), mimetype='text/plain')

@app.route('/')
def index():
    return '<h1>App deployed</h1>'
