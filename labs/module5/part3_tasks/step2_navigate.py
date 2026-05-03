"""Module 5 Part 3 — Step 2: Navigate Hard Maze (known turns)
Hard-coded 6-turn sequence for the hard maze: L R R L R R

Uses the depth camera to measure the distance ahead. The drone flies forward
until close to a wall, then executes the next turn in the sequence.

Your task:
    Same structure as Part 2 step2_navigate but with a longer TURN_SEQUENCE.
    Phase 0: fly to wall (depth camera). Phase 1: execute turn. Repeat until all turns done.
"""

import drone_core, drone_utils as uav_utils

STOP_DISTANCE = 1.2; FLY_SPEED = 0.4; YAW_SPEED = 0.5; YAW_THRESH = 3.0
MAX_RANGE = 10.0

TURN_SEQUENCE = [('L',90),('R',90),('R',90),('L',90),('R',90),('R',90)]

_step = 0; _phase = 0; _target_yaw = 0.0; _done = False

def reset():
    global _step, _phase, _target_yaw, _done
    _step = 0; _phase = 0; _target_yaw = 0.0; _done = False

def _get_front(drone):
    return min(uav_utils.get_depth_image_center_distance(drone.camera.get_depth_image()) / 100, MAX_RANGE)

def _yaw_error(t, c):
    return ((t - c) + 180) % 360 - 180

def update(drone):
    global _step, _phase, _target_yaw, _done
    if _done: return True

    if _phase == 0:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Same as Part 2 step2_navigate.
        # Use _get_front(drone) to read the depth camera distance ahead.
        # Fly forward until front <= STOP_DISTANCE, then turn using TURN_SEQUENCE[_step].

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Yaw to _target_yaw. When aligned → _phase = 0

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return False
