#!/usr/bin/env pybricks-micropython
from umqtt.robust import MQTTClient
from pybricks.hubs import EV3Brick
import time
from pybricks.ev3devices import UltrasonicSensor, Motor
from pybricks.parameters import Port, Color, Button
from pybricks.robotics import DriveBase


client = MQTTClient('testmqtt_124567_centria', 'broker.emqx.io', 1883)
brick = EV3Brick()


left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

if __name__ == '__main__':
    client.connect()

    is_clear_way_requested = False
    def callback_way_clear(topic, msg):
        global is_clear_way_requested
        if msg.decode() == 'move_away_please':
            is_clear_way_requested = True
    
    client.set_callback(callback_way_clear)
    client.subscribe('random/subtopic')

    while is_clear_way_requested != True:
        client.check_msg()
        time.sleep(0.1)
    
    robot.straight(200)

    client.publish('random/subtopic', 'clear')
