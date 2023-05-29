// Código sensor temperatura por puerto serie

float temperatura_C = 0;
int temperatura = A0;
  
void setup()
{
  Serial.begin(9600);
  pinMode(temperatura, INPUT);
}

void loop()
{
  temperatura_C = analogRead(temperatura);
  temperatura_C = (1.1 * temperatura_C * 100.0)/1024.0;
  Serial.println("#7:"+String(temperatura_C)+"@");
  delay(3000); // Wait for 3000 millisecond(s)
}
