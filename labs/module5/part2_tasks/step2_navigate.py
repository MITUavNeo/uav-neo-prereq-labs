"""Module 5 Part 2 — Step 2: Navigate Easy Maze
Hard-coded turn sequence for the easy corridor maze.

Sequence: fly to wall → turn left → fly to wall → turn right → fly to wall → done

The drone uses its forward-facing depth camera to measure the distance ahead.
When the distance falls below STOP_DISTANCE, the drone stops and executes the
next turn in the sequence before continuing forward.

Your task:
    Phase 0 (fly): Fly forward with FLY_SPEED. When front <= STOP_DISTANCE:
        - Stop
        - If all turns done → set _done = True, return True
        - Else: read current heading, compute _target_yaw for next turn, _phase = 1
    Phase 1 (turn): Compute yaw error = ((target - current) + 180) % 360 - 180
        When |err| < YAW_THRESH → stop, _phase = 0
        Else → yaw_cmd = clamp(err / 45.0, -YAW_SPEED, YAW_SPEED)
               drone.flight.send_pcmd(0, 0, yaw_cmd, 0)

    Turn directions in TURN_SEQUENCE: 'L' = CCW = add 90°, 'R' = CW = subtract 90°.
"""

import drone_core, drone_utils as uav_utils

STOP_DISTANCE = 1.2; FLY_SPEED = 0.35; YAW_SPEED = 0.5; YAW_THRESH = 3.0
MAX_RANGE = 10.0

# Turn sequence: list of (direction, degrees)  — 'L'=left (CCW), 'R'=right (CW)
TURN_SEQUENCE = [('L', 90), ('R', 90)]

_step        = 0    # which turn we are on
_phase       = 0    # 0=fly, 1=turn
_target_yaw  = 0.0
_done        = False

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
        # Hint: use the depth camera to measure the distance ahead
        # front = _get_front(drone)
        # if front <= STOP_DISTANCE:
        #     drone.flight.stop()
        #     if _step >= len(TURN_SEQUENCE): _done = True; return True
        #     d, deg = TURN_SEQUENCE[_step]
        #     cur = drone.physics.get_attitude()[1] % 360
        #     sign = 1 if d == 'L' else -1
        #     _target_yaw = (cur + sign * deg) % 360
        #     _phase = 1; _step += 1
        # else:
        #     drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # err = _yaw_error(_target_yaw, drone.physics.get_attitude()[1] % 360)
        # if |err| < YAW_THRESH → stop, _phase = 0
        # else → yaw_cmd = max(-YAW_SPEED, min(YAW_SPEED, err / 45.0))
        #         drone.flight.send_pcmd(0, 0, yaw_cmd, 0)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return False
