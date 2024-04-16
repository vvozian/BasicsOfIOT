#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port
import time

ev3 = EV3Brick()
button = TouchSensor(Port.S2)

while True:
    if button.pressed():
        ev3.speaker.beep()




