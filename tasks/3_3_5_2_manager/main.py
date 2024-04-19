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

if __name__ == '__main__':
    client.connect()

    def callback(topic, msg):
        data = msg.decode().split(':')
        if (len(data) != 2):
            return
        if data[1] == 'stopped':
            robot.stop()
            brick.speaker.beep()
            brick.screen.print('robot ' + data[0] + ' needs an inspection.')
        
    client.set_callback(callback)
    client.subscribe('random/subtopic')

    while True:
        client.check_msg()
        time.sleep(0.1)


