import RPi.GPIO as G
import time
import Adafruit_DHT
S=Adafruit_DHT.DHT11
DHTO=5
G.setmode(G.BCM)

def destroy():
    G.cleanup()
    
if __name__=='__main__':
    try:
        while True:
            hum,temp=Adafruit_DHT.read_retry(S,DHTO)
            if hum is not None and temp is not None:
                hum=round(hum,2)
                temp=round(temp,2)
                print('temp={0:0.1f}*C hum={1:0.1f}%'.format(temp,hum))
                #time.sleep(1)
            else:
                print('Retry again')
                time.sleep(1)
    except KeyboardInterrupt:
        destroy()