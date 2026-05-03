"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

Title: Module 1 — Hello Drone (Pattern Menu)
Python Topics: Functions, conditionals, state machines, button-triggered control
Drone Topic: Semi-autonomous flight — pick a pre-programmed pattern with a button

Purpose:
    Build on hello_drone.py (auto takeoff/hover/land) by letting you trigger
    one of four pre-programmed flight patterns with the controller:

        Press A (key '1') → Zigzag    (left ↔ right while flying forward)
        Press B (key '2') → Spiral    (constant forward + constant yaw)
        Press X (key '3') → Hallway   (forward 5m, turn 180°, return)
        Press Y (key '4') → Maze      (forward → right → forward → left)

    Press LB (key '5') to land at any time.

    The orchestrator below is provided complete; your work is in the four
    pattern files under module1/tasks/.

How to run:
    drone sim labs/module1/main.py
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../library'))
sys.path.insert(0, os.path.join(_HERE, '..'))
import drone_core

from tasks import pattern_zigzag, pattern_spiral, pattern_hallway, pattern_maze

drone = drone_core.create_drone()

# ── State ────────────────────────────────────────────────────────────────
_state = "TAKING_OFF"
_phase_timer = 0.0
TAKEOFF_WAIT  = 3.5
HOVER_ALT     = 1.5

_active_pattern      = None
_active_pattern_name = None
_PATTERNS = None


def start():
    global _state, _phase_timer, _active_pattern, _active_pattern_name, _PATTERNS
    _state = "TAKING_OFF"
    _phase_timer = 0.0
    _active_pattern = None
    _active_pattern_name = None

    Button = drone.controller.Button
    _PATTERNS = {
        Button.A: ("Zigzag",  pattern_zigzag),
        Button.B: ("Spiral",  pattern_spiral),
        Button.X: ("Hallway", pattern_hallway),
        Button.Y: ("Maze",    pattern_maze),
    }

    print("\n=== Module 1: Pattern Menu ===")
    print("Buttons:  A=Zigzag  B=Spiral  X=Hallway  Y=Maze   |   LB=Land")
    print("(keys:    1        2         3          4         5)\n")
    print("Taking off…")


def update():
    global _state, _phase_timer, _active_pattern, _active_pattern_name

    Button = drone.controller.Button
    _phase_timer += drone.get_delta_time()

    if _state in ("HOVERING", "RUNNING_PATTERN") and drone.controller.was_pressed(Button.LB):
        print("LB pressed — landing.")
        _state = "LANDING"
        _phase_timer = 0.0

    if _state == "TAKING_OFF":
        drone.flight.takeoff()
        if _phase_timer >= TAKEOFF_WAIT:
            _state = "HOVERING"
            _phase_timer = 0.0
            print("Hovering. Press a pattern button.")

    elif _state == "HOVERING":
        err = HOVER_ALT - drone.physics.get_altitude()
        throttle = max(-0.5, min(0.5, err * 2.5))
        drone.flight.send_pcmd(0, 0, 0, throttle)

        for button, (name, task) in _PATTERNS.items():
            if drone.controller.was_pressed(button):
                print(f"\n─── Running pattern: {name} ───")
                task.reset()
                _active_pattern = task
                _active_pattern_name = name
                _state = "RUNNING_PATTERN"
                break

    elif _state == "RUNNING_PATTERN":
        if _active_pattern.update(drone):
            print(f"─── {_active_pattern_name} complete. Hovering. ───\n")
            _active_pattern = None
            _active_pattern_name = None
            _state = "HOVERING"

    elif _state == "LANDING":
        drone.flight.land()


def update_slow():
    alt = drone.physics.get_altitude()
    if _state == "RUNNING_PATTERN":
        print(f"  [{_active_pattern_name}] alt={alt:.2f}m")
    else:
        print(f"  [{_state.lower()}] alt={alt:.2f}m")


if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
