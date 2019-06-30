#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep, time
sensorLight = LightSensor()
sensorLight.mode = "REFLECT"
cl = ColorSensor()
cl.mode='COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')
mleft = LargeMotor('outC')
mright =  LargeMotor('outD')
us = UltrasonicSensor()
us.mode='US-DIST-CM'
dist = 200

while 1:
	if colors[cl.value()] != 'black':
		mleft.stop(stop_action="hold")
		mright.stop(stop_action="hold")
		mleft.run_forever(speed_sp=300)
		mright.run_forever(speed_sp=300)
		sleep(1)
		mleft.run_forever(speed_sp=300)
		mright.run_forever(speed_sp=-300)
		sleep(.5)
	else:
		if us.value() >= dist:
			mleft.run_forever(speed_sp=300)
			mright.run_forever(speed_sp=-300)
		else:
			mleft.stop(stop_action="hold")
			mright.stop(stop_action="hold")
			mleft.run_forever(speed_sp=-900)
			mright.run_forever(speed_sp=-900)
			sleep(1)