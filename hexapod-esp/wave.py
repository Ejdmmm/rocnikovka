import time
from machine import Pin, I2C
from micropython_pca9685 import PCA9685
from micropython_pca9685 import Servo

i2c = I2C(0, sda=Pin(14), scl=Pin(12))

pca = PCA9685(i2c)
servos = [0,1,2]
for channel in pca.channels:
    servos.append(Servo(channel))

pca.frequency = 50

def wave(servo0, servo1. servo2):
    for i in range(70):
        servo0.angle = 90
        time.sleep(1)
        servo0.angle = 180
        time.sleep(1)
        servo1.angle = 0
        time.sleep(1)
        servo1.angle = 180
        time.sleep(1)
        servo2.angle = 0
        time.sleep(1)
        servo2.angle = 120
        time.sleep(1)