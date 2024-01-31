#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button, Color
from pybricks.hubs import EV3Brick
from time import sleep

ev3 = EV3Brick()

while True:
    if Button.UP in ev3.buttons.pressed():
        ev3.speaker.beep(100)
    elif Button.RIGHT in ev3.buttons.pressed():
        ev3.speaker.beep(200)
    elif Button.DOWN in ev3.buttons.pressed():
        ev3.speaker.beep(300)
    elif Button.LEFT in ev3.buttons.pressed():
        ev3.speaker.beep(400)
    elif Button.CENTER in ev3.buttons.pressed():
        ev3.speaker.beep(500)