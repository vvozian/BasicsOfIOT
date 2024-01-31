#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
import time

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
light_sensor = ColorSensor(Port.S1)

seeking_turn = 0
seeking_direction = 1

while True:
    if light_sensor.color() == Color.BLACK:
        robot.drive(60, 0)
        seeking_turn = 0
    elif light_sensor.color() == Color.BLUE:
        robot.drive(30, 0)
        seeking_turn = 0
    elif light_sensor.color() == Color.RED:
        break
    else:
        robot.stop()
        
        if seeking_turn > 30 or seeking_turn < -30:
            seeking_direction *= -1
        
        seeking_turn += seeking_direction * 2

        robot.turn(seeking_direction*2)
