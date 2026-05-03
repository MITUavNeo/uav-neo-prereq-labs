"""
Challenge 1 — Fly a Square
Fly the drone in a 4-sided square pattern using a loop.

Algorithm:
    For each of NUM_SIDES legs:
        Phase 0: Fly forward for LEG_DURATION seconds
        Phase 1: Turn right 90° (CW = subtract 90° from current heading)
    Land.

Yaw hint:
    _target_yaw = (current_heading - 90) % 360    # 90° CW turn
    error = ((target - current) + 180) % 360 - 180
    Send negative yaw_cmd for CW rotation.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../library'))

import drone_core

# ── Constants ──────────────────────────────────────────────────────────────────────
LEG_DURATION = 3.0   # seconds per side
FLY_SPEED    = 0.4   # PCMD pitch magnitude
YAW_SPEED    = 0.5   # PCMD yaw magnitude for turns
YAW_THRESHOLD = 3.0  # degrees — acceptable heading error
NUM_SIDES    = 4     # a square has 4 sides

# ── Module-level state ─────────────────────────────────────────────────────────────
_leg         = 0     # current leg number (0 – NUM_SIDES-1)
_phase       = 0     # 0 = flying forward, 1 = turning right
_timer       = 0.0
_target_yaw  = 0.0   # heading to turn to after each leg
_done        = False

# ──────────────────────────────────────────────────────────────────────────────────

def reset():
    global _leg, _phase, _timer, _target_yaw, _done
    _leg        = 0
    _phase      = 0
    _timer      = 0.0
    _target_yaw = 0.0
    _done       = False


def _yaw_error(target, current):
    return ((target - current) + 180) % 360 - 180


def update(drone):
    """
    Loop NUM_SIDES times: fly forward → turn right.
    Returns True when the square is complete.
    """
    global _leg, _phase, _timer, _target_yaw, _done
    if _done:
        return True

    if _leg >= NUM_SIDES:
        drone.flight.stop()
        print(f"[Challenge 1] Square complete! Flew {NUM_SIDES} legs.")
        _done = True
        return True

    if _phase == 0:   # ── Fly forward ────────────────────────────────────────────
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Hint: send forward PCMD (FLY_SPEED pitch)
        # Increment _timer by delta_time
        # When _timer >= LEG_DURATION:
        #     compute _target_yaw = (current_heading - 90) % 360
        #     set _phase = 1, reset _timer
        #     print progress message

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:  # ── Turn right ─────────────────────────────────────────────
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Hint: current = drone.physics.get_attitude()[1] % 360
        #       error   = _yaw_error(_target_yaw, current)
        # If |error| < YAW_THRESHOLD → stop, _leg += 1, _phase = 0, _timer = 0.0
        # Else → yaw_cmd = max(-YAW_SPEED, min(YAW_SPEED, error / 45.0))
        #        drone.flight.send_pcmd(0, 0, yaw_cmd, 0)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return False


# ── Standalone runner ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    _drone = drone_core.create_drone()
    _phase_main = 0

    def start():
        global _phase_main
        _phase_main = 0
        reset()
        print("Challenge 1: Fly a Square")

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
