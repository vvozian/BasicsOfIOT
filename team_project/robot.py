from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from pybricks.robotics import DriveBase


class Robot:
    def __init__(self):
        ev3 = EV3Brick()

        left_motor = Motor(Port.B)
        right_motor = Motor(Port.C)
        self.robot_base = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
        self.light_sensor = ColorSensor(Port.S1)
        self.gyro_sensor = GyroSensor(Port.S4)
    
    def turn_left(self):
        while self.gyro_sensor.angle() < 90:
            self.robot_base.drive(0, -25)
        
    
    def turn_right(self):
        while self.gyro_sensor.angle() > 0:
            self.robot_base.drive(0, 25)

    def straight_to_next_cell(self, direction_multiplier=1):
        while self.light_sensor.reflection() < 25:
            self.robot_base.straight(10 * direction_multiplier)
        
        self.robot_base.straight(40 * direction_multiplier)
        

        adjust_distance = 75
        self.robot_base.straight(35*direction_multiplier)
        while self.light_sensor.reflection() < 25:
            self.robot_base.straight(10 * direction_multiplier)
            adjust_distance += 10
        
        self.robot_base.straight(-1 * adjust_distance * direction_multiplier * 0.5)