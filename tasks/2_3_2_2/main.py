#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
import time

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
brick = EV3Brick()
distance_sensor = UltrasonicSensor(Port.S2)
touch_sensor = TouchSensor(Port.S3)

while not touch_sensor.pressed():
    robot.drive(100, 0)
    if (distance_sensor.distance() < 200):
        robot.stop()
        robot.turn(100)
    time.sleep(0.1)

