#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button, Color
from pybricks.hubs import EV3Brick
from time import sleep

ev3 = EV3Brick()

while True:
    if Button.CENTER in ev3.buttons.pressed():
        ev3.light.on(Color.RED)
    else:
        ev3.light.on(Color.GREEN)