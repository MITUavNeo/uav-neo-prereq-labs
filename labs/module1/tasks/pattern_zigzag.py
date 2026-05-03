"""Module 1 Pattern: Zigzag — alternate roll left/right while flying forward.

Returns True after CYCLES complete swings.

Hint: a sinusoidal roll command produces a smooth zigzag.
    roll = ROLL_AMP * math.sin(2 * math.pi * _elapsed / SWING_PERIOD)
"""

import math
import drone_core

FORWARD_PITCH = 0.4    # constant forward speed
ROLL_AMP      = 0.5    # left/right swing magnitude
SWING_PERIOD  = 2.0    # seconds per left-right cycle
CYCLES        = 3      # how many full swings before done

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

    dt = drone.get_delta_time()
    _elapsed += dt

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    #
    # 1) Compute a sinusoidal roll value (see hint in docstring above).
    # 2) Call drone.flight.send_pcmd(FORWARD_PITCH, roll, 0, 0).
    # 3) When _elapsed >= CYCLES * SWING_PERIOD, drone.flight.stop()
    #    and set _done = True.

    ###### END PUT CODE HERE #########
    ##################################

    return _done
