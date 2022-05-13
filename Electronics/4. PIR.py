# Motion Detection(PIR) with RPi
import RPi.GPIO as G
import time

G.setwarnings(False)
G.setmode(G.BCM)

G.setup(5, G.IN)                    # configure GPIO 5 as the input port
G.setup(27,G.OUT)                   # configure GPIO 27 as the output port

num = 0                             # here starts the extra bit code ma'am asked, 
count = 0                           # if in the exams, ma'am doesn't ask you can 
def intrudercount():                # delete this block of code and call function 
    num+=1                          # on line 27, intrudercount() which counts how 
    if num%10==0:                   # many intruders have passed through
        count+=1

while True:
    i = G.input(5)                  # storing the logic from PIR into variable 'i'
    if i == 0:                      # checking if the logic level is 0
        print("No intruder")
        G.output(27, 0)             # sending logic 0 to buzzer
        time.sleep(0.1)             # creating a delay of .1 second
    elif i==1:                      # checking if the logic level is 1
        print("Intruder Detected!")
        G.output(27, 1)             # sending logic 1 to buzzer
        time.sleep(0.1)             # creating a delay of .1 second
        intrudercount()             # calling the function
    print("Intruder count: ",count)