import time
from machine import Pin, I2C
from micropython_pca9685 import PCA9685
from micropython_pca9685 import Servo

i2c = I2C(0, sda=Pin(14), scl=Pin(12))

pca = PCA9685(i2c)
# HORNÍ SERVO doprava max 60, doleva max 160
# Střed nahoru max 155, dolu max 35
# spodek (noha) nahoru max 172, dolu max 15
pca.frequency = 50
servo = Servo(pca.channels[0])
servo1 = Servo(pca.channels[1])
servo2 = Servo(pca.channels[2])

def wave():
    global servo
    global servo1
    global servo2
    servo.angle = 75
    time.sleep(1)
    servo1.angle = 80
    time.sleep(1)
    servo2.angle = 50
    time.sleep(1)
