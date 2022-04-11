#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32


def callback(msg):  # Define a function called 'callback' that receives a parameter
    print(msg.data)


# Initiate a Node called 'topic_subscriber'
rospy.init_node('topic_subscriber')
# Create a Subscriber object that will listen to the /counter
sub = rospy.Subscriber('/counter', Int32, callback)
rospy.spin()
