#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button, Color, Port
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import UltrasonicSensor

ev3 = EV3Brick()
DSensor = UltrasonicSensor(Port.S4)

ev3.speaker.set_volume(5)

while True:
    reading = DSensor.distance()
    
    ev3.speaker.beep(reading)