"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

File Name: main.py
Title: Module 2 — Drone Control (Main Orchestrator)
Python Topics: Lists, While/For Loops
Drone Topic: Drone Control (altitude, position, turns, velocity, gates)

Purpose:
    Runs all Module 2 steps in sequence.
    Each step is defined in its own file under module2/tasks/.
    Run individual steps by executing them directly:
        drone sim module2/tasks/step1_takeoff.py
    Run the full sequence:
        drone sim module2/main.py
"""

########################################################################################
# Imports
########################################################################################

import sys
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../library'))
sys.path.insert(0, os.path.join(_HERE, '..'))   # for neo_helpers

import drone_core

# Import all task modules
from tasks import (
    step1_takeoff,
    step2_altitude,
    step3_absolute,
    step4_relative,
    step5_turns,
    step6_velocity,
    challenge1_square,
    challenge2_gates,
    challenge3_altitude_gates,
)

########################################################################################
# Global variables
########################################################################################

drone = drone_core.create_drone()

# ── Task sequencer ─────────────────────────────────────────────────────────────────
_TASKS = [
    ("Step 1: Takeoff",          step1_takeoff),
    ("Step 2: Altitude Control", step2_altitude),
    ("Step 3: Absolute Position",step3_absolute),
    ("Step 4: Relative Position",step4_relative),
    ("Step 5: Turns",            step5_turns),
    ("Step 6: Velocity",         step6_velocity),
    ("Challenge 1: Square",      challenge1_square),
    ("Challenge 2: Gates",           challenge2_gates),
    ("Challenge 3: Altitude Gates",  challenge3_altitude_gates),
]

_task_index = 0

########################################################################################
# Functions
########################################################################################

def start():
    global _task_index
    _task_index = 0
    _TASKS[0][1].reset()
    print(f"\n{'='*50}")
    print(f"  Module 2 — Drone Control")
    print(f"  Running: {_TASKS[0][0]}")
    print(f"{'='*50}\n")


def update():
    global _task_index
    if _task_index >= len(_TASKS):
        drone.flight.land()
        return

    name, task = _TASKS[_task_index]
    done = task.update(drone)

    if done:
        _task_index += 1
        if _task_index < len(_TASKS):
            next_name = _TASKS[_task_index][0]
            _TASKS[_task_index][1].reset()
            print(f"\n─── {next_name} ───\n")
        else:
            print("\n=== Module 2 Complete! Landing… ===\n")


def update_slow():
    if _task_index < len(_TASKS):
        print(f"[{_TASKS[_task_index][0]}] alt={drone.physics.get_altitude():.2f}m")


########################################################################################
# DO NOT MODIFY: Register callbacks and begin execution
########################################################################################

if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
