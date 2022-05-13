# LED swiching using mobile
import RPi.GPIO as G
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)               # create and configure the app
G.setmode(G.BCM)
G.setwarnings(False)

led = 5
ledSts = 0

G.setup(led,G.OUT)
G.output(led,G.LOW)

@app.route("/")
def index():
    if G.input(led)==1:             # read the pin status
        ledSts="on"
    else:
        ledSts="on"
    templateData = {
        'title':'GPIO output Status!',
        'led':ledSts,
    }
    return render_template('new_app_index.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'led':
        actuator = led
    if action == "on":
        G.output(actuator,G.HIGH)
    if action == "off":
        G.output(actuator,G.LOW)
    if G.input(led) == 1:
        ledSts = "on"
    else:
        ledSts = "off"
    templateData = {
        'led':ledSts,
    }
    return render_template('new_app_index.html',**templateData)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)

# To run this code, connect RPi to a wifi network, note down the IP address;
# then head over to the terminal, change the directory to where this file is saved
# and type 'sudo python3 filename.py' ; then open up browser on your phone 
# or on the RPi itself and enter the IP address noted down earlier in the URL box