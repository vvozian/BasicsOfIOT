#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port, Color
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from time import sleep

ev3 = EV3Brick()
CSensor = ColorSensor(Port.S1)

while True:
    if CSensor.color() == Color.RED:
        ev3.screen.clear()
        ev3.screen.print("RED")
    elif CSensor.color() == Color.GREEN:
        ev3.screen.clear()
        ev3.screen.print("GREEN")
    elif CSensor.color() == Color.BLUE:
        ev3.screen.clear()
        ev3.screen.print("BLUE")
    elif CSensor.color() == Color.YELLOW:
        ev3.screen.clear()
        ev3.screen.print("YELLOW")
    
    sleep(0.2)