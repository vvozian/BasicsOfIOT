#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
import time

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
button = TouchSensor(Port.S2)
multiplier = 1
base_speed = 2
flag = False

while True:
    if flag:
        robot.drive(base_speed * multiplier, 0)
        time.sleep(1)
        multiplier += 1
    elif button.pressed():
        flag = True



