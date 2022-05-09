# This is the modified version of the ma'am told us to do,
# incase she doesn't require us to write this verion of the program
# just delete all the lines of code that includes GPIO 6 pin and edit the 
# print statement to just include-'LED ON' or 'LED OFF'

import RPi.GPIO as G                        #include the GPIO library
import time                                 #include the built in time library

G.setmode(G.BCM)                            #setting the mode to BCM numbering system
G.setwarnings(False)                        #supress any warnings

G.setup(5,G.OUT)                            #configuring both GPIO 5 and GPIO 6 as output port
G.setup(6,G.OUT)

while True:                                 #starting the infinite loop
    G.output(5,G.HIGH)                      #sending logic 1 to GPIO 5 to turn ON LED
    G.output(6,G.LOW)                       #sending logic 0 to GPIO 6 to turn OFF LED
    print("LED 1 is ON and LED 2 is OFF")
    time.sleep(1)                           #creating a delay of 1 second
    G.output(5,G.LOW)                       #sending logic 0 to GPIO 5 to turn OFF LED
    G.output(6,G.HIGH)                      #sending logic 1 to GPIO 6 to turn ON LED
    print("LED 1 is OFF and LED 2 is ON")
    time.sleep(1)                           #creating a delay of 1 second