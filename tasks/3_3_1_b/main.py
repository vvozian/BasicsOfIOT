#!/usr/bin/env pybricks-micropython
from umqtt.robust import MQTTClient
import time

client = MQTTClient('testmqtt_124567_centria', 'broker.emqx.io', 1883)


if __name__ == '__main__':
    client.connect()

    client.publish('random/subtopic', 'Hello world!')


