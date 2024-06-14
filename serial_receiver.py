# PC (Python) code
import serial
import time
# Open a serial connection (adjust the port name and baud rate)
ser = serial.Serial("/dev/ttyACM0", 115200)
public = "1234"
try:
    while True:
        data_received = ser.readline().decode().strip()
        print(f"Received: {data_received}")
        print("\n")
        public = data_received
        nodes = data_received.split(',')
        for nodes in nodes:
            print(nodes)
except Exception as e:
    print(f"Error: {e}")
if(public == "B4,A7,G5,E7"):
    print(public)   
# Raspberry Pi Pico (Pico) code its here because yes :)
#import time
#from machine import Pin, UART

# Initialize UART on the Pico
#uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

#def send_data(data):
 #   print(data)
  #  uart.write(data.encode())

# Example: Send "Hello, PC!" repeatedly
#while True:
    #this is where you send the nodes or whatever you want make it into a loop and send it, good look :)
 #   send_data("B4,A7,G5,E7")
    #time.sleep(1)

