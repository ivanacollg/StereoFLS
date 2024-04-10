#!/usr/bin/env python3

import rospy
from stereo_sonar.stereoSonarCartisian import stereoSonar

if __name__ == "__main__":

    # init the node
    rospy.init_node("stereo_sonar", log_level=rospy.INFO)

    # call the class constructor for stereo sonar
    node = stereoSonar()
    # log info and spin
    rospy.loginfo("Start orthoganal sonar fusion...")

    try:
        while not rospy.is_shutdown():
            node.run_stereo()
        rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting down RGB_feature_node")


