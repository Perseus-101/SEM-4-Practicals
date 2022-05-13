# Zig-bee with RPi
import time
import serial               # serial library contains the access for the serial port

ser = serial.Serial(
    port='/dev/ttyUSB0',    # use 'sudo dmesg | grep tty' in terminal to find the port
    baudrate = 9600,                 
    parity=serial.PARITY_NONE,      
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1             
)

if __name__ == "__main__":                  # main program starts
    try: 
        while True:                         # infinite loop
               trx='Hey! How you doing?'
               ser.write(str.encode(trx))   
               rx=ser.readline().strip()             
               time.sleep(1)                
               print("Transmitted: ", trx,"| Recived : ",rx)
    except KeyboardInterrupt:
        ser.close()                # closes the program when 'ctrl+c' is pressed
        print('Exiting Program')
