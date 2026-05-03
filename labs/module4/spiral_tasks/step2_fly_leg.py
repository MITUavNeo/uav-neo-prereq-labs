"""Module 4 Spiral — Step 2: Fly One Leg
Fly forward for a specified duration while scanning for the SAR target.

Returns: True if target found (stores detection), False if leg complete without finding it.
Exports: found_contour, found_cx, found_cy for use by step4_land.

Your task:
    Each frame:
    1. Fly forward: drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)
    2. Get camera image and look for green target (TARGET_LOWER/UPPER).
    3. If target found → stop, set found_contour/found_cx/found_cy, set _found=True, _done=True, return True.
    4. If _timer >= _duration (leg done, no target) → stop, set _done=True.
    5. return _found (False if leg ended without finding target)
"""

import numpy as np
import drone_core, drone_utils as uav_utils

# Target colour: bright green landing pad (adjust for your scene)
TARGET_LOWER = np.array([ 40, 100,  80], dtype=np.uint8)
TARGET_UPPER = np.array([ 80, 255, 255], dtype=np.uint8)
MIN_AREA     = 400
FLY_SPEED    = 0.35

# Exported results
found_contour = None
found_cx      = 0
found_cy      = 0

_duration = 1.0   # set by reset()
_timer    = 0.0
_done     = False
_found    = False

def reset(duration=1.0):
    global _duration, _timer, _done, _found, found_contour
    _duration = duration; _timer = 0.0; _done = False; _found = False
    found_contour = None

def update(drone):
    global _timer, _done, _found, found_contour, found_cx, found_cy
    if _done: return _found

    _timer += drone.get_delta_time()

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Step 1: drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)
    # Step 2: image = drone.camera.get_color_image()
    #         contours = uav_utils.find_contours(image, TARGET_LOWER, TARGET_UPPER)
    #         best = uav_utils.get_largest_contour(contours, MIN_AREA)
    # Step 3: if best is not None:
    #             found_contour = best
    #             found_cx, found_cy = uav_utils.get_contour_center(best)
    #             area = uav_utils.get_contour_area(best)
    #             drone.flight.stop(); print message
    #             _found = True; _done = True; return True
    # Step 4: if _timer >= _duration → drone.flight.stop(); _done = True

    ###### END PUT CODE HERE #########
    ##################################

    return _found
