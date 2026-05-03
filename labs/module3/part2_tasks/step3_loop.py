"""
Module 3 Part 2 — Step 3: Maze Loop
Continuously scan for ArUco markers and call the action handler.

Your task:
    Each frame:
    1. Get the camera image: image = drone.camera.get_color_image()
    2. Detect ArUco markers: markers = uav_utils.get_ar_markers(image, ARUCO_DICT)
    3. Get the first detected marker's ID (or None if no markers).
    4. If the detected_id is DIFFERENT from _last_id (a new marker appeared):
           _last_id = detected_id
           step2_action.trigger(drone, detected_id)
    5. Call step2_action.update(drone) every frame to execute the current action.
    6. If step2_action.update() returns True → set _done = True.

Returns True when the maze end (ID=2) is reached.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))

import drone_core
import drone_utils as uav_utils
from . import step2_action

# ArUco dictionary used in the scene (must match what was baked into the textures)
import cv2
ARUCO_DICT = cv2.aruco.DICT_6X6_250

_last_id     = None   # most recently triggered marker ID
_done        = False

def reset():
    global _last_id, _done
    _last_id = None; _done = False
    step2_action.reset()

def update(drone):
    """
    Detect ArUco markers from the camera image.
    When a new marker appears, pass its ID to step2_action.trigger().
    Returns True when the maze end (ID=2) is reached.
    """
    global _last_id, _done
    if _done:
        return True

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Step 1: image   = drone.camera.get_color_image()
    # Step 2: markers = uav_utils.get_ar_markers(image, ARUCO_DICT)
    # Step 3: detected_id = markers[0].get_id() if markers else None
    # Step 4: if detected_id != _last_id:
    #             _last_id = detected_id
    #             step2_action.trigger(drone, detected_id)
    # Step 5: maze_done = step2_action.update(drone)
    #         if maze_done: _done = True

    ###### END PUT CODE HERE #########
    ##################################

    return _done
