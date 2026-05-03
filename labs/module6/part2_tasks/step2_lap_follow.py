"""Module 6 Part 2 — Step 2: Follow the Line and Count Laps

Build on the Part 1 line-following controller and add lap counting
using the drone's heading (yaw).

How lap counting works:
    The F1 circuit is a clockwise loop. Starting at the north straight
    facing north (yaw ≈ 0°), the drone passes through 4 heading sectors
    in order each lap:

        Sector 0 = North  (yaw  315–360 or 0–44)
        Sector 1 = East   (yaw   45–134)
        Sector 2 = South  (yaw  135–224)
        Sector 3 = West   (yaw  225–314)

    One lap = passing through sectors 1 → 2 → 3 → 0 in order.
    We track which sector we are "waiting for next" (_next_sector).

    At start: _next_sector = 1 (East — the first turn).
    When sector 1 seen:  _next_sector = 2  (South)
    When sector 2 seen:  _next_sector = 3  (West)
    When sector 3 seen:  _next_sector = 0  (North)
    When sector 0 seen:  _lap_count += 1,  _next_sector = 1  ← lap!

    The two left-turn chicanes (T3 S→E, T6 W→S) briefly push the yaw
    backward but don't advance _next_sector because we only advance
    forward, never backward.

Your task:
    Each frame:
    1.  Get the downward image and detect the red line (same as Part 1).
    2.  If line not found → drone.flight.stop(), return False.
    3.  Compute lateral_error and roll, fly forward (same as Part 1).
    4.  Get yaw: roll_d, pitch_d, yaw_d = drone.physics.get_attitude()
    5.  Determine current sector: sector = _yaw_to_sector(yaw_d)
    6.  If sector == _next_sector:
            advance _next_sector = (_next_sector + 1) % 4
            if _next_sector == 1:   # wrapped around — completed a lap
                _lap_count += 1
                lap_time = _elapsed - _last_lap_time
                _last_lap_time = _elapsed
                print(f"[Lap {_lap_count}] completed in {lap_time:.1f}s")
    7.  Increment _elapsed by drone.get_delta_time().
    8.  When _elapsed >= RACE_DURATION:
            drone.flight.stop()
            print summary (total laps, average lap time)
            _done = True

Extension challenge — speed tuning:
    Increase FLY_SPEED (up to 0.6) and ROLL_GAIN to try to complete
    more laps before RACE_DURATION expires. How fast can you go without
    losing the line on a corner?
"""

import sys, os
import numpy as np
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core
import drone_utils as uav_utils
from part1_tasks import step2_detect_line

# ── Tuning constants ──────────────────────────────────────────────────────────
FLY_SPEED    = 0.35   # forward pitch (0.0 – 1.0)
ROLL_GAIN    = 0.6    # how aggressively to correct lateral error
MAX_ROLL     = 0.5    # clamp roll to this maximum magnitude
RACE_DURATION = 120.0 # seconds to fly before stopping

# ── Image geometry ────────────────────────────────────────────────────────────
IMAGE_CX = 320        # centre column of the 640-wide downward image

# ── Lap state (read by part2_main.py update_slow) ────────────────────────────
_lap_count    = 0
_next_sector  = 1      # sector we're waiting to enter next (1=E is first after N start)
_last_lap_time = 0.0
_elapsed      = 0.0
_done         = False


def reset():
    global _lap_count, _next_sector, _last_lap_time, _elapsed, _done
    _lap_count = 0; _next_sector = 1; _last_lap_time = 0.0
    _elapsed = 0.0; _done = False


def _yaw_to_sector(yaw_deg):
    """Map a yaw angle (degrees, any range) to 0=N, 1=E, 2=S, 3=W."""
    yaw = yaw_deg % 360
    if yaw >= 315 or yaw < 45:  return 0   # North
    if yaw <  135:               return 1   # East
    if yaw <  225:               return 2   # South
    return 3                                # West


def update(drone):
    global _lap_count, _next_sector, _last_lap_time, _elapsed, _done
    if _done:
        return True

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    #
    # ── Step 1 & 2: detect red line (same as Part 1) ──────────────────────────
    # image = drone.camera.get_downward_image()
    # contours1 = uav_utils.find_contours(image,
    #                 step2_detect_line.LINE_LOWER,  step2_detect_line.LINE_UPPER)
    # contours2 = uav_utils.find_contours(image,
    #                 step2_detect_line.LINE_LOWER2, step2_detect_line.LINE_UPPER2)
    # best = uav_utils.get_largest_contour(
    #             contours1 + contours2, step2_detect_line.MIN_AREA)
    # if best is None:
    #     drone.flight.stop()
    #     return False
    #
    # ── Step 3: proportional roll (same as Part 1) ────────────────────────────
    # cx, cy = uav_utils.get_contour_center(best)   # (row, column)
    # lateral_error = (cy - IMAGE_CX) / IMAGE_CX
    # roll = max(-MAX_ROLL, min(MAX_ROLL, lateral_error * ROLL_GAIN))
    # drone.flight.send_pcmd(FLY_SPEED, roll, 0, 0)
    #
    # ── Steps 4-6: lap counting via heading sector ────────────────────────────
    # roll_d, pitch_d, yaw_d = drone.physics.get_attitude()
    # sector = _yaw_to_sector(yaw_d)
    # if sector == _next_sector:
    #     _next_sector = (_next_sector + 1) % 4
    #     if _next_sector == 1:             # wrapped back to waiting for East = lap done
    #         _lap_count += 1
    #         lap_time = _elapsed - _last_lap_time
    #         _last_lap_time = _elapsed
    #         print(f"[Lap {_lap_count}] completed in {lap_time:.1f}s  "
    #               f"(total elapsed: {_elapsed:.1f}s)")
    #
    # ── Steps 7-8: timer and stop ─────────────────────────────────────────────
    # _elapsed += drone.get_delta_time()
    # if _elapsed >= RACE_DURATION:
    #     drone.flight.stop()
    #     avg = (_elapsed / _lap_count) if _lap_count > 0 else 0
    #     print(f"\n[Part 2] Race over after {_elapsed:.1f}s — "
    #           f"{_lap_count} lap(s) completed, avg {avg:.1f}s/lap")
    #     _done = True

    ###### END PUT CODE HERE #########
    ##################################

    return _done
