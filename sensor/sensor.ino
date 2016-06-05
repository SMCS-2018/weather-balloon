#include <Wire.h>
#include <Adafruit_BNO055.h>
#include <Adafruit_Sensor.h>
#include <utility/imumaths.h>

Adafruit_BNO055 bno = Adafruit_BNO055(55);
const int CURRENT_SENSOR_PIN = 0;
const int UV_SENSOR_PIN = 0;
const int DUST_SENSOR_PIN = 0;

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


int whatToSend;
bool bnoFound = true;

void setup(){
    Serial.begin(28800);
    if (!bno.begin()) {
        Serial.println("HELP, SOMETHING HAPPENED");
        bnoFound = false;
    }
    pinMode(CURRENT_SENSOR_PIN, INPUT);
    pinMode(UV_SENSOR_PIN, INPUT);
}

void writeVector(imu::Vector<3> vec) {
    Serial.print(vec.x());
    Serial.print(",");
    Serial.print(vec.y());
    Serial.print(",");
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
                Serial.println("BNO055 NOT FOUND");
            }
            break;
        case ACCEL:
            if(bnoFound) {
                writeVector(bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER));
            } else {
                Serial.println("BNO055 NOT FOUND");
            }
            break;
        case MAGNET:
            if(bnoFound) {
                writeVector(bno.getVector(Adafruit_BNO055::VECTOR_MAGNETOMETER));
            } else {
                Serial.println("BNO055 NOT FOUND");
            }
            break;
        case EULERVEC:
            if(bnoFound) {
                writeVector(bno.getVector(Adafruit_BNO055::VECTOR_EULER));
            } else {
                Serial.println("BNO055 NOT FOUND");
            }
            break;
        case LINACCEL:
            if(bnoFound) {
                writeVector(bno.getVector(Adafruit_BNO055::VECTOR_LINEARACCEL));
            } else {
                Serial.println("BNO055 NOT FOUND");
            }
            break;
        case GRAVITY:
            if(bnoFound) {
                writeVector(bno.getVector(Adafruit_BNO055::VECTOR_GRAVITY));
            } else {
                Serial.println("BNO055 NOT FOUND");
            }
            break;
        case TEMP:
            if(bnoFound) {
                Serial.println(bno.getTemp());
            } else {
                Serial.println("BNO055 NOT FOUND");
            }
            break;
        case CURRENT:
            writeAnalogPin(CURRENT_SENSOR_PIN);
            break;
        case UV:
            writeAnalogPin(UV_SENSOR_PIN);
            break;
        case DUST:
            writeAnalogPin(DUST_SENSOR_PIN);
            break;
        default:
            Serial.println("INVALID");
            break;
    }
}
