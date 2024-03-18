#!/usr/bin/env python3

import rospy
from stereo_sonar.stereoSonarCartisianSim import stereoSonar

if __name__ == "__main__":

    # init the node
    rospy.init_node("stereo_sonar_sim", log_level=rospy.INFO)

    # call the class constructor for stereo sonar
    node = stereoSonar()

    # log info and spin
    rospy.loginfo("Start orthoganal sonar fusion...")
    rospy.spin()
