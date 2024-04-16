#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
import time

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
color_sensor = ColorSensor(Port.S1)
button = TouchSensor(Port.S3)
brick = EV3Brick()

base_color = color_sensor.color()

history = []
counter = {
    Color.RED: 0,
    Color.GREEN: 0,
    Color.BLUE: 0,
    Color.YELLOW: 0,
    Color.BLACK: 0,
    Color.WHITE: 0,
    Color.BROWN: 0
}
previous_color = base_color

robot.drive(100, 0)
while not button.pressed():
    current_color = color_sensor.color()
    if current_color != previous_color and current_color != base_color and current_color != None:
        history.append(current_color)
        counter[current_color] += 1
        previous_color = current_color
    
    brick.screen.clear()

    text_to_print = ""
    text_to_print += "Cc: " + str(current_color) + "; "
    text_to_print += "R: " + str(counter[Color.RED]) + "; \n"
    text_to_print += "G: " + str(counter[Color.GREEN]) + "; "
    text_to_print += "Blue: " + str(counter[Color.BLUE]) + "; \n"
    text_to_print += "Y: " + str(counter[Color.YELLOW]) + "; "
    text_to_print += "Black: " + str(counter[Color.BLACK]) + "; \n"
    text_to_print += "W: " + str(counter[Color.WHITE]) + "; "
    text_to_print += "Br: " + str(counter[Color.BROWN]) + "; "

    brick.screen.draw_text(0, 0, "Cc: " + str(current_color))
    brick.screen.draw_text(0, 20, "R: " + str(counter[Color.RED]) + "; " + "G: " + str(counter[Color.GREEN]))
    brick.screen.draw_text(0, 40, "B: " + str(counter[Color.BLUE]) + "; " + "Y: " + str(counter[Color.YELLOW]))
    brick.screen.draw_text(0, 60, "Bl: " + str(counter[Color.BLACK]) + "; " + "W: " + str(counter[Color.WHITE]))
    brick.screen.draw_text(0, 80, "Br: " + str(counter[Color.BROWN]) + "; ")

    time.sleep(0.1)

robot.stop()

for color in history:
    if (color == None):
        continue
    elif color == Color.RED:
        brick.speaker.beep(100)
    elif color == Color.GREEN:
        brick.speaker.beep(200)
    elif color == Color.BLUE:
        brick.speaker.beep(300)
    elif color == Color.YELLOW:
        brick.speaker.beep(400)
    elif color == Color.BLACK:
        brick.speaker.beep(500)
    elif color == Color.WHITE:
        brick.speaker.beep(600)
    elif color == Color.BROWN:
        brick.speaker.beep(700)

    time.sleep(0.5)