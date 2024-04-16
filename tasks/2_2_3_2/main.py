#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
import time

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

angle_speed = 40
direction_multiplier = 1
velocity = 100
circumference = 360 / angle_speed * velocity
robot.reset()
while True:
    robot.drive(velocity, angle_speed*direction_multiplier)
    if (robot.distance() > circumference):
        direction_multiplier = -1
        robot.reset()

