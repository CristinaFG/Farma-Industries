#!/usr/bin/env python
import serial
arduino1 = serial.Serial('/dev/ttyACM1', 9600)
arduino2 = serial.Serial('/dev/ttyACM0', 9600)

def cad_proc(cad):
    print ("\n\nInicio------------------------------------------------>" + cad)
    i = cad.find("@")
    while (i > 0):
        #Elimino primer #
        j = cad.find("#")
        cad = cad [j+1:]
        aux = cad

        #Cad avanza 1 bloque y aux se queda con el bloque anterior
        j = cad.find("#")
        if (j < 0):
            j = cad.find("@") #Si entro en este condicional he llegado a ultimo bloque
        aux = aux[:j]
        cad = cad[j:]

        #Divido aux en ID y valor
        x = aux.find(":")
        sensor = aux[:x]
        value = aux[x+1:]

        #info print
        print("sensor:" + sensor)
        print("value:" + value)
        #send_mysql(sensor,value)
        i = cad.find("@")

while True:
    line1 = arduino1.readline()
    cad_proc(str(line1))
    line2 = arduino2.readline()
    cad_proc(str(line2))

arduino1.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM1', 9600)
arduino2.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM0', 9600)