"""Final Challenge 2 — False Wall Maze
Navigate a corridor with multiple walls using ArUco marker IDs.

    ID = 0  → FAKE wall  — fly straight through (FLY_THROUGH_DURATION seconds)
    ID = 1  → REAL wall  — turn right 90° (CW = cur − 90°), then advance
    ID = 2  → END marker — maze complete, return True
    None    → no marker  — hover and wait

Same algorithm as Module 3 Part 2.

Your task:
    Implement reset() and update() below.
    Merge the detection loop (step3_loop) and action handler (step2_action)
    into a single update() function.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../../library'))
import drone_core
import drone_utils as uav_utils
import cv2

ARUCO_DICT           = cv2.aruco.DICT_6X6_250
FLY_THROUGH_DURATION = 3.0   # s — time to fly through a fake wall
ADVANCE_DURATION     = 1.5   # s — time to advance after real-wall turn
FLY_SPEED            = 0.4
YAW_SPEED            = 0.5
YAW_THRESHOLD        = 3.0

# _phase: 0=detect/idle, 1=fly_through_fake, 2=turning, 3=advancing, 4=done
_phase      = 0
_timer      = 0.0
_target_yaw = 0.0
_last_id    = None
_done       = False


def reset():
    global _phase, _timer, _target_yaw, _last_id, _done
    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Reset all state variables

    ###### END PUT CODE HERE #########
    ##################################


def _yaw_error(target, current):
    return ((target - current) + 180) % 360 - 180


def update(drone):
    """
    Scan for ArUco markers and navigate accordingly.
    Returns True when the END marker (ID=2) is reached.

    Hints:
        image   = drone.camera.get_color_image()
        markers = uav_utils.get_ar_markers(image, ARUCO_DICT)
        detected_id = markers[0].get_id() if markers else None

        Only trigger a new action when detected_id != _last_id AND _phase == 0:
            ID=0 → _phase = 1 (fly through)
            ID=1 → compute _target_yaw = (cur - 90) % 360, _phase = 2 (turn right)
            ID=2 → stop, _phase = 4, _done = True, return True

        Phase 1 (fly through): send_pcmd(FLY_SPEED, 0, 0, 0), timer → FLY_THROUGH_DURATION
        Phase 2 (turn right):  yaw toward _target_yaw using _yaw_error()
        Phase 3 (advance):     send_pcmd(FLY_SPEED, 0, 0, 0), timer → ADVANCE_DURATION
        Phase 0 (idle):        drone.flight.stop()
    """
    global _phase, _timer, _target_yaw, _last_id, _done
    if _done:
        return True

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE

    ###### END PUT CODE HERE #########
    ##################################

    return _done
