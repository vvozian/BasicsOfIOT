#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
import time

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
brick = EV3Brick()


robot.settings(150)
robot.straight(1000)
robot.stop()
time.sleep(2)
brick.speaker.beep()
robot.settings(50)
robot.straight(-1000)


