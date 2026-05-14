#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>
#include <OneWire.h>
#include <DallasTemperature.h>

// --- CONFIGURATION WIFI & MQTT ---
const char* ssid = "TDI";
const char* password = "TDII2027";
const char* mqtt_server = "broker.hivemq.com"; // Broker gratuit par défaut

WiFiClient espClient;
PubSubClient client(espClient);

// --- CONFIGURATION CAPTEURS ---
#define ONE_WIRE_BUS 4 
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);

void setup_wifi() {
  delay(10);
  Serial.print("Connexion a "); Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500); Serial.print(".");
  }
  Serial.println("\nWiFi connecte !");
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Connexion MQTT...");
    if (client.connect("ESP32_TDI_BeniMellal_2026")) {
      Serial.println("connecte");
    } else {
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  
  sensors.begin();
  if(!accel.begin()) { Serial.println("Erreur ADXL345"); while(1); }
  accel.setRange(ADXL345_RANGE_16_G);
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();

  // Lecture Vibration
  sensors_event_t event;
  accel.getEvent(&event);

  // Lecture Température
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);


  String payload = "{\"vib_x\":" + String(event.acceleration.x) + 
                   ",\"vib_y\":" + String(event.acceleration.y) + 
                   ",\"vib_z\":" + String(event.acceleration.z) + // Ajout de l'axe Z
                   ",\"temp\":" + String(tempC) + "}";

  // Publication sur le topic
  client.publish("pfa/industrial/data", payload.c_str());

  // Affichage local pour test
  Serial.println(payload);

  delay(1000); // Envoi toutes les secondes
}
