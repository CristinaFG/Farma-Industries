#!/usr/bin/env python
import serial
import mysql.connector
arduino = serial.Serial('/dev/ttyACM0', 9600)
#  {"1":12,"2":24.9375} 
def cad_proc(cad):
    print ("\n\nInicio------------------------------------------------>" + cad)
    i = cad.find("}")
    j = cad.find("{")

    if ((i<0)or(j<0)):
       return

    while (i > 0):
        #Elimino primer {
        j = cad.find("{")
        if (j<0):
            j = cad.find(",")
        cad = cad [j+1:]
        aux = cad

        #Cad avanza 1 bloque y aux se queda con el bloque anterior
        j = cad.find(",")
        if (j < 0):
            j = cad.find("}") #Si entro en este condicional he llegado a ultimo bloque
        aux = aux[:j]
        cad = cad[j:]
        print("future:" + cad)
        #Divido aux en ID y valor
        x = aux.find(":")
        sensor = aux[:x]
        value = aux[x+1:]


        sensor = sensor.replace('"', '')
        value = value.replace('"', '')

        #info print
        print("sensor:" + sensor)
        print("value:" + value)
        send_mysql(sensor,value)
        i = cad.find("}")

def send_mysql(sensor_,value_):
    cnx = mysql.connector.connect(user='user', password='1234',
                              host='127.0.0.1',
                              database='iot')
    cursor = cnx.cursor()
    query = "Insert into data (idsensor,value) VALUES (" + sensor_  + "," + value_ + ");"
    print(query)
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


while True:
    line = arduino.readline()
    cad_proc(str(line))
arduino.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM0', 9600)
