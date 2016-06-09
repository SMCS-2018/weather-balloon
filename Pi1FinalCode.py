#!/usr/local/bin/python3

import sensor
import serial
from timeout import timeout
import time

arduino = None
while arduino == None:
    try:
        arduino = serial.Serial('/dev/tty.usbserial-AL00F0YE', 9600)
    except:
        print(arduino)
        arduino = None

arduino.timeout = 5
arduino.readline()
arduino.readline()

@timeout(2)
def getDataFromArduino(thingToSendToArduino):
    arduino.reset_input_buffer()
    arduino.reset_output_buffer()
    arduino.write(thingToSendToArduino.encode('utf-8'))
    return arduino.readline().decode('utf-8').strip()


@timeout(10)
def get9DofData():
    with open('out/gyro.csv', 'a') as gyroFile:
        lineToWrite = ""
        lineToWrite += str(time.time()) + ','
        for i in range(6):
            lineToWrite += getDataFromArduino(str(i)) + ','
        lineToWrite += getDataFromArduino('9') + ','
        lineToWrite += '\n'
        gyroFile.write(lineToWrite)
        return lineToWrite

@timeout(5)
def getOutsideData():
    with open('out/outside.csv', 'a') as gyroFile:
        lineToWrite = ""
        lineToWrite += str(time.time()) + ','
        for i in range(10, 13):
            lineToWrite += getDataFromArduino(str(i)) + ','
        lineToWrite += '\n'
        gyroFile.write(lineToWrite)
        return lineToWrite

@timeout(5)
def getCurrentData():
    with open('out/current.csv', 'a') as gyroFile:
        lineToWrite = ""
        lineToWrite += str(time.time()) + ','
        lineToWrite += getDataFromArduino('6') + ','
        lineToWrite += '\n'
        gyroFile.write(lineToWrite)
        return lineToWrite

@timeout(5)
def getUvData():
    with open('out/uv.csv', 'a') as gyroFile:
        lineToWrite = ""
        lineToWrite += str(time.time()) + ','
        lineToWrite += getDataFromArduino('7') + ','
        lineToWrite += '\n'
        gyroFile.write(lineToWrite)
        return lineToWrite

@timeout(5)
def getGeigerCounterData():
    with open('out/geiger.csv', 'a') as gyroFile:
        lineToWrite = ""
        lineToWrite += str(time.time()) + ','
        lineToWrite += getDataFromArduino('149') + ','
        lineToWrite += '\n'
        gyroFile.write(lineToWrite)
        return lineToWrite


currentTime = time.time()
nextTime = currentTime + 15


while True:
    while time.time() < nextTime:
        pass
    dof = get9DofData()
    cam.stop_recording()
    cam.capture()
    cam.start_recording()
    nextTime = time.time() + 15
