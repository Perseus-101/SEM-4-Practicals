# Interfacing temp and humidity(DHT11) with RPi
import RPi.GPIO as G
import time
import Adafruit_DHT

S = Adafruit_DHT.DHT11
G.setwarnings(False)
G.setmode(G.BCM)
G.setup(6,G.OUT)    # Used as the output pin; for the LED

def light():        # funtion to turn on LED if h>29
    if(h>29):
        G.output(6,G.HIGH)
    else:
        G.output(6,G.LOW)

if __name__=='__main__':
    try:
        while True:  
            h, t = Adafruit_DHT.read_retry(S,5)
            if h is not None and t is not None:
                h = round(h, 2)
                t = round(t, 2)
                print('Temp = {0:0.1f}*C Humidity = {1:0.1f}%'.format(t,h))
                light()
            else:
                print('can not connect to the sensor!')
                time.sleep(1)
    except KeyboardInterrupt:
            G.cleanup()