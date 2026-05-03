"""Module 4 Lawnmower — Step 1: Setup
Take off and reach search altitude. (Same pattern as spiral step1.)

Your task:
    Phase 0: Takeoff — wait TAKEOFF_WAIT seconds.
    Phase 1: Proportional throttle to SEARCH_ALTITUDE.
             When |err| < 0.12 → stop, print, _done = True.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core

SEARCH_ALTITUDE = 2.5
TAKEOFF_WAIT    = 3.5
_phase = 0; _timer = 0.0; _done = False

def reset():
    global _phase, _timer, _done
    _phase = 0; _timer = 0.0; _done = False

def update(drone):
    global _phase, _timer, _done
    if _done: return True
    _timer += drone.get_delta_time()

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

    return _done
