#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node): #initialise node
    def __init__(self): #self is a parameter
        super().__init__("first_node")
        self.create_timer(1.0, self.timer_callback) #timer created with a period of 1 second, timer callback is the function that will be called every time the timer expires

    def timer_callback(self):
        self.get_logger().info("Hello") #for writing to the terminal, info is a method of the logger class, get_logger is a method of the node class    

def main(args=None):
    rclpy.init(args=args) #initialize communications and features
    node = MyNode()

    rclpy.spin(node) #node kept alive until shutdown
    rclpy.shutdown() #destroy node

if __name__ == '__main__': 
    main()
