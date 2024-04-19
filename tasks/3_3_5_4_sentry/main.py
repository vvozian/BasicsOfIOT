#!/usr/bin/env pybricks-micropython
from umqtt.robust import MQTTClient
from pybricks.hubs import EV3Brick
import time
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port, Color, Button


client = MQTTClient('testmqtt_124567_centria', 'broker.emqx.io', 1883)
distance_sensor = UltrasonicSensor(Port.S2)

treshold = 125
OWN_ID = "A1"

if __name__ == '__main__':
    client.connect()

    last_distance = distance_sensor.distance()

    while True:
        distance = distance_sensor.distance()

        print(distance, last_distance)

        if distance < treshold and last_distance >= treshold:
            client.publish('random/presence', OWN_ID)

        last_distance = distance

        time.sleep(0.1)


