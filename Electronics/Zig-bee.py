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

if __name__ == "__main__":                  #main program starts
    try: 
        while True:                         #infinite loop
               trx='Hey! How you doing?'
               ser.write(str.encode(trx))   #encodes and send the information stored in 'trx' string
               rx=ser.readline().strip()    #decodes and recives the information and stores it in 'rx' string
               time.sleep(1)                #creates a dealy of 1 second
               print("Transmitted: ", trx,"| Recived : ",rx)
    except KeyboardInterrupt:
        ser.close()                         #closes the program when 'ctrl+c' is pressed
        print('Exiting Program')
