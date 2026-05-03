"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

Title: Module 5 Part 1 — Fly to Wall (intro to depth camera distance sensing)
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../library'))
sys.path.insert(0, os.path.join(_HERE, '..'))
import drone_core, drone_utils as uav_utils
from part1_tasks import step1_init, step2_sensors, step3_fly_to_wall

drone = drone_core.create_drone()
_TASKS = [("Init", step1_init), ("Read Sensors", step2_sensors), ("Fly to Wall", step3_fly_to_wall)]
_task_index = 0

def start():
    global _task_index
    _task_index = 0; _TASKS[0][1].reset()
    print("\n=== Module 5 Part 1: Fly to Wall ===\n")

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
    depth_image = drone.camera.get_depth_image()
    f = uav_utils.get_depth_image_center_distance(depth_image) / 100
    print(f"Front={f:.2f}m | Alt={drone.physics.get_altitude():.2f}m")

if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
