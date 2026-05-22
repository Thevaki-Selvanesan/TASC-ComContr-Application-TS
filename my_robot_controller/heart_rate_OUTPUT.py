#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class HeartRateOutput(Node):
    def __init__(self):
        super().__init__("heart_rate_OUTPUT")
        self.HRoutput = self.create_subscription(Int32, "heart_rate", self.HR_callback, 10)
    
    def HR_callback(self, heart_rate: Int32):
        if heart_rate.data > 100 or heart_rate.data < 60:
            status = "danger"
        else:
            status = "normal"

        self.get_logger().info(f"Heart Rate: {heart_rate.data} | Status: {status}")

def main(args=None):
    rclpy.init(args=args) #initialize communications and features
    node = HeartRateOutput()
    rclpy.spin(node) #node kept alive until shutdown
    rclpy.shutdown() #destroy node