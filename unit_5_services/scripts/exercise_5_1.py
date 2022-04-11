#! /usr/bin/env python

import rospy
import rospkg
from iri_wam_reproduce_trajectory.srv import ExecTraj

rospack = rospkg.RosPack()
traj_file = rospack.get_path('iri_wam_reproduce_trajectory') + \
    "/config/get_food.txt"

rospy.init_node('service_client')
rospy.wait_for_service('/execute_trajectory')
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.

exec_trajectory_srv = rospy.ServiceProxy('/execute_trajectory', ExecTraj)

print("\nExecuting service trajectory...")

result = exec_trajectory_srv(traj_file)

print(" * Executing service \"execute_trajectory\"")

print("\nPress Ctrl + C to exit")

rospy.spin()
