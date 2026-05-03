"""
Challenge 2 — Fly Through Gates
Navigate through a series of gates placed along the +forward axis.

Each gate is defined by how far forward to fly before the next one.
Adjust GATE_DISTANCES and GATE_ALTITUDE to match your scene layout.

Your task:
    1. Each frame, integrate velocity[2] × dt to track _fwd (total forward distance).
    2. For the current gate, fly forward with FLY_SPEED pitch and maintain
       GATE_ALTITUDE using a throttle P-controller.
    3. When _fwd >= _leg_start_fwd + GATE_DISTANCES[_gate_index]:
           print gate passed, save _leg_start_fwd = _fwd, advance _gate_index
    4. When all gates passed → stop and return True.
"""

import math

import drone_core

# ── Gate waypoints (metres forward from previous gate / takeoff point) ─────────────
# Adjust these values to match the gate positions in Module2_DroneControl.unity
GATE_DISTANCES = [5.0, 5.0, 5.0]   # fly 5m forward to reach each gate
GATE_ALTITUDE  = 2.5                # metres — fly at this height through the gates
FLY_SPEED      = 0.45               # PCMD pitch magnitude
MAX_THROTTLE   = 0.4

# ── Module-level state ─────────────────────────────────────────────────────────────
_gate_index    = 0
_fwd           = 0.0    # dead-reckoning forward distance
_leg_start_fwd = 0.0    # forward position when this leg started
_done          = False

# ──────────────────────────────────────────────────────────────────────────────────

def reset():
    global _gate_index, _fwd, _leg_start_fwd, _done
    _gate_index    = 0
    _fwd           = 0.0
    _leg_start_fwd = 0.0
    _done          = False


def update(drone):
    """
    Fly through each gate by covering its target forward distance.
    Maintains GATE_ALTITUDE throughout.
    Returns True when all gates have been passed.
    """
    global _gate_index, _fwd, _leg_start_fwd, _done
    if _done:
        return True

    if _gate_index >= len(GATE_DISTANCES):
        drone.flight.stop()
        print(f"[Challenge 2] All {len(GATE_DISTANCES)} gates passed!")
        _done = True
        return True

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Step 1: dt = drone.get_delta_time(); vel = drone.physics.get_linear_velocity()
    #         _fwd += vel[2] * dt
    #
    # Step 2: Compute remaining distance to next gate
    #         leg_target = _leg_start_fwd + GATE_DISTANCES[_gate_index]
    #         remaining  = leg_target - _fwd
    #         err_alt    = GATE_ALTITUDE - drone.physics.get_altitude()
    #
    # Step 3: If remaining <= 0.3 (reached gate):
    #             print gate passed message
    #             _leg_start_fwd = _fwd
    #             _gate_index += 1
    #         Else:
    #             throttle = max(-MAX_THROTTLE, min(MAX_THROTTLE, err_alt * 2.5))
    #             drone.flight.send_pcmd(FLY_SPEED, 0, 0, throttle)

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
        print("Challenge 2: Fly Through Gates")

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
