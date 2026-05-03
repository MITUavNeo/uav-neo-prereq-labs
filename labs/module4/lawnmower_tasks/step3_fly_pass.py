"""Module 4 Lawnmower — Step 3: Fly One Pass
Sweep forward (or backward) across the search area, scanning for the target.

_at_bottom=True  → fly forward  (+pitch)
_at_bottom=False → fly backward (-pitch)

Returns True if target found, False when pass length reached.

Your task:
    Each frame:
    1. Accumulate abs(vel[2]) * dt into _fwd (distance along the pass).
    2. Determine pitch sign: FLY_SPEED if _at_bottom else -FLY_SPEED.
    3. Send PCMD (pitch, 0, 0, 0).
    4. Check camera for green target. If found → stop, export found_cx/found_cy,
       set _found=True, _done=True, return True.
    5. If _fwd >= PASS_LENGTH → stop, _done=True.
    6. Return _found.
"""

import sys, os
import numpy as np
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core, drone_utils as uav_utils

TARGET_LOWER  = np.array([ 40, 100,  80], dtype=np.uint8)
TARGET_UPPER  = np.array([ 80, 255, 255], dtype=np.uint8)
MIN_AREA      = 400
PASS_LENGTH   = 6.0   # metres — length of each sweep pass
FLY_SPEED     = 0.35

found_cx = 0; found_cy = 0
_at_bottom = True; _fwd = 0.0; _done = False; _found = False

def reset(at_bottom=True):
    global _at_bottom, _fwd, _done, _found, found_cx, found_cy
    _at_bottom = at_bottom; _fwd = 0.0; _done = False; _found = False
    found_cx = 0; found_cy = 0

def update(drone):
    global _fwd, _done, _found, found_cx, found_cy
    if _done: return _found

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # vel = drone.physics.get_linear_velocity()
    # _fwd += abs(vel[2]) * drone.get_delta_time()
    # pitch = FLY_SPEED if _at_bottom else -FLY_SPEED
    # drone.flight.send_pcmd(pitch, 0, 0, 0)
    # image = drone.camera.get_color_image()
    # contours = uav_utils.find_contours(image, TARGET_LOWER, TARGET_UPPER)
    # best = uav_utils.get_largest_contour(contours, MIN_AREA)
    # if best is not None:
    #     found_cx, found_cy = uav_utils.get_contour_center(best)
    #     drone.flight.stop(); print; _found = True; _done = True; return True
    # if _fwd >= PASS_LENGTH:
    #     drone.flight.stop(); _done = True

    ###### END PUT CODE HERE #########
    ##################################

    return _found
