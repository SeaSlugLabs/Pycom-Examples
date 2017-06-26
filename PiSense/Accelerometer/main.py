from machine import I2C
from lis2hh12 import LIS2HH12 # include this library on the lib folder
import time

i2c = I2C(0, baudrate=100000, pins=('P22', 'P21'))      # Initialize the I2C bus

acc = LIS2HH12(i2c=i2c)# 

while True:
    print('----------------------------------')
    print('X, Y, Z:', acc.read())
    print('Roll:', acc.roll())
    print('Pitch:', acc.pitch())
    print('Yaw:', acc.yaw())
    time.sleep(1)
