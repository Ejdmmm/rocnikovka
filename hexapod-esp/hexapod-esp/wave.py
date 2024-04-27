import time
from machine import Pin, I2C
from micropython_pca9685 import PCA9685
from micropython_pca9685 import Servo

i2c = I2C(sda=Pin(14), scl=Pin(12))
i2c_2 = I2C(sda=Pin(2), scl=Pin(4))

pca_1 = PCA9685(i2c)
pca_2 = PCA9685(i2c_2)
# HORNÍ SERVO doprava max 60, doleva max 160
# Střed nahoru max 155, dolu max 35
# spodek (noha) nahoru max 172, dolu max 15
pca_1.frequency = 50
pca_2.frequency = 50
servos_1 = []
servos_2 = []
for i in range(16):
    servos_1.append(Servo(pca_1.channels[i]))
    servos_2.append(Servo(pca_2.channels[i]))

# prava noha
def_conf_1 = [
      120, #0
      10, #1
      10, #2
       0, #3
      20, #4
     100, #5
     180, #6 predelat
       0, #7
     90, #8
      90, #9
      70, #10
       0, #11
      0, #12
      0, #13
      0, #14
       0, #15
]

def_conf_2 = [
      90, #0
      70, #1
      90, #2
       0, #3
      150, #4
       0, #5 predelat
      70, #6
       0, #7
     90, #8
      60, #9
      100, #10
       0, #11
      0, #12
      0, #13
      0, #14
       0, #15
]

def reset():
    global servos_1, servos_2
    for i, servo in enumerate(servos_1):
        servo.angle = def_conf_1[i]
    
    for i, servo in enumerate(servos_2):
        servo.angle = def_conf_2[i]
        

def wave():
    global servos_1, servos_2
    servos_1[0].angle = 180
    time.sleep(1)
    servos_1[0].angle = 120
    servos_1[1].angle = 120
    time.sleep(1)
    servos_1[1].angle = 10
    servos_1[2].angle = 50
    time.sleep(1)
    servos_1[2].angle = 90
    reset()