"""Module 1 Pattern: Hallway — fly forward 5 m, rotate 180°, fly back.

Phase machine:
    phase 0 (FORWARD)    — pitch forward until OUT_DURATION
    phase 1 (TURNING)    — yaw right until TURN_DURATION (≈180°)
    phase 2 (RETURNING)  — pitch forward until RET_DURATION
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../library'))
import drone_core

FORWARD_PITCH = 0.4
YAW_RATE      = 0.5
OUT_DURATION  = 4.0    # seconds — out leg
TURN_DURATION = 2.0    # seconds — 180° turn at YAW_RATE
RET_DURATION  = 4.0    # seconds — return leg

_phase = 0
_timer = 0.0
_done  = False


def reset():
    global _phase, _timer, _done
    _phase = 0; _timer = 0.0; _done = False


def update(drone):
    global _phase, _timer, _done
    if _done:
        return True

    _timer += drone.get_delta_time()

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    #
    # Build a 3-phase state machine:
    #   if _phase == 0:  # forward
    #       drone.flight.send_pcmd(FORWARD_PITCH, 0, 0, 0)
    #       advance to phase 1 when _timer >= OUT_DURATION (reset _timer)
    #
    #   elif _phase == 1:  # 180° turn
    #       drone.flight.send_pcmd(0, 0, YAW_RATE, 0)
    #       advance to phase 2 when _timer >= TURN_DURATION
    #
    #   elif _phase == 2:  # return leg
    #       drone.flight.send_pcmd(FORWARD_PITCH, 0, 0, 0)
    #       when _timer >= RET_DURATION: drone.flight.stop(), _done = True

    ###### END PUT CODE HERE #########
    ##################################

    return _done
