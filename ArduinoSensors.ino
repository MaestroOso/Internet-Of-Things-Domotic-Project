// Include Library
#include <DHT.h>
// Definimos el pin digital donde se conecta el sensor
#define DHTPIN 2
// Dependiendo del tipo de sensor
#define DHTTYPE DHT11
// Inicializamos el sensor DHT11
DHT dht(DHTPIN, DHTTYPE);
#include <Wire.h>

int lux = 0;
int luz = A0;
unsigned long time;
int tiempo = 5000;
int previousmillis = 0;
void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  time = millis();
  if (time - previousmillis > tiempo) {
    previousmillis = time;
    float lux = analogRead(luz) * 0.9765625;//Pasando a lux
    int  t = dht.readTemperature();
    int h = dht.readHumidity();
    Serial.println(2000);
    Serial.println(t);
    Serial.println(h);
    Serial.println(lux);
  }
}
