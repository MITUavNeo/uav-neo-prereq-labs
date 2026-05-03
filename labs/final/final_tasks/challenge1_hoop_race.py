"""Final Challenge 1 — Hoop Race
Fly through 4 gates placed along the forward (+pitch) axis.

Each gate entry: (forward_distance_m, target_altitude_m)
  - forward_distance_m: metres to travel from the previous gate (dead-reckoning)
  - target_altitude_m:  altitude to maintain while flying through that gate

Algorithm:
    • Dead-reckoning: _fwd += vel[2] * dt  each frame
    • For each gate: fly forward at FLY_SPEED while holding target altitude
      (throttle = max(-MAX_THROTTLE, min(MAX_THROTTLE, ALT_KP * altitude_error)))
    • When _fwd reaches the gate's distance → move to next gate
    • When all gates cleared → return True

Your task:
    Implement reset() and update() below.
"""

import drone_core

# ── Gate waypoints: (metres_forward_from_prev_gate, target_altitude_m) ─────────
GATE_WAYPOINTS = [
    (8.0,  2.0),   # Gate 1
    (8.0,  3.0),   # Gate 2
    (8.0,  1.5),   # Gate 3
    (8.0,  2.5),   # Gate 4
]
FLY_SPEED      = 0.45
MAX_THROTTLE   = 0.4
ALT_KP         = 2.5
ARRIVAL_MARGIN = 0.5   # m — within this distance counts as "cleared"

# ── Module-level state ─────────────────────────────────────────────────────────
_gate_idx      = 0
_fwd           = 0.0
_leg_start_fwd = 0.0
_done          = False

# ──────────────────────────────────────────────────────────────────────────────


def reset():
    global _gate_idx, _fwd, _leg_start_fwd, _done
    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Reset _gate_idx, _fwd, _leg_start_fwd, _done to initial values

    ###### END PUT CODE HERE #########
    ##################################


def update(drone):
    """
    Fly through each gate by covering its forward distance at the correct altitude.
    Returns True when all gates have been passed.

    Hints:
        dt  = drone.get_delta_time()
        vel = drone.physics.get_linear_velocity()   # vel[2] = forward speed
        _fwd += vel[2] * dt                         # dead-reckoning

        dist, alt = GATE_WAYPOINTS[_gate_idx]
        remaining = (_leg_start_fwd + dist) - _fwd
        err_alt   = alt - drone.physics.get_altitude()

        if remaining <= ARRIVAL_MARGIN:
            → print cleared, update _leg_start_fwd and _gate_idx
        else:
            throttle = max(-MAX_THROTTLE, min(MAX_THROTTLE, ALT_KP * err_alt))
            drone.flight.send_pcmd(FLY_SPEED, 0, 0, throttle)

        Check _gate_idx >= len(GATE_WAYPOINTS) → all done, return True
    """
    global _gate_idx, _fwd, _leg_start_fwd, _done
    if _done:
        return True

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE

    ###### END PUT CODE HERE #########
    ##################################

    return False
