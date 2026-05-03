"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

Title: Module 5 Part 4 — Right-Hand Rule Maze Solver
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..'))
import drone_core
from part4_tasks import step1_init, step2_right_hand_rule, step3_exit

drone = drone_core.create_drone()
_TASKS = [
    ("Init",              step1_init),
    ("Right-Hand Rule",   step2_right_hand_rule),
    ("Exit Maze",         step3_exit),
]
_task_index = 0

def start():
    global _task_index
    _task_index = 0; _TASKS[0][1].reset()
    print("\n=== Module 5 Part 4: Right-Hand Rule ===\n")

def update():
    global _task_index
    if _task_index >= len(_TASKS):
        drone.flight.land(); return
    if _TASKS[_task_index][1].update(drone):
        _task_index += 1
        if _task_index < len(_TASKS):
            _TASKS[_task_index][1].reset()
            print(f"\n─── {_TASKS[_task_index][0]} ───\n")

def update_slow():
    import drone_utils as uav_utils
    f = uav_utils.get_depth_image_center_distance(drone.camera.get_depth_image()) / 100
    print(f"Front={f:.2f}m | Alt={drone.physics.get_altitude():.2f}m")

if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
