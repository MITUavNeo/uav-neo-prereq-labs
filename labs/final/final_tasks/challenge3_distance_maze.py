"""Final Challenge 3 — Distance Maze (Right-Hand Rule)
Navigate an unknown maze using the right-hand-rule algorithm with the depth camera.

Since the depth camera only sees straight ahead, the drone must periodically turn
right to check for openings, then turn back to continue forward.

    Phase 0 (fly forward):
        Fly forward. Check front distance each frame.
        - If front <= STOP_DISTANCE → wall ahead, turn LEFT 90° (_phase = 1).
        - Every CHECK_INTERVAL seconds → stop, turn right to look (_phase = 2).
        - Otherwise → keep flying forward.
    Phase 1 (execute turn):
        Yaw to _target_yaw. When aligned → _nudge_timer = 0, _phase = 3.
    Phase 2 (look right):
        Turn 90° right. When aligned → read depth camera.
        If right_dist > RIGHT_OPEN_THRES → passage open! Stay facing right, _phase = 3.
        Else → turn back to forward heading, _phase = 1.
    Phase 3 (post-turn advance):
        Fly forward 0.8s to clear the corner, then _phase = 0.

Safety: stop after MAX_TURNS turns and return True.

Your task:
    Implement reset() and update() below.
    (Same algorithm as Module 5 Part 4.)
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../../library'))
import drone_core
import drone_utils as uav_utils

STOP_DISTANCE    = 1.2    # m — stop flying when this close to a wall
RIGHT_OPEN_THRES = 4.0    # m — right side "open" if camera sees this far
CHECK_INTERVAL   = 1.5    # s — peek right this often while flying forward
FLY_SPEED        = 0.35
YAW_SPEED        = 0.5
YAW_THRESH       = 3.0
MAX_RANGE        = 10.0
MAX_TURNS        = 50     # safety: declare done after this many turns

_phase        = 0
_forward_yaw  = 0.0
_target_yaw   = 0.0
_front_dist   = MAX_RANGE
_right_dist   = MAX_RANGE
_check_timer  = 0.0
_nudge_timer  = 0.0
_turn_count   = 0
_done         = False


def reset():
    global _phase, _forward_yaw, _target_yaw, _front_dist, _right_dist
    global _check_timer, _nudge_timer, _turn_count, _done
    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE — reset all state variables to their initial values

    ###### END PUT CODE HERE #########
    ##################################


def _get_front(drone):
    return min(uav_utils.get_depth_image_center_distance(drone.camera.get_depth_image()) / 100, MAX_RANGE)


def _yaw_err(t, c):
    return ((t - c) + 180) % 360 - 180


def update(drone):
    """
    Apply right-hand-rule every frame using the depth camera (turn-to-look).
    Returns True when MAX_TURNS is exhausted (maze exit reached).

    Hints (Phase 0 — fly + tick timer):
        _front_dist = _get_front(drone)
        _check_timer += drone.get_delta_time()
        if _front_dist <= STOP_DISTANCE or _check_timer >= CHECK_INTERVAL:
            stop; _check_timer = 0.0
            _forward_yaw = drone.physics.get_attitude()[1] % 360
            _target_yaw  = (_forward_yaw - 90) % 360   # CW = look right
            _phase = 1
        else: send_pcmd(FLY_SPEED, 0, 0, 0)

    Hints (Phase 1 — turn right to look):
        err = _yaw_err(_target_yaw, cur)
        if |err| < YAW_THRESH:
            stop; _right_dist = _get_front(drone); _target_yaw = _forward_yaw; _phase = 2
        else: yaw PCMD

    Hints (Phase 2 — turn back to _forward_yaw, then apply RHR):
        err = _yaw_err(_forward_yaw, cur)
        if |err| < YAW_THRESH:
            stop
            if _right_dist > RIGHT_OPEN_THRES:          # right open → turn right
                _turn_count += 1; print(...)
                _forward_yaw = (_forward_yaw - 90) % 360
                _target_yaw = _forward_yaw; _nudge_timer = 0.0; _phase = 3
            elif _front_dist <= STOP_DISTANCE:           # wall ahead → turn left
                if _turn_count >= MAX_TURNS: _done = True; return True
                _turn_count += 1; print(...)
                _forward_yaw = (_forward_yaw + 90) % 360
                _target_yaw = _forward_yaw; _nudge_timer = 0.0; _phase = 3
            else: _phase = 0                             # clear → resume flying
        else: yaw PCMD

    Hints (Phase 3 — turn to new heading + advance 0.8 s):
        err = _yaw_err(_target_yaw, cur)
        if |err| >= YAW_THRESH: yaw PCMD
        else:
            send_pcmd(FLY_SPEED, 0, 0, 0)
            _nudge_timer += dt
            if _nudge_timer >= 0.8: _nudge_timer = 0.0; _phase = 0
    """
    global _phase, _forward_yaw, _target_yaw, _front_dist, _right_dist
    global _check_timer, _nudge_timer, _turn_count, _done
    if _done:
        return True

    if _phase == 0:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 2:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 3:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return _done
