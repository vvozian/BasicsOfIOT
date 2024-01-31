#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import UltrasonicSensor
from time import sleep

ev3 = EV3Brick()
DSensor = UltrasonicSensor(Port.S4)

while True:
    reading = DSensor.distance()
    
    ev3.screen.clear()
    ev3.screen.print(reading)

    sleep(0.2)