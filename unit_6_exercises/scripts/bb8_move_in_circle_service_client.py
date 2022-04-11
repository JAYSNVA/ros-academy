#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /move_bb8_in_circle to be running
rospy.wait_for_service('/move_bb8_in_circle')
# Create the connection to the service
move_bb8_in_cicle_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
# Create an object of type TrajByNameRequest
move_bb8_object = EmptyRequest()
# Send through the connection the name of the trajectory to be executed by the robot
result = move_bb8_in_cicle_service(move_bb8_object)
# Print the result given by the service called
print(result)
