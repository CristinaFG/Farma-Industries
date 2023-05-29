#!/usr/bin/env python
import serial
import mysql.connector
arduino1 = serial.Serial('/dev/ttyACM1', 9600)
arduino2 = serial.Serial('/dev/ttyACM0', 9600)
#  #1:68#2:21.50@
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
        send_mysql(sensor,value)
        i = cad.find("@")

def send_mysql(sensor_,value_):
    cnx = mysql.connector.connect(user='user', password='1234',
                              host='127.0.0.1',
                              database='Proyecto_Farma')
    cursor = cnx.cursor()
    query = "Insert into Datos (IDSENSOR,VALOR) VALUES (" + sensor_  + "," + value_ + ");"
    print(query)
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


while True:
    line1 = arduino1.readline()
    cad_proc(str(line1))
    line2 = arduino2.readline()
    cad_proc(str(line2))

arduino1.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM1', 9600)
arduino2.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM0', 9600)