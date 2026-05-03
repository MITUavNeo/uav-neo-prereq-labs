"""Module 6 Part 1 — Step 3: Follow the Line
Fly forward while steering to keep the red line centred under the drone.

How it works:
    The downward camera gives a 480×640 image with the line below.
    The centre of that image (column 320) is directly under the drone.
    If the line appears to the RIGHT of centre (cx > 320) → roll right to follow it.
    If the line appears to the LEFT  of centre (cx < 320) → roll left to follow it.

    lateral_error = (cx - IMAGE_CX) / IMAGE_CX      # -1.0 (far left) … +1.0 (far right)
    roll = clamp(lateral_error * ROLL_GAIN, -MAX_ROLL, MAX_ROLL)
    Then fly: drone.flight.send_pcmd(FLY_SPEED, roll, 0, 0)

Your task:
    Each frame:
    1. Get the downward image: image = drone.camera.get_downward_image()
    2. Find red contours in both hue ranges (use step2_detect_line constants).
    3. If no contour found → hover (drone.flight.stop()) and return False.
    4. Get the centroid: cx, cy = uav_utils.get_contour_center(best)
       Note: cx is the ROW, cy is the COLUMN — use cy for lateral error.
    5. Compute lateral_error = (cy - IMAGE_CX) / IMAGE_CX
    6. Compute roll = clamp(lateral_error * ROLL_GAIN, -MAX_ROLL, MAX_ROLL)
    7. Fly forward: drone.flight.send_pcmd(FLY_SPEED, roll, 0, 0)
    8. Increment _elapsed by drone.get_delta_time().
       When _elapsed >= RUN_DURATION → stop, print, set _done = True.

Extension challenge — lap counting:
    Each time the drone completes a full circuit it returns to the starting heading.
    You can count laps by tracking when get_attitude()[2] (yaw) cycles through
    north (≈0°/360°) → east (≈90°) → south (≈180°) → west (≈270°) → north again.
"""

import sys, os
import numpy as np
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core
import drone_utils as uav_utils
from . import step2_detect_line   # re-use the colour constants from step2

# ── Tuning constants ──────────────────────────────────────────────────────────────────
FLY_SPEED   = 0.35   # forward pitch (0.0 – 1.0)
ROLL_GAIN   = 0.6    # how aggressively to correct lateral error
MAX_ROLL    = 0.5    # clamp roll to this maximum magnitude
RUN_DURATION = 60.0  # seconds — fly for this long then stop
                     # (increase to complete more of the circuit)

# ── Image geometry ───────────────────────────────────────────────────────────────────
IMAGE_WIDTH  = 640
IMAGE_HEIGHT = 480
IMAGE_CX     = IMAGE_WIDTH  // 2   # column 320 — directly below the drone

_done    = False
_elapsed = 0.0


def reset():
    global _done, _elapsed
    _done = False; _elapsed = 0.0


def update(drone):
    global _done, _elapsed
    if _done:
        return True

    ##################################
    #### START PUT CODE HERE #########

    image = drone.camera.get_downward_image()

    contours1 = uav_utils.find_contours(image,
                    step2_detect_line.LINE_LOWER,  step2_detect_line.LINE_UPPER)
    contours2 = uav_utils.find_contours(image,
                    step2_detect_line.LINE_LOWER2, step2_detect_line.LINE_UPPER2)
    best = uav_utils.get_largest_contour(
                contours1 + contours2, step2_detect_line.MIN_AREA)

    if best is None:
        drone.flight.stop()
        return False

    cx, cy = uav_utils.get_contour_center(best)  # (row, column)

    lateral_error = (cy - IMAGE_CX) / IMAGE_CX   # -1.0 … +1.0

    roll = max(-MAX_ROLL, min(MAX_ROLL, lateral_error * ROLL_GAIN))

    drone.flight.send_pcmd(FLY_SPEED, roll, 0, 0)

    _elapsed += drone.get_delta_time()
    if _elapsed >= RUN_DURATION:
        drone.flight.stop()
        print(f"[Step 3] Done — flew for {_elapsed:.1f}s")
        _done = True

    ###### END PUT CODE HERE #########
    ##################################

    return _done
