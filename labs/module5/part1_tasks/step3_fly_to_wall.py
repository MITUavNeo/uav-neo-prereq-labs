"""Module 5 Part 1 — Step 3: Fly to Wall
Fly forward until the depth camera reads a distance below STOP_DISTANCE.

Your task:
    Each frame:
    1. Read the depth camera center distance (convert cm → metres).
    2. If front_dist <= STOP_DISTANCE → stop, print, set _done = True.
    3. Else → drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0) to fly forward.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core, drone_utils as uav_utils
from . import step2_sensors

STOP_DISTANCE = 1.2   # metres — stop this far from the wall
FLY_SPEED     = 0.35

_done = False

def reset():
    global _done
    _done = False

def update(drone):
    global _done
    if _done: return True

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # depth_image = drone.camera.get_depth_image()
    # front_dist = min(uav_utils.get_depth_image_center_distance(depth_image) / 100,
    #                  step2_sensors.MAX_RANGE)
    # if front_dist <= STOP_DISTANCE:
    #     drone.flight.stop(); print; _done = True
    # else:
    #     drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)

    ###### END PUT CODE HERE #########
    ##################################

    return _done
