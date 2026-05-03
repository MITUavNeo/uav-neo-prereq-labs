"""
Module 3 Part 2 — Step 2: ArUco Action
Decide what to do based on the detected ArUco marker ID.

    ID = 0  → FAKE wall  — fly straight through for FLY_THROUGH_DURATION seconds
    ID = 1  → REAL wall  — turn right 90° (CW = cur - 90°), then advance
    ID = 2  → END marker — maze complete, stop and set _done = True
    None    → no marker  — hover

trigger(drone, marker_id) is called by step3_loop when a NEW marker is detected.
update(drone) is called every frame to execute the current action.
Returns True only when ID=2 (maze end) is reached.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))

import drone_core
import drone_utils as uav_utils

# ── Timing constants ───────────────────────────────────────────────────────────────
FLY_THROUGH_DURATION = 3.0   # seconds to fly through a fake wall
ADVANCE_DURATION     = 1.5   # seconds to advance after turning at a real wall
FLY_SPEED            = 0.4
YAW_SPEED            = 0.5
YAW_THRESHOLD        = 3.0

# ── Module-level state ─────────────────────────────────────────────────────────────
_phase      = 0   # 0=idle, 1=fly_through, 2=turning, 3=advancing, 4=maze_done
_timer      = 0.0
_target_yaw = 0.0
_done       = False   # True only when ID=2 received

# ──────────────────────────────────────────────────────────────────────────────────

def reset():
    global _phase, _timer, _target_yaw, _done
    _phase = 0; _timer = 0.0; _target_yaw = 0.0; _done = False


def _yaw_error(target, current):
    return ((target - current) + 180) % 360 - 180


def trigger(drone, marker_id):
    """
    Called by step3_loop when a new marker is detected.
    Sets the action phase based on marker_id.
    """
    global _phase, _timer, _target_yaw, _done

    if _phase != 0:   # already executing an action
        return

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # if marker_id == 0 (FAKE wall):
    #     print message, set _phase = 1, _timer = 0.0
    #
    # elif marker_id == 1 (REAL wall):
    #     current = drone.physics.get_attitude()[1] % 360
    #     _target_yaw = (current - 90) % 360   # 90° CW turn
    #     print message, set _phase = 2, _timer = 0.0
    #
    # elif marker_id == 2 (END):
    #     print message, stop, _phase = 4, _done = True
    #
    # else (None / no detection):
    #     drone.flight.stop()  # hover

    ###### END PUT CODE HERE #########
    ##################################


def update(drone):
    """
    Execute the current action phase.
    Returns True only when ID=2 has been confirmed (maze done).
    """
    global _phase, _timer, _done

    if _phase == 0:   # idle — waiting for trigger()
        drone.flight.stop()
        return False

    elif _phase == 1:  # fly through fake wall
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Send forward PCMD, increment _timer
        # When _timer >= FLY_THROUGH_DURATION → stop, _phase = 0

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 2:  # turning at real wall
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Yaw to _target_yaw using shortest-path error
        # When |err| < YAW_THRESHOLD → stop, _phase = 3, _timer = 0.0

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 3:  # advance after turn
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Send forward PCMD, increment _timer
        # When _timer >= ADVANCE_DURATION → stop, _phase = 0

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 4:  # maze done
        drone.flight.stop()
        return True

    return _done
