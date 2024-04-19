#!/usr/bin/env pybricks-micropython
from umqtt.robust import MQTTClient
from pybricks.hubs import EV3Brick
import time
from pybricks.ev3devices import UltrasonicSensor, Motor
from pybricks.parameters import Port, Color, Button
from pybricks.robotics import DriveBase


client = MQTTClient('testmqtt_124567_centria', 'broker.emqx.io', 1883)
brick = EV3Brick()
distance_sensor = UltrasonicSensor(Port.S2)


left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)


message_was_handled = False
def callback(topic, msg):
    global message_was_handled
    if msg.decode() == 'up':
        robot.drive(100, 0)
    elif msg.decode() == 'down':
        robot.drive(-100, 0)
    elif msg.decode() == 'left':
        robot.drive(0, 90)
    elif msg.decode() == 'right':
        robot.drive(0, -90)
    elif msg.decode() == 'center':
        robot.stop()

if __name__ == '__main__':
    client.connect()
    client.set_callback(callback)
    client.subscribe('random/subtopic')

    while True:
        distance = distance_sensor.distance()
        client.publish('random/ultrasonicMeasurement', str(distance))

        message_was_handled = True
        while message_was_handled == True:
            message_was_handled = False
            client.check_msg()

        time.sleep(0.5)