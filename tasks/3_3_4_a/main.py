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


if __name__ == '__main__':
    client.connect()

    robot.drive(100, 0)
    while distance_sensor.distance() > 200:
        continue

    robot.stop()

    is_way_clear = False
    def callback_way_clear(topic, msg):
        global is_way_clear
        if msg.decode() == 'clear':
            is_way_clear = True
    
    client.set_callback(callback_way_clear)
    client.subscribe('random/subtopic')

    client.publish('random/subtopic', 'move_away_please')

    while is_way_clear != True:
        client.check_msg()
        time.sleep(0.1)

    robot.drive(100, 0)

    while True:
        time.sleep(0.5)
