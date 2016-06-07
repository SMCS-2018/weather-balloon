#include <Adafruit_BME280.h>

#include <Wire.h>
#include <Adafruit_BNO055.h>
#include <Adafruit_Sensor.h>
#include <utility/imumaths.h>

Adafruit_BNO055 bno = Adafruit_BNO055(55);
Adafruit_BME280 bme; // I2C

const int CURRENT_SENSOR_PIN = 0;
const int UV_SENSOR_PIN = 0;
const int DUST_SENSOR_PIN = A0;
const int DUST_SENSOR_LED = 11;

const int GYRO = 0;
const int ACCEL = 1;
const int MAGNET = 2;
const int EULERVEC = 3;
const int LINACCEL = 4;
const int GRAVITY = 5;
const int CURRENT = 6;
const int UV = 7;
const int DUST = 8;
const int TEMP = 9;
const int OUTTEMP = 10;
const int OUTHUM = 11;
const int OUTPRESS = 12;


int whatToSend;
bool bnoFound = true;
bool bmeFound = true;

int samplingTime = 280;
int deltaTime = 40;
int sleepTime = 9680;

int voMeasured = 0;
float calcVoltage = 0;
float dustDensity = 0;


void setup(){
    Serial.begin(57600);
    if (!bno.begin()) {
        Serial.println("No 9DOF found.");
        bnoFound = false;
    }
    if(!bme.begin()) {
        Serial.println("Could not find a valid BME280 sensor, check wiring!");
        bmeFound = false;
    }
    pinMode(DUST_SENSOR_LED, OUTPUT);
    pinMode(CURRENT_SENSOR_PIN, INPUT);
    pinMode(UV_SENSOR_PIN, INPUT);
}

void writeVector(imu::Vector<3> vec) {
    Serial.print(vec.x());
    Serial.print(" ");
    Serial.print(vec.y());
    Serial.print(" ");
    Serial.print(vec.z());
    Serial.println();
}

void writeAnalogPin(int pin) {
    Serial.println(analogRead(pin));
}

void loop() {
    while(Serial.available() == 0);
    whatToSend = Serial.parseInt();
    switch(whatToSend) {
        case GYRO:
            if(bnoFound) {
                writeVector(bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE));
            } else {
                Serial.println("GYRO NOT FOUND");
            }
            break;
        case ACCEL:
            if(bnoFound) {
                writeVector(bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER));
            } else {
                Serial.println("ACCEL NOT FOUND");
            }
            break;
        case MAGNET:
            if(bnoFound) {
                writeVector(bno.getVector(Adafruit_BNO055::VECTOR_MAGNETOMETER));
            } else {
                Serial.println("MAGNET NOT FOUND");
            }
            break;
        case EULERVEC:
            if(bnoFound) {
                writeVector(bno.getVector(Adafruit_BNO055::VECTOR_EULER));
            } else {
                Serial.println("EULERVEC NOT FOUND");
            }
            break;
        case LINACCEL:
            if(bnoFound) {
                writeVector(bno.getVector(Adafruit_BNO055::VECTOR_LINEARACCEL));
            } else {
                Serial.println("LINACCEL NOT FOUND");
            }
            break;
        case GRAVITY:
            if(bnoFound) {
                writeVector(bno.getVector(Adafruit_BNO055::VECTOR_GRAVITY));
            } else {
                Serial.println("GRAVITY NOT FOUND");
            }
            break;
        case TEMP:
            if(bnoFound) {
                Serial.println(bno.getTemp());
            } else {
                Serial.println("TEMP NOT FOUND");
            }
            break;
        case CURRENT:
            writeAnalogPin(CURRENT_SENSOR_PIN);
            break;
        case UV:
            writeAnalogPin(UV_SENSOR_PIN);
            break;
        case DUST:
            digitalWrite(DUST_SENSOR_LED, LOW); // power on the LED
            delayMicroseconds(samplingTime);
            voMeasured = analogRead(DUST_SENSOR_PIN); // read the dust value
            delayMicroseconds(deltaTime);
            digitalWrite(DUST_SENSOR_LED, HIGH); // turn the LED off
            Serial.println(voMeasured);
            break;
        case OUTTEMP:
            if(bmeFound) {
                Serial.println(bme.readTemperature());
            } else {
                Serial.println("NO TEMP FOUND");
            }
            break;
        case OUTPRESS:
            if(bmeFound) {
                Serial.println(bme.readPressure());
            } else {
                Serial.println("NO PRESSURE FOUND");
            }
            break;
        case OUTHUM:
            if(bmeFound) {
                Serial.println(bme.readHumidity());
            } else {
                Serial.println("NO HUMIDITY FOUND");
            }
            break;
        default:
            if(bmeFound) {
                Serial.println("INVALID");
            } else {
                Serial.println();
            }
            break;
    }
}
