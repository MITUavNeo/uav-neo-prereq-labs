"""Module 4 Spiral — Step 4: Land on Target
Centre the drone over the target using the downward camera, then land.

Your task:
    Phase 0 (centre):
        Try to get a downward camera image. Detect green target.
        If target found: compute err_x = cx - IMAGE_CX, err_y = cy - IMAGE_CY
        If |err_x| < CENTRE_THRESHOLD and |err_y| < CENTRE_THRESHOLD → stop, Phase 1
        Else → pitch/roll to correct position:
               roll  = clamp(err_x / IMAGE_CX, -MAX_ROLL, MAX_ROLL)
               pitch = clamp(err_y / IMAGE_CY, -MAX_PITCH, MAX_PITCH)
    Phase 1 (land):
        Call drone.flight.land() every frame.
        After 5 seconds → print, set _done = True.
"""

import numpy as np
import drone_core, drone_utils as uav_utils
from . import step2_fly_leg   # re-use colour constants

CENTRE_THRESHOLD = 40   # pixels — close enough to centre
MAX_ROLL  = 0.3
MAX_PITCH = 0.3
IMAGE_CX  = 320; IMAGE_CY = 240

_phase = 0; _land_timer = 0.0; _done = False

def reset():
    global _phase, _land_timer, _done
    _phase = 0; _land_timer = 0.0; _done = False

def update(drone):
    global _phase, _land_timer, _done
    if _done: return True

    if _phase == 0:   # centre over target using downward camera
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Step 1: try: img = drone.camera.get_downward_image()
        #         except: img = drone.camera.get_color_image()
        # Step 2: contours = uav_utils.find_contours(img, step2_fly_leg.TARGET_LOWER, step2_fly_leg.TARGET_UPPER)
        #         best = uav_utils.get_largest_contour(contours, 200)
        # Step 3: if best is None → drone.flight.stop(); return False
        # Step 4: cx, cy = uav_utils.get_contour_center(best)
        #         err_x = cx - IMAGE_CX; err_y = cy - IMAGE_CY
        # Step 5: if |err_x| < CENTRE_THRESHOLD and |err_y| < CENTRE_THRESHOLD:
        #             stop, print, _phase = 1, _land_timer = 0.0
        #         else: roll/pitch correction

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:  # land
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # drone.flight.land()
        # _land_timer += drone.get_delta_time()
        # if _land_timer > 5.0 → print, _done = True

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return _done
