#!/usr/bin/env python3

from rclpy.node import Node

last_odom = None
times = 0
class Odom_subscriber(Node):

    def __init__(self):
        super().__init__('odom_subscriber')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10)
        self.subscription

    def odom_callback(self, od_data):
        global last_odom
        last_odom = od_data


if __name__ == '__main__':
    odom_subscriber = Odom_subscriber()

