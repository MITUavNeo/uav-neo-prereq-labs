"""
Step 2 — Altitude Control
Use proportional feedback to climb to a specific altitude.

Your task:
    Implement a P-controller (proportional controller):
        error    = TARGET_ALTITUDE - current_altitude
        throttle = Kp * error   (clamped to [-MAX_THROTTLE, MAX_THROTTLE])

    When |error| < THRESHOLD, stop and return True.

P-controller recap:
    - A large positive error means we're too low → send positive throttle (ascend)
    - A large negative error means we're too high → send negative throttle (descend)
    - As error approaches 0, throttle approaches 0 → smooth landing on target
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../library'))

import drone_core

# ── Constants ──────────────────────────────────────────────────────────────────────
TARGET_ALTITUDE = 3.0   # metres — target height above origin
THRESHOLD       = 0.12  # metres — acceptable error band
MAX_THROTTLE    = 0.5   # PCMD throttle limit (0.0 – 1.0)
KP              = 2.5   # proportional gain for throttle controller

# ── Module-level state ─────────────────────────────────────────────────────────────
_done = False

# ──────────────────────────────────────────────────────────────────────────────────

def reset():
    global _done
    _done = False


def update(drone):
    """
    Climb or descend to TARGET_ALTITUDE using a proportional controller.
    Returns True when within THRESHOLD metres of TARGET_ALTITUDE.
    """
    global _done
    if _done:
        return True

    altitude = drone.physics.get_altitude()
    error    = TARGET_ALTITUDE - altitude

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Hint 1: if abs(error) < THRESHOLD → stop, print success, set _done = True, return True
    # Hint 2: throttle = max(-MAX_THROTTLE, min(MAX_THROTTLE, KP * error))
    # Hint 3: drone.flight.send_pcmd(pitch, roll, yaw, throttle) — only throttle changes here

    ###### END PUT CODE HERE #########
    ##################################

    return False


# ── Standalone runner ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    _drone = drone_core.create_drone()
    _phase = 0

    def start():
        global _phase
        _phase = 0
        reset()
        print("Step 2: Altitude Control")
        _drone.flight.takeoff()

    def _update():
        global _phase
        if _phase == 0:
            _drone.flight.takeoff()
            if _drone.get_delta_time() > 0 and _drone.physics.get_altitude() > 0.5:
                _phase = 1
                reset()
        else:
            done = update(_drone)
            if done:
                _drone.flight.land()

    _drone.set_start_update(start, _update)
    _drone.go()
