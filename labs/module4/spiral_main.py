"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0
Title: Search & Rescue — Spiral Pattern
Python Topics: Classes, Architecture
Drone Topic: Autonomous search, spiral pattern, landing on target
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..'))
import drone_core
from spiral_tasks import step1_setup, step3_search_loop, step4_land

drone = drone_core.create_drone()
_TASKS = [("Setup", step1_setup), ("Spiral Search", step3_search_loop), ("Land on Target", step4_land)]
_task_index = 0

def start():
    global _task_index
    _task_index = 0
    _TASKS[0][1].reset()
    print("\n=== Module 4: Spiral Search & Rescue ===\n")

def update():
    global _task_index
    if _task_index >= len(_TASKS):
        drone.flight.land(); return
    _, task = _TASKS[_task_index]
    if task.update(drone):
        _task_index += 1
        if _task_index < len(_TASKS):
            _TASKS[_task_index][1].reset()
            print(f"\n─── {_TASKS[_task_index][0]} ───\n")

def update_slow():
    name = _TASKS[min(_task_index, len(_TASKS)-1)][0]
    print(f"[{name}] alt={drone.physics.get_altitude():.2f}m")

if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
