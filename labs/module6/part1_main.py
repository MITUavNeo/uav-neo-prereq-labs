"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

Title: Module 6 Part 1 — Line Following
Python Topics: If/Else, Functions, Proportional Control
Drone Topic: Downward camera, colour thresholding, closed-loop steering

Expected Outcome:
    1. Drone takes off and climbs to line-following altitude (1.2 m)
    2. Drone hovers and confirms it can see the red line below
    3. Drone flies forward along the red line, correcting left/right to stay centred
    4. After RUN_DURATION seconds the drone stops and lands

Scene: Module6_LineFollowing
    Open this scene in the UAV Neo simulator before running the script.
    The track is a closed rectangular circuit (~56 m × 66 m) marked with red line
    segments. The drone spawns at the start/finish line facing north.

How to run:
    drone sim labs/module6/part1_main.py
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..'))

import drone_core
import drone_utils as uav_utils
from part1_tasks import step1_init, step2_detect_line, step3_follow_line

drone = drone_core.create_drone()

_TASKS = [
    ("Init",          step1_init),
    ("Detect Line",   step2_detect_line),
    ("Follow Line",   step3_follow_line),
]
_task_index = 0
_land_timer = 0.0
_landing    = False


def start():
    global _task_index, _land_timer, _landing
    _task_index = 0; _land_timer = 0.0; _landing = False
    _TASKS[0][1].reset()
    print("\n=== Module 6 Part 1: Line Following ===\n")
    print(f"─── {_TASKS[0][0]} ───\n")


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
        print("\n=== Module 6 Part 1 Complete! Landing… ===")
        return

    name, task = _TASKS[_task_index]
    if task.update(drone):
        _task_index += 1
        if _task_index < len(_TASKS):
            _TASKS[_task_index][1].reset()
            print(f"\n─── {_TASKS[_task_index][0]} ───\n")


def update_slow():
    image = drone.camera.get_downward_image()
    contours1 = uav_utils.find_contours(
        image, step2_detect_line.LINE_LOWER, step2_detect_line.LINE_UPPER)
    contours2 = uav_utils.find_contours(
        image, step2_detect_line.LINE_LOWER2, step2_detect_line.LINE_UPPER2)
    best = uav_utils.get_largest_contour(
        contours1 + contours2, step2_detect_line.MIN_AREA)

    if best is not None:
        cx, cy = uav_utils.get_contour_center(best)   # (row, column)
        err = (cy - 320) / 320
        print(f"Alt={drone.physics.get_altitude():.2f}m | "
              f"line_col={cy} | lateral_err={err:+.2f} | "
              f"task={_TASKS[min(_task_index, len(_TASKS)-1)][0]}")
    else:
        print(f"Alt={drone.physics.get_altitude():.2f}m | "
              f"line=NOT FOUND | "
              f"task={_TASKS[min(_task_index, len(_TASKS)-1)][0]}")


if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
