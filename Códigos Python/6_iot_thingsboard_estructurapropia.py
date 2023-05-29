#!/usr/bin/env python
import serial
import mysql.connector
import paho.mqtt.client as mqtt
import json

arduino1 = serial.Serial('/dev/ttyACM1', 9600)
arduino2 = serial.Serial('/dev/ttyACM0', 9600)

THINGSBOARD_HOST = 'arduo.es'
ACCESS_TOKEN = 'tjvh2jq9RCFrfNnba1FA'


client = mqtt.Client()
# Set access token
client.username_pw_set(ACCESS_TOKEN)
# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()


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
        if (sensor == '1'):
            print("Sensor1")
            sensor_data = {'distancia': 0}
            sensor_data['distancia'] = value
            # Sending to ThingsBoard
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)    
        elif (sensor == '2'): 
            print("Sensor2")        
            sensor_data = {'presion': 0}
            sensor_data['presion'] = value
            # Sending to ThingsBoard
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)    
        elif (sensor == '3'): 
            print("Sensor3")        
            sensor_data = {'humedad': 0}
            sensor_data['humedad'] = value
            # Sending to ThingsBoard
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)   
        elif (sensor == '4'): 
            print("Sensor4")        
            sensor_data = {'contadorparticulas05': 0}
            sensor_data['contadorparticulas05'] = value
            # Sending to ThingsBoard
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)  
        elif (sensor == '5'): 
            print("Sensor5")        
            sensor_data = {'contadorparticulas5': 0}
            sensor_data['contadorparticulas5'] = value
            # Sending to ThingsBoard
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)  
        elif (sensor == '6'): 
            print("Sensor6")        
            sensor_data = {'peso': 0}
            sensor_data['peso'] = value
            # Sending to ThingsBoard
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)  
        elif (sensor == '7'): 
            print("Sensor7")        
            sensor_data = {'temperatura': 0}
            sensor_data['temperatura'] = value
            # Sending to ThingsBoard
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)  
        else:
            print("OTHER")

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
    line2 = arduino2.readline()
    cad_proc(str(line2))
    line1 = arduino1.readline()
    cad_proc(str(line1))
    
    
arduino1.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM1', 9600)
arduino2.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM0', 9600)
