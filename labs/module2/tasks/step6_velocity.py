"""
Step 6 — Velocity Control
Fly using raw PCMD commands to demonstrate pitch, roll, yaw, and throttle.

send_pcmd(pitch, roll, yaw, throttle) — all values in [-1.0, 1.0]:
    pitch    > 0  → forward     pitch    < 0  → backward
    roll     > 0  → right       roll     < 0  → left
    yaw      > 0  → CW (right)  yaw      < 0  → CCW (left)
    throttle > 0  → ascend      throttle < 0  → descend

Your task:
    Loop through MANOEUVRES in order.
    For each manoeuvre, send the PCMD command for 'duration' seconds, then advance.
    When all manoeuvres are done, stop and return True.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../library'))

import drone_core

# ── Velocity manoeuvre sequence ────────────────────────────────────────────────────
# Each entry: (pitch, roll, yaw, throttle, duration_seconds, label)
MANOEUVRES = [
    ( 0.5,  0.0,  0.0,  0.0, 2.0, "Fly FORWARD  (pitch=+0.5)"),
    ( 0.0,  0.0,  0.0,  0.0, 1.0, "Hover pause"),
    (-0.5,  0.0,  0.0,  0.0, 1.5, "Fly BACKWARD (pitch=-0.5)"),
    ( 0.0,  0.0,  0.0,  0.0, 1.0, "Hover pause"),
    ( 0.0,  0.5,  0.0,  0.0, 2.0, "Strafe RIGHT (roll=+0.5)"),
    ( 0.0,  0.0,  0.0,  0.0, 1.0, "Hover pause"),
    ( 0.0, -0.5,  0.0,  0.0, 2.0, "Strafe LEFT  (roll=-0.5)"),
    ( 0.0,  0.0,  0.0,  0.0, 1.0, "Hover pause"),
    ( 0.0,  0.0,  0.0,  0.3, 1.5, "ASCEND       (throttle=+0.3)"),
    ( 0.0,  0.0,  0.0, -0.3, 1.5, "DESCEND      (throttle=-0.3)"),
    ( 0.0,  0.0,  0.0,  0.0, 1.0, "Hover pause"),
]

# ── Module-level state ─────────────────────────────────────────────────────────────
_manoeuvre_index = 0
_timer           = 0.0
_done            = False

# ──────────────────────────────────────────────────────────────────────────────────

def reset():
    global _manoeuvre_index, _timer, _done
    _manoeuvre_index = 0
    _timer           = 0.0
    _done            = False


def update(drone):
    """
    Execute each manoeuvre in sequence for its specified duration.
    Returns True when all manoeuvres are complete.
    """
    global _manoeuvre_index, _timer, _done
    if _done:
        return True

    if _manoeuvre_index >= len(MANOEUVRES):
        drone.flight.stop()
        print("[Step 6] Velocity demo complete!")
        _done = True
        return True

    pitch, roll, yaw, throttle, duration, label = MANOEUVRES[_manoeuvre_index]

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Hint 1: When _timer == 0.0, print the label (this fires once when the manoeuvre starts)
    # Hint 2: drone.flight.send_pcmd(pitch, roll, yaw, throttle)
    # Hint 3: _timer += drone.get_delta_time()
    # Hint 4: When _timer >= duration → _manoeuvre_index += 1; _timer = 0.0

    ###### END PUT CODE HERE #########
    ##################################

    return False


# ── Standalone runner ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    _drone = drone_core.create_drone()
    _phase_main = 0

    def start():
        global _phase_main
        _phase_main = 0
        reset()
        print("Step 6: Velocity Control")

    def _update():
        global _phase_main
        if _phase_main == 0:
            _drone.flight.takeoff()
            if _drone.physics.get_altitude() > 1.0:
                _phase_main = 1; reset()
        else:
            done = update(_drone)
            if done:
                _drone.flight.land()

    _drone.set_start_update(start, _update)
    _drone.go()
