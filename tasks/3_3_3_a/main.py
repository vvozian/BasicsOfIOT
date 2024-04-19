#!/usr/bin/env pybricks-micropython
from umqtt.robust import MQTTClient
from pybricks.hubs import EV3Brick
import time
from pybricks.ev3devices import UltrasonicSensor, Motor
from pybricks.parameters import Port, Color, Button


client = MQTTClient('testmqtt_124567_centria', 'broker.emqx.io', 1883)
brick = EV3Brick()

message_was_handled = False
def callback(topic, msg):
    global message_was_handled
    print('Received message:', msg)
    brick.screen.print(msg.decode())
    message_was_handled = True

if __name__ == '__main__':
    client.connect()
    client.set_callback(callback)
    client.subscribe('random/ultrasonicMeasurement')

    while True:
        pressed_buttons = brick.buttons.pressed()
        if len(pressed_buttons) != 0:
            pressed_button = pressed_buttons[0]

            if pressed_button == Button.UP:
                client.publish('random/subtopic', 'up')
            elif pressed_button == Button.DOWN:
                client.publish('random/subtopic', 'down')
            elif pressed_button == Button.LEFT:
                client.publish('random/subtopic', 'left')
            elif pressed_button == Button.RIGHT:
                client.publish('random/subtopic', 'right')
            elif pressed_button == Button.CENTER:
                client.publish('random/subtopic', 'center')
            elif pressed_button == Button.BEACON:
                client.publish('random/subtopic', 'beacon')

        message_was_handled = True
        while message_was_handled == True:
            message_was_handled = False
            client.check_msg()

        time.sleep(0.5)