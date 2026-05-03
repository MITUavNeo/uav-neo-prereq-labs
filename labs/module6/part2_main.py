"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

Title: Module 6 Part 2 — Lap Counter
Python Topics: State machines, modular arithmetic, performance measurement
Drone Topic: Closed-loop steering, heading-based state tracking

Expected Outcome:
    1. Drone takes off and climbs to line-following altitude (1.2 m)
    2. Drone detects the red line below
    3. Drone follows the red line for RACE_DURATION seconds, counting laps
       - A lap is one full circuit: N → E → S → W → N
       - Each lap completion is printed with its elapsed time
    4. Drone stops and lands; total laps and average lap time are reported

Scene: Module6_LineFollowing
    Open this scene before running. The track is the F1-style 8-corner circuit.
    The drone spawns at the start/finish line facing north.

How to run:
    drone sim labs/module6/part2_main.py
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../library'))
sys.path.insert(0, os.path.join(_HERE, '..'))

import drone_core
import drone_utils as uav_utils
from part1_tasks import step1_init, step2_detect_line
from part2_tasks import step2_lap_follow

drone = drone_core.create_drone()

_TASKS = [
    ("Init",            step1_init),
    ("Detect Line",     step2_detect_line),
    ("Follow & Count",  step2_lap_follow),
]
_task_index = 0
_land_timer = 0.0
_landing    = False


def start():
    global _task_index, _land_timer, _landing
    _task_index = 0; _land_timer = 0.0; _landing = False
    _TASKS[0][1].reset()
    print("\n=== Module 6 Part 2: Lap Counter ===\n")
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
        print("\n=== Module 6 Part 2 Complete! Landing… ===")
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

    roll, pitch, yaw = drone.physics.get_attitude()
    lap = step2_lap_follow._lap_count

    if best is not None:
        cx, cy = uav_utils.get_contour_center(best)
        err = (cy - 320) / 320
        print(f"Alt={drone.physics.get_altitude():.2f}m | "
              f"line_col={cy} | err={err:+.2f} | "
              f"yaw={yaw:.0f}° | lap={lap}")
    else:
        print(f"Alt={drone.physics.get_altitude():.2f}m | "
              f"line=NOT FOUND | yaw={yaw:.0f}° | lap={lap}")


if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
