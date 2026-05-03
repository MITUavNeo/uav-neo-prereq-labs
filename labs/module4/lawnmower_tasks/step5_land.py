"""Module 4 Lawnmower — Step 5: Land on Target
Centre the drone over the target using the downward camera, then land.
(Same algorithm as spiral/step4_land.py)

Your task:
    Phase 0: Centre using camera. Compute roll/pitch corrections.
             When aligned → Phase 1.
    Phase 1: drone.flight.land() until _land_timer > 5s.
"""

import drone_core
import numpy as np

TARGET_LOWER = np.array([ 40, 100,  80], dtype=np.uint8)
TARGET_UPPER = np.array([ 80, 255, 255], dtype=np.uint8)
CENTRE_THRESHOLD = 40
IMAGE_CX = 320; IMAGE_CY = 240

_phase = 0; _land_timer = 0.0; _done = False

def reset():
    global _phase, _land_timer, _done
    _phase = 0; _land_timer = 0.0; _done = False

def update(drone):
    global _phase, _land_timer, _done
    if _done: return True

    if _phase == 0:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Same as spiral/step4_land.py:
        # Get downward/colour image, find green target, correct roll/pitch
        # When centred → Phase 1

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:
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
