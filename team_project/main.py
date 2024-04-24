#!/usr/bin/env pybricks-micropython
from OrdersQueue import OrdersQueue
from navigation import Navigation
from order import Order
from sequencer import Sequencer
from robot import Robot
from umqtt.robust import MQTTClient
import json
import time

navigator = Navigation(0, 0)
orders_queue = OrdersQueue()
client = MQTTClient('testmqtt_124567_centria', 'broker.emqx.io', 1883)
sequencer = Sequencer()
robot = Robot()

def move_to_next_cell(destination): # origin and destination are Coordinate
    global navigator
    print("destination: " + str(destination))
    delta = navigator.get_delta(destination.x, destination.y)
    print(navigator.coordinate.x, navigator.coordinate.y, destination.x, destination.y)
    print("Delta: " + str(delta))
    if delta['x'] != 0:
        if navigator.heading == 'y':
            robot.turn_right()
            navigator.set_heading_x()
        if delta['x'] > 0:
            robot.straight_to_next_cell(1)
            navigator.coordinate.x += 1
        elif delta['x'] < 0:
            robot.straight_to_next_cell(-1)
            navigator.coordinate.x -= 1
        return
    
    if delta['y'] != 0:
        if navigator.heading == 'x':
            robot.turn_left()
            navigator.set_heading_y()
        if delta['y'] > 0:
            robot.straight_to_next_cell(1)
            navigator.coordinate.y += 1
        elif delta['y'] < 0:
            robot.straight_to_next_cell(-1)
            navigator.coordinate.y -= 1
        return

handled_message = False
def on_message(topic, message):
    global client, orders_queue, handled_message
    try:
        command = str(message.decode())

        if topic == 'Centria/WarehouseOrders'.encode():
            parsed_order = json.loads(command)
            print("Received order: " + str(parsed_order))
            order = Order(
                sequencer.get_next(),
                int(parsed_order['x']),
                int(parsed_order['y'])
            )
            orders_queue.add_order(order)
    except Exception as e:
        print("Error: " + str(e))
        
    handled_message = True



def main_loop():
    global client, orders_queue, handled_message

    client.set_callback(on_message)
    client.subscribe('Centria/WarehouseOrders')
    
    while True:
        # Check for new orders
        client.check_msg()
        while handled_message:
            handled_message = False
            client.check_msg()

        # Acknowledge order (later)
        # Publish orders queue
        if(orders_queue.acknowledgement_required()):
            client.publish('Centria/WarehouseOrdersQueue', json.dumps([o.__dict__ for o in orders_queue.get_orders()]))
            orders_queue.acknwoledge_orders()

        didMove = False
        if orders_queue.get_order_count() > 0:
            order = orders_queue.look_at_next_order()
            move_to_next_cell(order)
            print(order.x, navigator.coordinate.x, order.y, navigator.coordinate.x)
            if ((order.x == navigator.coordinate.x) and (order.y == navigator.coordinate.y)):
                orders_queue.set_next_order_as_done()

        if not didMove:
            time.sleep(0.1)
        


def main():
    robot.gyro_sensor.reset_angle(0)
    client.connect()
    main_loop()

if __name__ == "__main__":
    main()