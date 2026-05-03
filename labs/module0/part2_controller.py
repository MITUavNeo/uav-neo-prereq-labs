"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

Title: Module 0 Part 2 — Controller Polling
Python Topics: Conditionals, function calls
Drone Topic: Reading button input — event-driven vs state-driven (no flight)

Author: [PLACEHOLDER] << Write your name here

Purpose:
    Learn the THREE ways to ask "what's the controller doing?":
        was_pressed(button)   — True for ONE frame on the press
        was_released(button)  — True for ONE frame on the release
        is_down(button)       — True for EVERY frame the button is held

    Picking the wrong one is a common bug:
      • Use was_pressed() for "do this once when the button is hit"
        (e.g. fire a missile, take off the drone)
      • Use is_down() for "do this continuously while held"
        (e.g. accelerate a car, hold an arm raised)

Controller mapping in the simulator:
    A button = '1' key on keyboard       LB = '5' key
    B button = '2' key on keyboard       RB = '6' key
    X button = '3' key on keyboard
    Y button = '4' key on keyboard

Expected Outcome:
    Press 1 once   → "A pressed!" once
    Hold 1         → "A pressed!" once, then update_slow lists A as held
    Release 1      → "A released!" once
    Hold 3 (X)     → spam "X held" every frame while held

How to run:
    drone sim labs/module0/part2_controller.py
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../library'))
import drone_core

drone = drone_core.create_drone()

# Track totals so update_slow can show a summary
_a_press_count = 0
_b_press_count = 0


def start():
    global _a_press_count, _b_press_count
    _a_press_count = 0
    _b_press_count = 0
    print("=== Module 0 Part 2: Controller Polling ===")
    print("Press '1' for A, '2' for B, '3' for X, '4' for Y in the sim window.\n")


def update():
    """Demonstrate event-driven (was_pressed/was_released) vs state-driven (is_down)."""
    global _a_press_count, _b_press_count

    drone.flight.stop()   # don't fly

    Button = drone.controller.Button

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    #
    # 1) If A was pressed this frame, increment _a_press_count and print it.
    #    Hint: drone.controller.was_pressed(Button.A)
    #
    # 2) If A was released this frame, print "A released!".
    #    Hint: drone.controller.was_released(Button.A)
    #
    # 3) If B was pressed, increment _b_press_count and print it.
    #
    # 4) (Demonstrate the noisy version!) If X is currently down (held), print
    #    a message EVERY frame. Hint: drone.controller.is_down(Button.X).
    #    You'll see how is_down floods the terminal vs the cleaner was_pressed.

    ###### END PUT CODE HERE #########
    ##################################


def update_slow():
    """Once per second — show held-state of buttons via is_down()."""
    Button = drone.controller.Button

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Hint: build a list of button names that are currently held using
    # drone.controller.is_down(Button.X) for X in {A, B, Y, LB, RB}.
    # Print the list, or a "(none)" message + totals if no buttons are held.

    ###### END PUT CODE HERE #########
    ##################################


if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
