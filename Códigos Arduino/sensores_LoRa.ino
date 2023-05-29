// Código sensor distancia y presión

float distancia_cm = 0; 
int echoPin = 7;
int triggerPin = 6;
float presion_Pa;
float peso_g;
float humedad_minima = 20;
float humedad_maxima = 40;
float presion_minima = 53;
float presion_maxima = 80;
float humedad_anterior;
float humedad;
float presion_anterior;
float presion;
float suma_humedad;
float suma_presion;
int particulas_05;
int particulas_5;
int peso;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
} 
  
void setup()
{
  Serial.begin(9600);
  humedad = 30;
  humedad_anterior = 25;
  presion = 60;
  presion_anterior = 75;
  delay(101);
}

void loop()
{
  // Sensor distancia
  distancia_cm = 0.01723 * readUltrasonicDistance(triggerPin,echoPin);
  
  // Sensor presión
  suma_presion = random(0,9)/100.0;
  presion_anterior = presion;
  if (presion_minima < presion && presion < presion_maxima)
  {
    int operacion_presion = random(0, 2);  // Generar un número aleatorio entre 0 y 1
    if (operacion_presion == 0) 
    {
      presion = presion - suma_presion;  // Restar el valor generado
    }
    else
    {
      presion = presion + suma_presion;  // Sumar el valor generado
    }
  }
  else 
  {
    if (presion_minima > presion)
    {
      presion = presion + suma_presion;  // Sumar el valor generado
    }
    if (presion > presion_maxima)
    {
      presion = presion - suma_presion;  // Sumar el valor generado
    }
   }
  
  // Sensor humedad
  suma_humedad = random(0,9)/100.0;
  humedad_anterior = humedad;
  if (humedad_minima < humedad && humedad < humedad_maxima)
  {
    int operacion_humedad = random(0, 2);  // Generar un número aleatorio entre 0 y 1
    if (operacion_humedad == 0) 
    {
      humedad = humedad - suma_humedad;  // Restar el valor generado
    }
    else
    {
      humedad = humedad + suma_humedad;  // Sumar el valor generado
    }
  }
  else 
  {
    if (humedad_minima > humedad)
    {
      humedad = humedad + suma_humedad;  // Sumar el valor generado
    }
    if (humedad > humedad_maxima)
    {
      humedad = humedad - suma_humedad;  // Sumar el valor generado
    }
   }

  // Sensor peso
  peso = random(145,155);

  // Sensor contador de particulas de 0,5 micrometros por metro cúbico (Grado A y B)
  particulas_05 = random(351600,353000);
  
  // Sensor contador de particulas de 5 micrometros por metro cúbico (Grado A y B)
  particulas_5 = random(2700,3000);
  Serial.println("#1:"+String(distancia_cm)+"#2:"+String(presion)+"#3:"+String(humedad)+"#4:"+String(particulas_05)+"#5:"+String(particulas_5)+"#6:"+String(peso)+"@");
  delay(3000); // Wait for 3000 millisecond(s)
}
