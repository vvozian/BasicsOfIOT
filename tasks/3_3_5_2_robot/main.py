#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
import time
from umqtt.robust import MQTTClient

client = MQTTClient('testmqtt_124567_centria', 'broker.emqx.io', 1883)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
brick = EV3Brick()
distance_sensor = UltrasonicSensor(Port.S2)
touch_sensor = TouchSensor(Port.S3)

OWN_ID = 'A1'

if __name__ == '__main__':
    client.connect()

    reach_count = 0
    robot.drive(100, 0)
    while reach_count < 10:
        if (distance_sensor.distance() < 100):
            robot.stop()
            robot.turn(100)
            robot.drive(100, 0)
            reach_count += 1
        time.sleep(0.1)
    
    robot.stop()
    brick.light.on(Color.RED)

    client.publish('random/subtopic', OWN_ID + ':stopped')


