#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class DrawCircle(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.cmv_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10) #publisher created, Twist is the message type, /turtle1/cmd_vel is the topic name, 10 is the queue size 
        self.timer_ = self.create_timer(0.5, self.send_velocity_command) #timer created with a period of 0.5 seconds, timer callback is the function that will be called every time the timer expires   
        self.get_logger().info("draw circle mode has been started")
    
    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmv_vel_pub_.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node = DrawCircle()
    rclpy.spin(node)
    rclpy.shutdown()
