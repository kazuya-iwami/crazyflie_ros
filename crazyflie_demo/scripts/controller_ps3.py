#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy


def joyChanged(data):
    global buttons
    global twist
    global count
    axes = data.axes
    count = count + 1
    if axes[1] > 0:
        twist.linear.z = 50000*axes[1]
        if(count%10 == 0):
            print "thrust:{0}".format(twist.linear.z)
        
    else:
         twist.linear.z = 0



    twist.linear.y = -30*axes[2]
    twist.linear.x = 30*axes[3]

    # for i in range(0, len(data.buttons)):
    #     if buttons == None or data.buttons[i] != buttons[i]:
    #         if i == 13 and data.buttons[i] == 1:
    #             twist.linear.z = 12000
    #         if i == 14 and data.buttons[i] == 1:
    #             twist.linear.z = 0
    #         if i == 15 and data.buttons[i] == 1:
    #             twist.linear.z = 20000

    buttons = data.buttons

if __name__ == '__main__':
    rospy.init_node('crazyflie_demo_const_thrust', anonymous=True)
    p = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('joy', Joy, joyChanged)
    twist = Twist()
    buttons = None
    r = rospy.Rate(50)
    #for i in range(0, 100):
    #    p.publish(twist)
    #    r.sleep()

    twist.linear.z = 0
    count = 0;
    while not rospy.is_shutdown():
        p.publish(twist)
        r.sleep()
