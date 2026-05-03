"""
Module 3 Part 1 — Step 2: Find Object
Scan with the camera to detect the target colored object.

Target: RED object (OpenCV HSV hue wraps: red lives in 0-10 AND 170-180).

Your task:
    1. Hover in place (drone.flight.stop()).
    2. Get the camera image: image = drone.camera.get_color_image()
    3. Find contours in both red hue ranges (TARGET_LOWER/UPPER and TARGET_LOWER2/UPPER2).
    4. Find the largest contour with uav_utils.get_largest_contour(..., MIN_AREA).
    5. If found: get centroid with uav_utils.get_contour_center(contour),
       store in target_cx / target_cy, print, set _done = True.

Returns True when the target is found.
"""

import sys, os
import numpy as np
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))

import drone_core
import drone_utils as uav_utils

# ── Target colour (HSV) ────────────────────────────────────────────────────────────
# Hue: 0–10 and 170–180 covers red in OpenCV HSV
TARGET_LOWER  = np.array([  0, 120,  80], dtype=np.uint8)
TARGET_UPPER  = np.array([ 10, 255, 255], dtype=np.uint8)
TARGET_LOWER2 = np.array([170, 120,  80], dtype=np.uint8)
TARGET_UPPER2 = np.array([180, 255, 255], dtype=np.uint8)
MIN_AREA      = 300   # pixels — ignore very small detections

# ── Results exported for use by step3 ─────────────────────────────────────────────
target_cx = 0   # pixel column of target centre  (0 = left, 639 = right)
target_cy = 0   # pixel row    of target centre  (0 = top,  479 = bottom)

_done = False

def reset():
    global _done, target_cx, target_cy
    _done = False; target_cx = 0; target_cy = 0

def update(drone):
    """
    Capture a colour image and search for the red target.
    Hover in place while scanning.
    Returns True when the target is found.
    """
    global _done, target_cx, target_cy
    if _done:
        return True

    drone.flight.stop()   # hover while searching

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Step 1: image = drone.camera.get_color_image()   # BGR, 480×640
    # Step 2: contours1 = uav_utils.find_contours(image, TARGET_LOWER,  TARGET_UPPER)
    #         contours2 = uav_utils.find_contours(image, TARGET_LOWER2, TARGET_UPPER2)
    #         all_contours = contours1 + contours2
    # Step 3: best = uav_utils.get_largest_contour(all_contours, MIN_AREA)
    # Step 4: if best is not None:
    #             cx, cy = uav_utils.get_contour_center(best)
    #             target_cx, target_cy = cx, cy
    #             print a message showing cx, cy, and area
    #             _done = True

    ###### END PUT CODE HERE #########
    ##################################

    return _done
