"""Module 5 Part 3 — Step 3: Detect Left Opening
Fly forward and periodically turn left to check for an opening.

The drone uses its depth camera to measure distance. Since the camera only
sees straight ahead, the drone must turn to look left, read the distance,
then turn back to continue flying forward.

Strategy:
    Phase 0 (fly + check):
        Fly forward. Every CHECK_INTERVAL seconds, stop and enter Phase 1.
        If front distance <= STOP_DISTANCE → stop, hit wall, _done = True.
    Phase 1 (turn left to look):
        Turn 90° left (CCW). When aligned, read depth camera center distance.
        If left_dist > opening_threshold → opening found! Stay facing left, _phase = 3.
        Else → save heading, _phase = 2 (turn back).
    Phase 2 (turn back to forward):
        Turn back to the original heading. When aligned → _phase = 0.
    Phase 3 (nudge forward into opening):
        Fly forward for 1.0s, then stop and enter Phase 4.
    Phase 4 (fly to next wall):
        Fly forward until front <= STOP_DISTANCE → stop, _done = True.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core, drone_utils as uav_utils

STOP_DISTANCE   = 1.2
OPENING_FACTOR  = 1.5   # left_dist > corridor_width * factor → opening found
CHECK_INTERVAL  = 0.8   # seconds between left-checks while flying
FLY_SPEED       = 0.35
YAW_SPEED       = 0.5; YAW_THRESH = 3.0
MAX_RANGE       = 10.0

_phase = 0; _corridor_width = 3.0; _target_yaw = 0.0
_forward_yaw = 0.0; _nudge_timer = 0.0; _check_timer = 0.0; _done = False

def reset(corridor_width=3.0):
    global _phase, _corridor_width, _target_yaw, _forward_yaw
    global _nudge_timer, _check_timer, _done
    _phase = 0; _corridor_width = corridor_width
    _target_yaw = 0.0; _forward_yaw = 0.0
    _nudge_timer = 0.0; _check_timer = 0.0; _done = False

def _get_front(drone):
    return min(uav_utils.get_depth_image_center_distance(drone.camera.get_depth_image()) / 100, MAX_RANGE)

def _yaw_err(t, c): return ((t-c)+180)%360-180

def update(drone):
    global _phase, _target_yaw, _forward_yaw, _nudge_timer, _check_timer, _done
    if _done: return True

    dt = drone.get_delta_time()

    if _phase == 0:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Fly forward. Track _check_timer += dt.
        # Check front distance each frame: if front <= STOP_DISTANCE → stop, _done = True.
        # When _check_timer >= CHECK_INTERVAL:
        #     stop, save _forward_yaw = current heading
        #     set _target_yaw = (_forward_yaw + 90) % 360 to look left
        #     _check_timer = 0; _phase = 1
        # Otherwise: drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Turn to _target_yaw (left). When aligned:
        #     Read depth camera: left_dist = _get_front(drone)
        #     opening_threshold = _corridor_width * OPENING_FACTOR
        #     If left_dist > opening_threshold → opening found!
        #         Print message, _phase = 3, _nudge_timer = 0
        #     Else → _target_yaw = _forward_yaw, _phase = 2 (turn back)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 2:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Turn back to _forward_yaw. When aligned → stop, _phase = 0

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 3:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Nudge forward: drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)
        # _nudge_timer += dt. After 1.0s → _phase = 4

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 4:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Read front distance. If front <= STOP_DISTANCE → stop, print complete, _done = True
        # Else → fly forward

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return _done
