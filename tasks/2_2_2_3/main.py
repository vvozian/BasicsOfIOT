#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
import time

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

while True:
    left_motor.run(100)
    right_motor.run(100)
    time.sleep(2)
    # 90 degrees turn
    right_motor.run_target(100, -45, wait=True)
