"""
Step 1 — Takeoff
Arm the motors and hover until the drone reaches a stable altitude.

Your task:
    1. Call drone.flight.takeoff() every frame to arm the motors.
    2. Wait TAKEOFF_WAIT seconds for the drone to stabilise.
    3. Print the achieved altitude and return True.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../library'))

import drone_core

# ── Constants ──────────────────────────────────────────────────────────────────────
TAKEOFF_WAIT = 3.5   # seconds to allow the automatic launch sequence to complete

# ── Module-level state ─────────────────────────────────────────────────────────────
_timer = 0.0
_done  = False

# ──────────────────────────────────────────────────────────────────────────────────

def reset():
    """Call once before the first update() call to reset state."""
    global _timer, _done
    _timer = 0.0
    _done  = False


def update(drone):
    """
    Call every frame. Returns True when the step is complete.

    Tasks:
        1. Send the takeoff command.
        2. Wait TAKEOFF_WAIT seconds for the drone to stabilise.
        3. Print the achieved altitude.
    """
    global _timer, _done
    if _done:
        return True

    _timer += drone.get_delta_time()

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Hint: call drone.flight.takeoff() each frame
    # When _timer >= TAKEOFF_WAIT, stop, print altitude, and set _done = True

    ###### END PUT CODE HERE #########
    ##################################

    return _done


# ── Standalone runner ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    _drone = drone_core.create_drone()

    def start():
        reset()
        print("Step 1: Takeoff")

    def _update():
        done = update(_drone)
        if done:
            _drone.flight.land()

    _drone.set_start_update(start, _update)
    _drone.go()
