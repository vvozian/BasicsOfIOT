#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
import time

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

multiplier = 1
base_speed = 2

while True:
    robot.drive(base_speed * multiplier, 0)
    time.sleep(1)
    multiplier += 1


