"""Final Challenge 4 — Search and Rescue
Search for a magenta target disk using an expanding spiral pattern.
When found, centre the drone over it using the downward camera, then land.

Search pattern (expanding square spiral):
    fly_leg(duration) → turn left (CCW +90°) → fly_leg(duration) → turn left
    Increase leg duration by LEG_STEP every 2 legs.

Landing:
    Use downward camera to centre over the target, then call drone.flight.land().

Phases:
    0 = fly spiral leg (scan for target)
    1 = turn left 90°
    2 = centre over target (downward camera)
    3 = land

Your task:
    Implement reset() and update() below.
    (Combines Module 4 spiral search + Module 4 landing.)
"""

import sys, os
import numpy as np
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../../library'))
import drone_core
import drone_utils as uav_utils

# ── Target colour (HSV — magenta landing pad) ──────────────────────────────────
TARGET_LOWER = np.array([140, 100,  80], dtype=np.uint8)
TARGET_UPPER = np.array([170, 255, 255], dtype=np.uint8)
MIN_AREA     = 400

# ── Search parameters ──────────────────────────────────────────────────────────
SEARCH_ALTITUDE  = 3.0    # m — altitude during search
FLY_SPEED        = 0.35
MAX_THROTTLE     = 0.4
ALT_KP           = 2.5
LEG_START        = 1.5    # s — first spiral leg duration
LEG_STEP         = 0.5    # s — added every 2 legs
MAX_LEGS         = 20
YAW_SPEED        = 0.5
YAW_THRESH       = 3.0

# ── Centering / landing parameters ────────────────────────────────────────────
CENTRE_THRESHOLD = 40     # px — pixel error < this = centred
MAX_ROLL         = 0.3
MAX_PITCH        = 0.3
IMAGE_CX         = 320
IMAGE_CY         = 240
LAND_WAIT        = 5.0    # s

_phase        = 0
_leg_count    = 0
_leg_duration = LEG_START
_leg_timer    = 0.0
_target_yaw   = 0.0
_land_timer   = 0.0
_done         = False


def reset():
    global _phase, _leg_count, _leg_duration, _leg_timer, _target_yaw, _land_timer, _done
    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Reset all state variables

    ###### END PUT CODE HERE #########
    ##################################


def _yaw_err(t, c):
    return ((t - c) + 180) % 360 - 180


def update(drone):
    """
    Run one frame of SAR. Returns True when landed on target.

    Hints (Phase 0 — fly spiral leg):
        Maintain SEARCH_ALTITUDE with proportional throttle.
        drone.flight.send_pcmd(FLY_SPEED, 0, 0, throttle)
        _leg_timer += drone.get_delta_time()
        Scan camera: img = drone.camera.get_color_image()
            contours = uav_utils.find_contours(img, TARGET_LOWER, TARGET_UPPER)
            best     = uav_utils.get_largest_contour(contours, MIN_AREA)
            if best is not None → stop, _phase = 2
        If _leg_timer >= _leg_duration → compute _target_yaw = (cur + 90) % 360,
            _phase = 1, _leg_count += 1, every 2 legs: _leg_duration += LEG_STEP

    Hints (Phase 1 — turn left):
        Use _yaw_err; when aligned → _leg_timer = 0, _phase = 0

    Hints (Phase 2 — centre using downward camera):
        try: img = drone.camera.get_downward_image()
        except: img = drone.camera.get_color_image()
        Find contour; compute err_x = cx - IMAGE_CX, err_y = cy - IMAGE_CY
        If |err_x| < CENTRE_THRESHOLD and |err_y| < CENTRE_THRESHOLD → _phase = 3
        Else: roll = max(-MAX_ROLL, min(MAX_ROLL, err_x/IMAGE_CX)); pitch = max(-MAX_PITCH, min(MAX_PITCH, err_y/IMAGE_CY))
              drone.flight.send_pcmd(pitch, roll, 0, 0)

    Hints (Phase 3 — land):
        drone.flight.land()
        _land_timer += dt
        if _land_timer > LAND_WAIT → _done = True
    """
    global _phase, _leg_count, _leg_duration, _leg_timer, _target_yaw, _land_timer, _done
    if _done:
        return True

    if _phase == 0:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 2:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 3:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return _done
