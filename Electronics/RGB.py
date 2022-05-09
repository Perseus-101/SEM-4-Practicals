import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
g=5
r=6
b=12
GPIO.setup(g,GPIO.OUT)
GPIO.setup(r,GPIO.OUT)
GPIO.setup(b,GPIO.OUT)
freq=100
G=GPIO.PWM(g,freq)
R=GPIO.PWM(r,freq)
B=GPIO.PWM(b,freq)
if __name__=='__main__':
    try:
        while True:
            for x in range(0,101):
                G.ChangeDutyCycle(x)
                time.sleep(0.05)
            for x in range(100,0):
                G.ChangeDutyCycle(100-x)
                time.sleep(0.05)   
            for x in range(0,101):
                R.ChangeDutyCycle(x)
                time.sleep(0.05)
            for x in range(100,0):
                R.ChangeDutyCycle(100-x)
                time.sleep(0.05)
            for x in range(0,101):
                B.ChangeDutyCycle(x)
                time.sleep(0.05)
            for x in range(100,0):
                B.ChangeDutyCycle(100-x)
                time.sleep(0.05)
    except KeyboardInterrupt:
           GPIO.cleanup()
