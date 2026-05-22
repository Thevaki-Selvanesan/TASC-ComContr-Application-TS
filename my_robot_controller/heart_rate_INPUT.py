#!/usr/bin/env python3
import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class HeartRateInput(Node):
    def __init__(self):
        super().__init__("heart_rate_INPUT")
        self.HRinput = self.create_publisher(Int32, "heart_rate", 10)
        self.timer_ = self.create_timer(0.5, self.timer_callback )
    
    def timer_callback(self):
        heart_rate = random.randint(0, 200)
        msg = Int32()
        msg.data = heart_rate
        self.HRinput.publish(msg)
        self.get_logger().info(str(heart_rate))

def main(args=None):
    rclpy.init(args=args) #initialize communications and features
    node = HeartRateInput()
    rclpy.spin(node) #node kept alive until shutdown
    rclpy.shutdown() #destroy node
