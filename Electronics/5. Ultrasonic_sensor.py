# Interfacing Ultrasonic Sensor with RPi
import RPi.GPIO as G
import time

G.setwarnings(False)
G.setmode(G.BCM)

trig = 5
echo = 27
buz = 6

G.setup(trig, G.OUT)
G.setup(buz, G.OUT)
G.setup(echo, G.IN)

def distance():
    G.output(trig, 1)
    time.sleep(0.00001)
    G.output(trig, 0)

    while G.input(echo) == 0:
        startTime = time.time()
    while G.input(echo) == 1:
        stopTime = time.time()
    
    Echo_Time = stopTime-startTime
    dist=(Echo_Time*34300)/2
    
    return dist
    
if __name__ =='__main__':
    try:
        while True:
            dist=distance()
            if dist<=10:
                G.output(buz,1)
                print('Measured Disance: ',dist,' cm')
                time.sleep(1)
            else:
                G.output(buz,0)
                print('Measured Disance: ',dist,' cm')
                time.sleep(1)
    except KeyboardInterrupt:
        G.cleanup()