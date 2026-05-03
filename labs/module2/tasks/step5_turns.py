"""
Step 5 — Turns
Rotate the drone to specific headings using yaw feedback control.

Heading convention (verify in your scene):
    0°  / 360° = forward (East / +X world axis)
    90°         = left   (North / +Y world axis)
    180°        = backward
    270°        = right  (South / -Y world axis)

Your task:
    For each (target_heading, pause, label) in TURN_SEQUENCE:
        Phase 0 — Turning:
            Compute shortest-path error = ((target - current) + 180) % 360 - 180
            If |error| < THRESHOLD → stop, print, advance to pause phase
            Else → send yaw PCMD proportional to error
        Phase 1 — Pausing:
            Stop and wait pause_sec seconds, then advance to next turn
"""

import drone_core

# ── Turn sequence: list of (target_heading_deg, pause_seconds, label) ─────────────
TURN_SEQUENCE = [
    (90,  1.5, "Turn Left 90°  → face North"),
    (180, 1.5, "Turn Left 90°  → face South (180°)"),
    (270, 1.5, "Turn Right 90° → face West  (270°)"),
    (0,   1.5, "Return to forward (0°)"),
]

YAW_SPEED  = 0.5   # PCMD yaw magnitude
THRESHOLD  = 3.0   # degrees — acceptable heading error

# ── Module-level state ─────────────────────────────────────────────────────────────
_turn_index  = 0
_phase       = 0   # 0=turning, 1=pausing
_pause_timer = 0.0
_done        = False

# ──────────────────────────────────────────────────────────────────────────────────

def reset():
    global _turn_index, _phase, _pause_timer, _done
    _turn_index  = 0
    _phase       = 0
    _pause_timer = 0.0
    _done        = False


def _shortest_yaw_error(target, current):
    """Return signed error (degrees) using the shortest rotation direction."""
    return ((target - current) + 180) % 360 - 180


def update(drone):
    """
    Execute each turn in TURN_SEQUENCE, pausing briefly after each.
    Returns True when all turns are complete.
    """
    global _turn_index, _phase, _pause_timer, _done
    if _done:
        return True

    if _turn_index >= len(TURN_SEQUENCE):
        _done = True
        print("[Step 5] All turns complete!")
        return True

    target_deg, pause_sec, label = TURN_SEQUENCE[_turn_index]

    if _phase == 0:   # ── Turning phase ──────────────────────────────────────────
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Hint: current = drone.physics.get_attitude()[1] % 360
        #       error   = _shortest_yaw_error(target_deg, current)
        # If |error| < THRESHOLD → stop, print label, set _phase = 1, reset _pause_timer
        # Else → yaw_cmd = max(-YAW_SPEED, min(YAW_SPEED, error / 45.0))
        #        drone.flight.send_pcmd(0, 0, yaw_cmd, 0)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:  # ── Pause phase ───────────────────────────────────────────
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Hint: stop, increment _pause_timer by delta_time
        # When _pause_timer >= pause_sec → _turn_index += 1, _phase = 0

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
        print("Step 5: Turns")

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
