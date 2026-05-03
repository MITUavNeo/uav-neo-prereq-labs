"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

Title: Module 0 Part 1 — Python + Callback Primer
Python Topics: Print statements, f-strings, variables, simple math
Drone Topic: The start / update / update_slow callback lifecycle (no flight)

Author: [PLACEHOLDER] << Write your name here

Purpose:
    Introduce the drone control paradigm before flying anything. Learn how
    the THREE callback functions get called at different rates:
        start()       — once when the program begins
        update()      — every frame (~60 fps)
        update_slow() — once per second
    The drone stays grounded the whole time — drone.flight.stop() is called
    every frame so nothing takes off.

Expected Outcome:
    1. start()        — prints once at the beginning
    2. update()       — prints a counter every frame, scrolls fast
    3. update_slow()  — prints a tidy summary once per second

How to run:
    drone sim labs/module0/part1_python.py
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../library'))
import drone_core

drone = drone_core.create_drone()

# Variables we'll update every frame
_frame_count = 0
_total_time  = 0.0


def start():
    """Called ONCE, when the simulator starts the script."""
    global _frame_count, _total_time

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Hint: zero out _frame_count and _total_time, then print a welcome banner.

    ###### END PUT CODE HERE #########
    ##################################


def update():
    """Called EVERY FRAME (~60 times per second)."""
    global _frame_count, _total_time

    drone.flight.stop()   # keep the drone grounded

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Hint:
    #   1) Increment _frame_count by 1.
    #   2) Read dt = drone.get_delta_time() and add it to _total_time.
    #   3) Print a one-line message that includes _frame_count and dt.
    #      Use an f-string. e.g. print(f"frame {_frame_count}, dt={dt:.4f}s")

    ###### END PUT CODE HERE #########
    ##################################


def update_slow():
    """Called ONCE PER SECOND — useful for debug / status."""

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Hint: compute average fps = _frame_count / _total_time (guard against
    # division by zero). Print a one-line summary every second.

    ###### END PUT CODE HERE #########
    ##################################


if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
