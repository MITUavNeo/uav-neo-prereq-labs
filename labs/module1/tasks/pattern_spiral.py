"""Module 1 Pattern: Spiral — constant forward + constant yaw → expanding circle.

Returns True after DURATION seconds.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../library'))
import drone_core

FORWARD_PITCH = 0.3    # constant forward speed
YAW_RATE      = 0.4    # constant rotation rate
DURATION      = 6.0    # seconds

_elapsed = 0.0
_done    = False


def reset():
    global _elapsed, _done
    _elapsed = 0.0
    _done    = False


def update(drone):
    global _elapsed, _done
    if _done:
        return True

    _elapsed += drone.get_delta_time()

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    #
    # 1) drone.flight.send_pcmd(FORWARD_PITCH, 0, YAW_RATE, 0)
    # 2) When _elapsed >= DURATION, drone.flight.stop() and set _done = True.

    ###### END PUT CODE HERE #########
    ##################################

    return _done
