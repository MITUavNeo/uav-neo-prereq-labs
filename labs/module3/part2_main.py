"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0
Title: Computer Vision — ArUco Maze
Python Topics: If/Else, Functions
Drone Topic: ArUco marker detection, fake vs real walls

Expected Outcome:
    1. Drone takes off and faces forward at marker height
    2. Loop: detect ArUco marker → decide action:
         ID=0 (fake)  → fly straight through
         ID=1 (real)  → turn right 90° and advance
         ID=2 (end)   → maze complete, land
    3. Drone lands after exiting the maze
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..'))

import drone_core
from part2_tasks import step1_init, step3_loop

drone = drone_core.create_drone()

_phase      = 0   # 0=init, 1=maze_loop, 2=landing
_land_timer = 0.0

def start():
    global _phase, _land_timer
    _phase = 0; _land_timer = 0.0
    step1_init.reset()
    step3_loop.reset()
    print("\n=== Module 3 Part 2: ArUco Maze ===\n")

def update():
    global _phase, _land_timer

    if _phase == 0:
        if step1_init.update(drone):
            _phase = 1
            print("\n─── Maze Loop Active ───\n")

    elif _phase == 1:
        if step3_loop.update(drone):
            _phase = 2
            print("\n=== Maze Complete! Landing… ===\n")

    elif _phase == 2:
        _land_timer += drone.get_delta_time()
        if _land_timer < 2.0:
            drone.flight.stop()
        else:
            drone.flight.land()

def update_slow():
    print(f"Alt={drone.physics.get_altitude():.2f}m | Phase={_phase}")

if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
