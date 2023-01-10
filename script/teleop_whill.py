#!/usr/bin/python
# -*- coding: utf-8 -*-

# (Reference)[https://demura.net/robot/ros2/20748.html]

import rclpy
from rclpy.node import Node
import readchar
from sensor_msgs.msg import Joy

class TeleopPublisher(Node): 
    def __init__(self):
        super().__init__('teleop_publisher_node') 
        self.publisher = self.create_publisher(Joy,'/whill/controller/joy', 10)
        timer_period = 0.01  # second
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.vel = Joy()
        self.axes = [0] * 2
        print("*** my_teleop node ***")
        print("Input f, b, r, l  key, then press Enter key.")

    def timer_callback(self): 
        key = input("f:forward, b:backward, r:right, l:left, s:stop <<")
        print("key=", key)
        if key == 'f':
            self.vel.axes.append(0)
            self.vel.axes.append(10)
        elif key == 'b':
            self.vel.axes.append(0)
            self.vel.axes.append(-10)
        elif key == 'l':
            self.vel.axes.append(-10)
            self.vel.axes.append(0)
        elif key == 'r':
            self.vel.axes.append(10)
            self.vel.axes.append(0)
        else:
            print("Input f, b, r, l : ") 

        self.publisher.publish(self.vel) 
        self.get_logger().info("Velocity: Linear=%f angular=%f" % (self.vel.axes[1], self.vel.axes[0])) 
        self.vel = Joy()

def main(args=None):
    rclpy.init(args=args)
    teleop_publisher = TeleopPublisher() 
    rclpy.spin(teleop_publisher)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
