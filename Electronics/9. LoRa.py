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
  
if __name__ == "__main__":      #main program starts
    try:
        while True:             #infinite loop
            trx=ser.write(str.encode('Hey guys!'))  #encodes and send the information stored in 'trx' string
            time.sleep(1)                           #creating a delay of 1 second
            rx=ser.readline().strip()               #decodes and recives the information and stores it in 'rx' string
            print("Transmitted: ", trx,"| Recived : ",rx)
            time.sleep(1)                           #creating a delay of 1 second
    except KeyboardInterrupt:
        ser.close()
        print ('Exiting Program')

