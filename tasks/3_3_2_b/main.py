#!/usr/bin/env pybricks-micropython
from umqtt.robust import MQTTClient
from pybricks.hubs import EV3Brick
import time
from pybricks.ev3devices import UltrasonicSensor, Motor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

client = MQTTClient('testmqtt_124567_centria', 'broker.emqx.io', 1883)
brick = EV3Brick()
distance_sensor = UltrasonicSensor(Port.S2)

def callback(topic, msg):
    global should_drive
    should_drive = True

should_drive = False
if __name__ == '__main__':
    client.connect()
    client.set_callback(callback)
    client.subscribe('random/subtopic')

    while should_drive != True:
        client.check_msg()
    
    while True:
        robot.drive(100, 0)

