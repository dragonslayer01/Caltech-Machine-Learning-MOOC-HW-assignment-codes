import serial
import time

# reading data from Arduino
arduino = serial.Serial("COM3", 9600)

while True:
    a = arduino.readline()
    a = str(a)
    print(a)

