#!/usr/bin/env pybricks-micropython
from umqtt.robust import MQTTClient
from pybricks.hubs import EV3Brick
import time

client = MQTTClient('testmqtt_124567_centria', 'broker.emqx.io', 1883)
brick = EV3Brick()


def on_message(topic, message):
    brick.screen.clear()
    brick.screen.print(message.decode())


if __name__ == '__main__':
    client.connect()
    client.set_callback(on_message)
    client.subscribe('random/subtopic')
    
    while True:
        client.check_msg()
        time.sleep(0.1)
