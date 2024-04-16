#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port
import time

ev3 = EV3Brick()
button = TouchSensor(Port.S2)

counter = 0

timestamp = time.time()
toggle = False
print("Press the button to increase the counter")
while time.time() - timestamp < 5:
    if button.pressed() and not toggle:
        toggle = True
        counter += 1
    elif not button.pressed():
        toggle = False
    
    time.sleep(0.25)

for i in range(counter):
    ev3.speaker.beep()
    time.sleep(0.5)



