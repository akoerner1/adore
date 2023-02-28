#!/usr/bin/env python3
# ********************************************************************************
# * Copyright (C) 2017-2020 German Aerospace Center (DLR). 
# * Eclipse ADORe, Automated Driving Open Research https://eclipse.org/adore
# *
# * This program and the accompanying materials are made available under the 
# * terms of the Eclipse Public License 2.0 which is available at
# * http://www.eclipse.org/legal/epl-2.0.
# *
# * SPDX-License-Identifier: EPL-2.0 
# *
# * Contributors: 
# *	  Thomas Lobig
# ********************************************************************************

import rospy

from std_msgs.msg import Bool


def callback_sample(msg):
	print(msg.data)

    
def signal_publish():
	# if condition?:
	pub.publish(False)
	# False does nothing, unless you wanted to start already stopped automation
	# True will make it so the tactical planner stops sending trajectories to the feedback loop controller
	

if __name__ == '__main__':
	pub = rospy.Publisher('/vehicle0/FUN/HaltAutomation', Bool, queue_size=1)
	rospy.init_node('ecu_emergency_stop_node')
	

	# run loop:
	r = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		signal_publish()
		r.sleep()

	# alternatively use ros.spin() to wait until shutdown, if you don't need a run loop
