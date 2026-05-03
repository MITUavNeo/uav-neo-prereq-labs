"""Module 4 Lawnmower — Step 4: Search Loop
Alternate forward/backward passes with sideways steps until target found.

Pattern:
    Phase 0: Fly pass (step3_fly_pass)
        - If target found → _done = True
        - If pass done → flip _at_bottom, Phase 1
    Phase 1: Step sideways (step2_step_side)
        - When done → _row += 1, reset step3 with new _at_bottom, Phase 0
    Safety: stop after MAX_ROWS rows.

Your task:
    Implement the phase logic described above.
"""

import drone_core
from . import step2_step_side, step3_fly_pass

MAX_ROWS = 8
_row        = 0
_at_bottom  = True
_phase      = 0   # 0=pass, 1=step_side
_done       = False

def reset():
    global _row, _at_bottom, _phase, _done
    _row = 0; _at_bottom = True; _phase = 0; _done = False
    step3_fly_pass.reset(_at_bottom)

def update(drone):
    global _row, _at_bottom, _phase, _done
    if _done: return True
    if _row >= MAX_ROWS:
        drone.flight.stop()
        print("[Lawnmower Step 4] Max rows reached.")
        _done = True; return True

    if _phase == 0:   # fly pass
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # found = step3_fly_pass.update(drone)
        # if found → _done = True; return True
        # if step3_fly_pass._done:
        #     _at_bottom = not _at_bottom
        #     _phase = 1; step2_step_side.reset()

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:  # step sideways
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # if step2_step_side.update(drone):
        #     _row += 1; _phase = 0
        #     step3_fly_pass.reset(_at_bottom)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return False
