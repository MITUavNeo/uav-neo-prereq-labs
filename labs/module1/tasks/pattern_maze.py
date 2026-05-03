"""Module 1 Pattern: Maze — forward → right → forward → left → forward.

Five-segment course. Each segment is a fixed PCMD held for a fixed duration.
Drives a list of (label, pitch, roll, yaw, throttle, duration) tuples and
advances when the per-segment timer elapses.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../library'))
import drone_core

FORWARD_PITCH = 0.35
YAW_RATE      = 0.5

# (label, pitch, roll, yaw, throttle, duration)
SEGMENTS = [
    ("forward 1",  FORWARD_PITCH, 0, 0,         0, 3.0),
    ("turn right", 0,             0, -YAW_RATE, 0, 1.0),    # ≈ -90°
    ("forward 2",  FORWARD_PITCH, 0, 0,         0, 3.0),
    ("turn left",  0,             0,  YAW_RATE, 0, 1.0),    # ≈ +90°
    ("forward 3",  FORWARD_PITCH, 0, 0,         0, 3.0),
]

_seg_index = 0
_timer     = 0.0
_done      = False


def reset():
    global _seg_index, _timer, _done
    _seg_index = 0
    _timer     = 0.0
    _done      = False


def update(drone):
    global _seg_index, _timer, _done
    if _done:
        return True

    if _seg_index >= len(SEGMENTS):
        drone.flight.stop()
        _done = True
        return True

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    #
    # 1) Unpack the current segment:
    #    label, pitch, roll, yaw, throttle, duration = SEGMENTS[_seg_index]
    #
    # 2) Send the command:
    #    drone.flight.send_pcmd(pitch, roll, yaw, throttle)
    #
    # 3) Advance the timer:
    #    _timer += drone.get_delta_time()
    #
    # 4) When _timer >= duration:
    #    print(f"  segment '{label}' done")
    #    advance _seg_index, reset _timer

    ###### END PUT CODE HERE #########
    ##################################

    return _done
