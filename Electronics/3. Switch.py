# Switch interfacing with RPi
import RPi.GPIO as G
import time

LED = 5                                         # assigning variable 'LED' the value 5
SW = 27                                         # assigning variable 'SW' the value 27

G.setwarnings(False)
G.setmode(G.BCM)

G.setup(LED , G.OUT)                            # congiure GPIO 5 as output port and send logic level to LED
G.setup(SW , G.IN , pull_up_down = G.PUD_UP)    # configure GPIO 27 as input port for switch

while True:
    n = G.input(SW)                             # storing the logic level in 'n' from switch
    if n==0:                                    # cheking if logic level is 0
        G.output(LED , G.HIGH)                  # sending logic level 1 to LED to turn it ON
        time.sleep(1)                           # creating a delay of 1 second
        print('Switch pressed, LED ON')
    elif n==1:                                  # checking if logic level is 1
        G.output(LED , G.LOW)                   # sending logic level 0 to LED to turn it off
        time.sleep(1)                           # creating a delay of 1 second
        print('Switch not pressed, LED OFF')