#!/usr/bin/env python
import serial

arduino1 = serial.Serial('/dev/ttyACM1', 9600)
arduino2 = serial.Serial('/dev/ttyACM0', 9600)
while True:
    line1 = arduino1.readline()
    print(line1)
    line2 = arduino2.readline()
    print(line2)

arduino1.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM0', 9600)
arduino2.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM0', 9600)