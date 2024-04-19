#!/usr/bin/env pybricks-micropython
from umqtt.robust import MQTTClient
from pybricks.hubs import EV3Brick
import time
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port, Color, Button
from pybricks.hubs import EV3Brick


client = MQTTClient('testmqtt_124567_centria', 'broker.emqx.io', 1883)
distance_sensor = UltrasonicSensor(Port.S2)
brick = EV3Brick()

path_trace = []

if __name__ == '__main__':
    client.connect()

    def callback(topic, msg):
        global path_trace
        path_trace.append(msg)
    
    client.set_callback(callback)

    client.subscribe('random/presence')

    while True:
        client.check_msg()

        text = ""
        cntr = 0
        brick.screen.clear()
        for sentry_id in path_trace:
            if len(text) > 14:
                brick.screen.draw_text(0, cntr*20, text)
                cntr += 1
                text = ""
            text += sentry_id.decode() + " "

        if (len(text) > 0):
            brick.screen.draw_text(0, cntr*20, text)
        
        time.sleep(0.1)



