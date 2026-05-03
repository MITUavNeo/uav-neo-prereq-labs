"""Module 4 Lawnmower — Step 2: Step Sideways
Move one row-width to the right before the next pass.

Your task:
    Each frame:
    1. Integrate vel[0] * dt to track _rgt (rightward distance).
    2. Compute err = ROW_WIDTH - _rgt.
    3. If |err| < 0.2 → stop, print, _done = True.
    4. Else → roll = clamp(err * 0.25, -MAX_SPEED, MAX_SPEED)
              drone.flight.send_pcmd(0, roll, 0, 0)
"""

import drone_core

ROW_WIDTH  = 2.0    # metres between lawnmower rows
MAX_SPEED  = 0.35

_rgt = 0.0; _done = False

def reset():
    global _rgt, _done
    _rgt = 0.0; _done = False

def update(drone):
    global _rgt, _done
    if _done: return True

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # vel = drone.physics.get_linear_velocity()
    # _rgt += vel[0] * drone.get_delta_time()
    # err = ROW_WIDTH - _rgt
    # if |err| < 0.2 → stop, print, _done = True
    # else → roll = max(-MAX_SPEED, min(MAX_SPEED, err * 0.25))
    #         drone.flight.send_pcmd(0, roll, 0, 0)

    ###### END PUT CODE HERE #########
    ##################################

    return _done
