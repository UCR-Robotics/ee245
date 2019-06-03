#!/usr/bin/env python

import rospy
import crazyflie
import time

if __name__ == '__main__':
    rospy.init_node('takeoff_n_land')

    robot_index = 1   # for cf1
    cf = crazyflie.Crazyflie(robot_index, [0.0, 0, 0], "")

    cf.setParam("commander/enHighLevel", 1)
    cf.setParam("stabilizer/estimator", 2) # Use EKF
    cf.setParam("stabilizer/controller", 2) # Use mellinger controller
    #cf.setParam("ring/effect", 7)

    cf.takeoff(targetHeight = 1.0, duration = 3.0)
    time.sleep(3.0)

    cf.land(targetHeight = 0.0, duration = 3.0)
    time.sleep(3.0)
