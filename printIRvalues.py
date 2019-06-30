#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

ir=Sensor(address='in3:i2c8',driver_name='ht-nxt-ir-seek-v2')
#Set the IR mode to AC.  This helps keep the sun from messing us up
ir.mode='AC'
#set dir to the direction detected.
#5 is straight ahead.
#1-4 is to the left
#6-9 is to the right
#0 means nothing is detected
dir=ir.value()
while True:
    print ir.value()