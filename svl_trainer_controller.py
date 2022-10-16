#!/usr/bin/env python
import rospy
import pygame
import cv2
import sys
import numpy as np
from sensor_msgs.msg import CompressedImage
from lgsvl_msgs.msg import VehicleControlData
from pygame.locals import *

video_size = 950, 600
velocity_publisher = rospy.Publisher('/vehicle_cmd', VehicleControlData, queue_size=10)
vel_msg = VehicleControlData()
scale_percent = 50 # percent of original size



def key_action():    
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        vel_msg.target_wheel_angle -=0.1 
    if keys[K_UP]:
        vel_msg.acceleration_pct += 0.1
        vel_msg.braking_pct += 0
    if keys[K_RIGHT]:
        vel_msg.target_wheel_angle +=0.1
    if keys[K_DOWN]:
        vel_msg.acceleration_pct -= 0.1
        vel_msg.braking_pct += 1
    if keys[K_0]:    
        vel_msg.target_gear = 0
    if keys[K_1]:    
        vel_msg.target_gear = 1
    if keys[K_2]:    
        vel_msg.target_gear = 2
    if keys[K_3]:    
        vel_msg.target_gear = 3
    if keys[K_4]:    
        vel_msg.target_gear = 4
    return vel_msg


def callback(ros_data):
    screen = pygame.display.set_mode(video_size)
    np_arr = np.frombuffer(ros_data.data, np.uint8)
    image_np = cv2.rotate(cv2.imdecode(np_arr, cv2.IMREAD_COLOR), cv2.ROTATE_90_COUNTERCLOCKWISE)
    width = int(image_np.shape[1] * scale_percent / 100)
    height = int(image_np.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.flip(cv2.resize(image_np, dim, interpolation = cv2.INTER_AREA),0)
    surf = pygame.surfarray.make_surface(resized)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    vel_msg = key_action()
    velocity_publisher.publish(vel_msg)


def main(args):
    '''Initializes and cleanup ros node'''
    rospy.init_node('svl_human_agent_client', anonymous=True)
    subscriber = rospy.Subscriber('/simulator/camera_node/image/compressed', CompressedImage, callback)
    try:
        screen = pygame.display.set_mode(video_size)        
        vel_msg = key_action()
        velocity_publisher.publish(vel_msg)
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down SVL TRAINER module")
    cv2.destroyAllWindows()
    pygame.quit()

if __name__ == '__main__':
    main(sys.argv)