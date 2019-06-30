#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
cl = ColorSensor()
cl.mode='COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')

mleft = LargeMotor('outB')
mright =  LargeMotor('outC')
us = UltrasonicSensor()
us.mode='US-DIST-CM'
dist = 90

while True:
        if us.value()<dist:
                mleft.run_forever(speed_sp=-300)
                mright.run_forever(speed_sp=-300)
                sleep(.25)
                mleft.stop(stop_action="hold")
                mright.stop(stop_action="hold")

                mleft.run_forever(speed_sp=300)
                mright.run_forever(speed_sp=-300)
                sleep(.5)
                mleft.stop(stop_action="hold")
                mright.stop(stop_action="hold")

                mleft.run_forever(speed_sp=300)
                mright.run_forever(speed_sp=300)
                sleep(1.2)

                mleft.stop(stop_action="hold")
                mright.stop(stop_action="hold")
                mleft.run_forever(speed_sp=-300)
                mright.run_forever(speed_sp=300)
                sleep(.5)
                mleft.stop(stop_action="hold")
                mright.stop(stop_action="hold")

                mleft.run_forever(speed_sp=300)
                mright.run_forever(speed_sp=300)
                sleep(1.8)
                mleft.stop(stop_action="hold")
                mright.stop(stop_action="hold")

                mleft.run_forever(speed_sp=-300)
                mright.run_forever(speed_sp=300)
                sleep(.6)
                mleft.stop(stop_action="hold")
                mright.stop(stop_action="hold")

                mleft.run_forever(speed_sp=300)
                mright.run_forever(speed_sp=300)
                sleep(.9)

                mleft.run_forever(speed_sp=300)
                mright.run_forever(speed_sp=-300)
                sleep(.75)
                mleft.stop(stop_action="hold")
                mright.stop(stop_action="hold")


        else:
                if colors[cl.value()] == 'white':
                        mleft.run_forever(speed_sp=400)
                        mright.run_forever(speed_sp=-40)
                elif colors[cl.value()]=='black':
                        mright.run_forever(speed_sp=400)
                        mleft.run_forever(speed_sp=-40)