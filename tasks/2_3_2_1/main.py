#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
import time

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
brick = EV3Brick()
distance_sensor = UltrasonicSensor(Port.S2)

while distance_sensor.distance() > 200:
    robot.drive(100, 0)
    time.sleep(0.1)

