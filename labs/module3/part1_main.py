"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0
Title: Computer Vision — Object Detection
Python Topics: If/Else, Functions
Drone Topic: Camera, colour detection, move to target

Expected Outcome:
    1. Drone takes off and climbs to search altitude
    2. Camera scans for the red target object
    3. Drone flies forward toward the object, keeping it centred
    4. Drone hovers next to the object and lands
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../library'))
sys.path.insert(0, os.path.join(_HERE, '..'))

import drone_core
from part1_tasks import step1_positioning, step2_find_object, step3_move_forward

drone = drone_core.create_drone()

_TASKS = [
    ("Step 1: Positioning",    step1_positioning),
    ("Step 2: Find Object",    step2_find_object),
    ("Step 3: Move to Object", step3_move_forward),
]
_task_index = 0
_land_timer = 0.0
_landing    = False

def start():
    global _task_index, _land_timer, _landing
    _task_index = 0; _land_timer = 0.0; _landing = False
    _TASKS[0][1].reset()
    print("\n=== Module 3 Part 1: Object Detection ===\n")

def update():
    global _task_index, _land_timer, _landing

    if _landing:
        _land_timer += drone.get_delta_time()
        if _land_timer < 2.0:
            drone.flight.stop()
        else:
            drone.flight.land()
        return

    if _task_index >= len(_TASKS):
        _landing = True
        print("=== Part 1 Complete! Landing… ===")
        return

    name, task = _TASKS[_task_index]
    if task.update(drone):
        _task_index += 1
        if _task_index < len(_TASKS):
            _TASKS[_task_index][1].reset()
            print(f"\n─── {_TASKS[_task_index][0]} ───\n")

def update_slow():
    print(f"Alt={drone.physics.get_altitude():.2f}m | "
          f"Task={_TASKS[min(_task_index, len(_TASKS)-1)][0]}")

if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
