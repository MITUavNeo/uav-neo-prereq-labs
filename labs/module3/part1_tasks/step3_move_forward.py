"""
Module 3 Part 1 — Step 3: Move to Object
Fly toward the detected object while keeping it centred in the camera frame.

Your task:
    Each frame:
    1. Get the camera image and re-detect the red contour (same HSV as step2).
    2. If no contour → hover (lost the target).
    3. Get the contour's centroid: cx, cy = uav_utils.get_contour_center(best)
       Get the area:              area  = uav_utils.get_contour_area(best)
    4. If area >= STOP_AREA → stop, print, return True (close enough).
    5. Compute lateral error: lateral_error = (cx - IMAGE_CX) / IMAGE_CX  [-1..+1]
       Compute roll:          roll = clamp(lateral_error * CENTERING_GAIN, -0.4, 0.4)
    6. Fly: drone.flight.send_pcmd(APPROACH_SPEED, roll, 0, 0)
"""

import sys, os
import numpy as np
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))

import drone_core
import drone_utils as uav_utils
from . import step2_find_object   # re-use the colour detection from step2

# ── Constants ──────────────────────────────────────────────────────────────────────
APPROACH_SPEED  = 0.3    # forward PCMD pitch
CENTERING_GAIN  = 0.8    # lateral steering gain
STOP_AREA       = 8000   # stop when contour is this large (px²) — object is close
IMAGE_WIDTH     = 640
IMAGE_HEIGHT    = 480
IMAGE_CX        = IMAGE_WIDTH  // 2   # centre column
IMAGE_CY        = IMAGE_HEIGHT // 2   # centre row

_done = False

def reset():
    global _done
    _done = False

def update(drone):
    """
    Fly forward while steering to keep the red target centred.
    Stops when the object's contour area >= STOP_AREA (close enough).
    Returns True when done.
    """
    global _done
    if _done:
        return True

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Step 1: image = drone.camera.get_color_image()
    #         Use step2_find_object.TARGET_LOWER/UPPER and TARGET_LOWER2/UPPER2
    #         to find contours and get the largest one
    # Step 2: if best is None → drone.flight.stop(); return False
    # Step 3: cx, cy = uav_utils.get_contour_center(best)
    #         area   = uav_utils.get_contour_area(best)
    # Step 4: if area >= STOP_AREA → stop, print, set _done = True, return True
    # Step 5: lateral_error = (cx - IMAGE_CX) / IMAGE_CX
    #         roll = max(-0.4, min(0.4, lateral_error * CENTERING_GAIN))
    # Step 6: drone.flight.send_pcmd(APPROACH_SPEED, roll, 0, 0)

    ###### END PUT CODE HERE #########
    ##################################

    return False
