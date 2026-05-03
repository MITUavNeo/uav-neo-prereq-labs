"""
Step 4 — Relative Position
Record the current position, then fly a fixed offset from it.

"Relative" means the target is computed from wherever the drone
happens to be when reset() is called — not a fixed world location.

Your task:
    1. On the first frame, record the drone's current altitude as _start_alt.
       Set _target_alt = _start_alt + OFFSET_UP.
    2. Integrate velocity each frame to track _fwd and _rgt.
    3. Send proportional PCMD until OFFSET_FORWARD / OFFSET_RIGHT / OFFSET_UP
       are reached within POSITION_THRESHOLD.
"""

import math

import drone_core

# ── Offset to fly from the current position ────────────────────────────────────────
OFFSET_FORWARD = 3.0    # metres forward
OFFSET_RIGHT   = 2.0    # metres right (negative = left)
OFFSET_UP      = 0.5    # metres up    (negative = down)

POSITION_THRESHOLD = 0.4
MAX_SPEED    = 0.4
MAX_THROTTLE = 0.5

# ── Module-level state ─────────────────────────────────────────────────────────────
_fwd          = 0.0
_rgt          = 0.0
_start_alt    = 0.0
_target_alt   = 0.0
_done         = False

# ──────────────────────────────────────────────────────────────────────────────────

def reset():
    global _fwd, _rgt, _start_alt, _target_alt, _done
    _fwd        = 0.0
    _rgt        = 0.0
    _done       = False
    # Target altitude is set in first update() call (needs live drone data)
    _start_alt  = -1.0   # sentinel — set on first frame


def update(drone):
    """
    On the first frame: record the drone's altitude to compute the target.
    Then fly forward/right/up by the defined offsets.
    Returns True when within POSITION_THRESHOLD of the target.
    """
    global _fwd, _rgt, _start_alt, _target_alt, _done
    if _done:
        return True

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Step 1: If _start_alt < 0 (first frame):
    #           _start_alt  = drone.physics.get_altitude()
    #           _target_alt = _start_alt + OFFSET_UP
    #           print a message showing starting alt and target
    #
    # Step 2: Integrate velocity (same as step3)
    #           dt  = drone.get_delta_time()
    #           vel = drone.physics.get_linear_velocity()
    #           _fwd += vel[2] * dt
    #           _rgt += vel[0] * dt
    #
    # Step 3: Compute errors to OFFSET_FORWARD, OFFSET_RIGHT, _target_alt
    #
    # Step 4: If close enough → stop, print, set _done = True, return True
    #
    # Step 5: Send proportional PCMD (pitch, roll, 0, throttle)

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
        print("Step 4: Relative Position")

    def _update():
        global _phase
        if _phase == 0:
            _drone.flight.takeoff()
            if _drone.physics.get_altitude() > 1.0:
                _phase = 1; reset()
        else:
            done = update(_drone)
            if done:
                _drone.flight.land()

    _drone.set_start_update(start, _update)
    _drone.go()
