"""Module 5 Part 1 — Step 2: Read Distance Sensors
Use the depth camera to measure the distance to the wall in front of the drone.

The depth camera returns a 480x640 image where each pixel stores the distance (in cm)
from the drone to whatever that pixel is looking at. The utility function
uav_utils.get_depth_image_center_distance() returns the average distance at the center
of the image — i.e., the distance straight ahead.

To measure distances in other directions (left, right), you must first turn the drone
to face that direction, then read the depth camera again.

Your task:
    1. Hover: drone.flight.stop()
    2. Get the depth image: depth_image = drone.camera.get_depth_image()
    3. Read the center distance: uav_utils.get_depth_image_center_distance(depth_image)
       Clamp the reading to MAX_RANGE. Convert from cm to metres (divide by 100).
    4. Print the distance, set _done = True, return True.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core, drone_utils as uav_utils

MAX_RANGE = 10.0  # metres — clamp readings beyond this

# Exported values (read by other steps after update() returns True)
front_dist = 0.0

_done = False

def reset():
    global _done
    _done = False

def update(drone):
    global front_dist, _done
    if _done: return True

    drone.flight.stop()   # hover while reading

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # depth_image = drone.camera.get_depth_image()
    # front_dist = min(uav_utils.get_depth_image_center_distance(depth_image) / 100, MAX_RANGE)
    # print results, set _done = True

    ###### END PUT CODE HERE #########
    ##################################

    return _done
