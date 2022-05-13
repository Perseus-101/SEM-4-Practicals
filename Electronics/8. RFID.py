import time
import serial                   #serial library contains the access for the serial port

ser = serial.Serial(
    port='/dev/ttyUSB0',        #use 'sudo dmesg | grep tty' in terminal to find the port
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def access():                       # access() is the additional prgram teacher asked us to do,
    if data == b'5900D4EE791A':     # it prints 'Granted' or 'Denied' if the address of ID tag
        print('Access Granted!')    # In order to find the address of ID tag, run the program first
    else:                           # without the function access() and the calling fucntion in line 28
        print('Access Denied!')     # Then copy the address to the if condition of data in line 14

print('RFID Program\nPlease wave the tag')

if __name__ == '__main__':          #main program
    try:
        while True:                 #infinite loop
            data = ser.read(12)     #reads up to 12 bytes of data
            if len(data)!=0:        #returns the number of items/digits in an object
                print('RFID Tag: ', data)
                time.sleep(1)       #creating a delay of 1 second
                access()            #calling the function
    except KeyboardInterrupt:       
        ser.close()                 #closes the program when 'ctrl+c' is pressed
        print('Exiting Program')