# This is the modifies verion of 'Interfacing switch with LED' program, here we use 
# 2 switches and 2 LEDs, this program is self-explanatory if you understood 
# the original program. No documentation would be made

import RPi.GPIO as G
import time

LED1 = 5
LED2 = 6
SW1 = 27
SW2 = 26

G.setwarnings(False)
G.setmode(G.BCM)

G.setup(LED1 , G.OUT)
G.setup(LED2 , G.OUT)
G.setup(SW1 , G.IN , pull_up_down = G.PUD_UP)
G.setup(SW2 , G.IN , pull_up_down = G.PUD_UP)

while True:
    n = G.input(SW1)
    m = G.input(SW2)
    
    if n==0:
        G.output(LED1 , G.HIGH)
        time.sleep(1)
        print('Switch 1 is pressed, LED 1 is ON')
    if m==0:    
        G.output(LED2 , G.HIGH)
        time.sleep(1)
        print('Switch 2 is pressed, LED 2 is ON')
    if n==1:
        G.output(LED1 , G.LOW)
        time.sleep(1)
        print('Switch 1 is not pressed, LED 1 is OFF')
    if m==1:   
        G.output(LED2 , G.LOW)
        time.sleep(1)
        print('Switch 2 is not pressed, LED 2 is OFF')
        
           
        