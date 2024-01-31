#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button, Color
from pybricks.hubs import EV3Brick
from time import sleep

ev3 = EV3Brick()

while True:
    ev3.screen.clear()
    pressed = ev3.buttons.pressed()

    if Button.UP in pressed:
        ev3.screen.print("UP")
    if Button.RIGHT in pressed:
        ev3.screen.print("RIGHT")
    if Button.DOWN in pressed:
        ev3.screen.print("DOWN")
    if Button.LEFT in pressed:
        ev3.screen.print("LEFT")
    if Button.CENTER in pressed:
        ev3.screen.print("CENTER")
    
    sleep(0.2)