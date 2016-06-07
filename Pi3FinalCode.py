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

@timeout(10)
def get9DofData():
    with open('out/gyro.csv', 'a') as gyroFile:
        arduino.reset_input_buffer()
        arduino.reset_output_buffer()
        gyroFile.write(str(time.time()) + ',')
        for i in range(6):
            arduino.write(str(i).encode('utf-8'))
            gyroFile.write(arduino.readline().decode('utf-8').strip() + ',')
        arduino.write("9".encode('utf-8'))
        gyroFile.write(arduino.readline().decode('utf-8').strip() + ',')
        gyroFile.write('\n')

@timeout(5)
def getOutsideData():
    with open('out/outside.csv', 'a') as gyroFile:
        arduino.reset_input_buffer()
        arduino.reset_output_buffer()
        gyroFile.write(str(time.time()) + ',')
        for i in range(10, 13):
            arduino.write(str(i).encode('utf-8'))
            gyroFile.write(arduino.readline().decode('utf-8').strip() + ',')
        gyroFile.write('\n')

@timeout(5)
def getCurrentData():
    with open('out/current.csv', 'a') as gyroFile:
        arduino.reset_input_buffer()
        arduino.reset_output_buffer()
        gyroFile.write(str(time.time()) + ',')
        arduino.write("6".encode('utf-8'))
        gyroFile.write(arduino.readline().decode('utf-8').strip() + ',')
        gyroFile.write('\n')

@timeout(5)
def getUvData():
    with open('out/uv.csv', 'a') as gyroFile:
        arduino.reset_input_buffer()
        arduino.reset_output_buffer()
        gyroFile.write(str(time.time()) + ',')
        arduino.write("7".encode('utf-8'))
        gyroFile.write(arduino.readline().decode('utf-8').strip() + ',')
        gyroFile.write('\n')


currentTime = time.time()
nextTime = currentTime + 1
