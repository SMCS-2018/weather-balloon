#include <Wire.h>
#include <Adafruit_BNO055.h>
#include <Adafruit_Sensor.h>
#include <utility/imumaths.h>

Adafruit_BNO055 bno = Adafruit_BNO055(55);
const int currentSensorPin=0;
const int UVSensorPin=0;

void setup(){
  Serial.begin(28800);
  if (!bno.begin()) {
    Serial.println("HELP, SOMETHING HAPPENED");
  }
  pinMode(currentSensorPin,INPUT);
  pinMode(UVSensorPin,INPUT);
}
void loop() {
  Serial.print("Current:");
  Serial.println(analogRead(currentSensorPin));
  Serial.print("UV:");
  Serial.println(analogRead(UVSensorPin));
  
  // Possible vector values can be:
  // - VECTOR_ACCELEROMETER - m/s^2
  // - VECTOR_MAGNETOMETER  - uT
  // - VECTOR_GYROSCOPE     - rad/s
  // - VECTOR_EULER         - degrees
  // - VECTOR_LINEARACCEL   - m/s^2
  // - VECTOR_GRAVITY       - m/s^2
  imu::Vector<3> vec;
  vec = bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);
  Serial.println("Gyro:");
  Serial.print(vec.x());
  Serial.print(",");
  Serial.print(vec.y());
  Serial.print(",");
  Serial.print(vec.z());
  Serial.println();
  
  vec = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  Serial.println("Accel:");
  Serial.print(vec.x());
  Serial.print(",");
  Serial.print(vec.y());
  Serial.print(",");
  Serial.print(vec.z());
  Serial.println();
  
  vec = bno.getVector(Adafruit_BNO055::VECTOR_MAGNETOMETER);
  Serial.println("Magnet:");
  Serial.print(vec.x());
  Serial.print(",");
  Serial.print(vec.y());
  Serial.print(",");
  Serial.print(vec.z());
  Serial.println();
  
  vec = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
  Serial.println("Direction:");
  Serial.print(vec.x());
  Serial.print(",");
  Serial.print(vec.y());
  Serial.print(",");
  Serial.print(vec.z());
  Serial.println();
  
  
  delay(2000);
}

