"""Module 5 Part 4 — Step 2: Right-Hand Rule Maze Solver

Algorithm using the depth camera (turn-to-look pattern):
    Since the depth camera only faces forward, checking the right side requires
    the drone to briefly turn 90° right, read the camera, then turn back.

    Phase 0 (fly + tick timer):
        Fly forward. Read front distance and increment _check_timer each frame.
        Stop when front <= STOP_DISTANCE OR _check_timer >= CHECK_INTERVAL.
        Then: save _forward_yaw = current yaw; _target_yaw = (_forward_yaw - 90) % 360
        (CW = look right); reset _check_timer = 0; _phase = 1.
        Otherwise: send_pcmd(FLY_SPEED, 0, 0, 0).

    Phase 1 (turn right to look):
        Yaw to _target_yaw. When aligned:
            _right_dist = _get_front(drone)    # capture right-side distance
            _target_yaw = _forward_yaw         # prepare to turn back
            _phase = 2

    Phase 2 (turn back, then apply right-hand rule):
        Yaw back to _forward_yaw. When aligned, stop and decide:
            if _right_dist > RIGHT_OPEN_THRES  → right is open:
                _forward_yaw = (_forward_yaw - 90) % 360   (turn right)
                _target_yaw = _forward_yaw; _nudge_timer = 0; _phase = 3
            elif _front_dist <= STOP_DISTANCE  → wall still ahead:
                _turn_count += 1; if >= MAX_TURNS → _done = True; return True
                _forward_yaw = (_forward_yaw + 90) % 360   (turn left)
                _target_yaw = _forward_yaw; _nudge_timer = 0; _phase = 3
            else → clear ahead:
                _phase = 0

    Phase 3 (turn to new heading + advance 0.8 s):
        Yaw to _target_yaw. While not aligned: yaw PCMD.
        When aligned: send_pcmd(FLY_SPEED, 0, 0, 0); _nudge_timer += dt.
        After 0.8 s: _check_timer = 0; _phase = 0.

Safety: return True after MAX_TURNS turns.

Your task:
    Implement the four phases described above.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core, drone_utils as uav_utils

STOP_DISTANCE    = 1.2    # m — stop flying when this close to a wall
RIGHT_OPEN_THRES = 4.0    # m — right side is "open" if camera sees this far
CHECK_INTERVAL   = 1.5    # s — peek right this often while flying forward
FLY_SPEED        = 0.35
YAW_SPEED        = 0.5
YAW_THRESH       = 3.0
MAX_RANGE        = 10.0
MAX_TURNS        = 30     # safety: give up after this many turns

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
    _phase = 0; _forward_yaw = 0.0; _target_yaw = 0.0
    _front_dist = MAX_RANGE; _right_dist = MAX_RANGE
    _check_timer = 0.0; _nudge_timer = 0.0; _turn_count = 0; _done = False


def _get_front(drone):
    return min(uav_utils.get_depth_image_center_distance(drone.camera.get_depth_image()) / 100.0, MAX_RANGE)


def _yaw_err(t, c):
    return ((t - c) + 180) % 360 - 180


def update(drone):
    global _phase, _forward_yaw, _target_yaw, _front_dist, _right_dist
    global _check_timer, _nudge_timer, _turn_count, _done
    if _done:
        return True

    dt  = drone.get_delta_time()
    cur = drone.physics.get_attitude()[1] % 360

    if _phase == 0:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # _front_dist = _get_front(drone)
        # _check_timer += dt
        # if _front_dist <= STOP_DISTANCE or _check_timer >= CHECK_INTERVAL:
        #     drone.flight.stop()
        #     _check_timer = 0.0
        #     _forward_yaw = cur
        #     _target_yaw  = (_forward_yaw - 90) % 360   # CW = look right
        #     _phase = 1
        # else:
        #     drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE — turn right to look, then capture distance and turn back
        # err = _yaw_err(_target_yaw, cur)
        # if abs(err) < YAW_THRESH:
        #     drone.flight.stop()
        #     _right_dist = _get_front(drone)
        #     _target_yaw = _forward_yaw   # turn back
        #     _phase = 2
        # else:
        #     yaw PCMD: drone.flight.send_pcmd(0, 0, max(-YAW_SPEED, min(YAW_SPEED, err / 45)), 0)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 2:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE — turn back to _forward_yaw, then apply right-hand rule
        # err = _yaw_err(_forward_yaw, cur)
        # if abs(err) < YAW_THRESH:
        #     drone.flight.stop()
        #     if _right_dist > RIGHT_OPEN_THRES:          # right is open → turn right
        #         _turn_count += 1; print(...)
        #         _forward_yaw = (_forward_yaw - 90) % 360
        #         _target_yaw = _forward_yaw; _nudge_timer = 0.0; _phase = 3
        #     elif _front_dist <= STOP_DISTANCE:           # wall ahead → turn left
        #         if _turn_count >= MAX_TURNS: _done = True; return True
        #         _turn_count += 1; print(...)
        #         _forward_yaw = (_forward_yaw + 90) % 360
        #         _target_yaw = _forward_yaw; _nudge_timer = 0.0; _phase = 3
        #     else:                                        # clear ahead → keep flying
        #         _phase = 0
        # else:
        #     yaw PCMD

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 3:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE — turn to new heading, then advance 0.8 s
        # err = _yaw_err(_target_yaw, cur)
        # if abs(err) >= YAW_THRESH:
        #     yaw PCMD
        # else:
        #     drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)
        #     _nudge_timer += dt
        #     if _nudge_timer >= 0.8:
        #         _nudge_timer = 0.0; _phase = 0

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return _done
