#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button, Color, Port
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor

ev3 = EV3Brick()
CSensor = ColorSensor(Port.S1)

while True:
    if CSensor.color() == Color.RED:
        ev3.speaker.beep(100)
    elif CSensor.color() == Color.GREEN:
        ev3.speaker.beep(300)
    elif CSensor.color() == Color.BLUE:
        ev3.speaker.beep(500)
    elif CSensor.color() == Color.YELLOW:
        ev3.speaker.beep(700)