# Raspberry Pi Pico (Pico) code
import time
from machine import Pin, UART

# Initialize UART on the Pico
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

def send_data(data):
    print(data)
    uart.write(data.encode())

# Example: Send "Hello, PC!" repeatedly
while True:
    #this is where you send the nodes or whatever you want make it into a loop and send it, good look :)
    send_data("B4,A7,G5,E7")
    #time.sleep(1)
