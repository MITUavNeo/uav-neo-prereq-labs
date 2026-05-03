"""Module 6 Part 1 — Step 2: Detect the Line Colour

The track line spawns a RANDOM colour every run (red, blue, green, yellow,
orange, purple, or cyan).  You cannot hardcode red HSV ranges anymore —
you must figure out the colour dynamically from the downward camera.

HOW COLOUR DETECTION WORKS
──────────────────────────
The downward camera returns a 480×640 BGR image.
Converting to HSV splits colour into three channels:
    H (Hue)        0–179  — the colour family (red=0, yellow=30, green=60,
                             cyan=90, blue=120, purple=150, red again=180)
    S (Saturation) 0–255  — how vivid the colour is (0=grey, 255=pure)
    V (Value)      0–255  — how bright it is (0=black, 255=white)

The floor/terrain has LOW saturation (grey/brown).
The line has HIGH saturation.

Algorithm:
    1. Convert image to HSV with cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    2. Mask pixels with S > 80 and V > 60  (saturated, non-dark)
    3. Take all H values from those pixels and build a histogram
    4. The peak bin = dominant hue → that is the line colour
    5. Build HSV bounds:  lower = [hue-15, 80, 60]
                          upper = [hue+15, 255, 255]
       Special case — Red wraps at 0/179: need two ranges
           range 1: [0, 80, 60] → [hue+15, 255, 255]
           range 2: [hue-15+180, 80, 60] → [179, 255, 255]

Once colour detected:
    6. Run find_contours with those bounds to confirm the line is visible
    7. Store the bounds in LINE_LOWER, LINE_UPPER (and LINE_LOWER2,
       LINE_UPPER2 for red) so Step 3 can use them
    8. Set _done = True and print a confirmation message

Returns True when the line colour has been identified and confirmed.
"""

import cv2
import numpy as np

import drone_core
import drone_utils as uav_utils

# ── Colour bounds — populated dynamically during step 2 ──────────────────────
# Step 3 reads these to know which HSV range to search for.
LINE_LOWER  = np.array([  0, 80, 60], dtype=np.uint8)   # placeholders
LINE_UPPER  = np.array([179, 255, 255], dtype=np.uint8)
LINE_LOWER2 = np.array([  0, 80, 60], dtype=np.uint8)   # only used for red wrap
LINE_UPPER2 = np.array([  0, 80, 60], dtype=np.uint8)   # set equal → no-op if not red

MIN_AREA     = 500   # pixels — ignore tiny detections
IS_RED_WRAP  = False # True when dominant hue is near 0° (red wraps in HSV)

# ── Results exported for step3 ────────────────────────────────────────────────
line_cx = 0   # pixel column of line centre
line_cy = 0   # pixel row    of line centre

_done = False


def reset():
    global _done, line_cx, line_cy
    _done = False; line_cx = 0; line_cy = 0


def _dominant_hue(image):
    """
    Return the dominant hue (0-179) of saturated pixels in the image,
    or None if no saturated pixels are found.
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Keep only saturated, mid-bright pixels (not floor/sky)
    mask = (hsv[:, :, 1] > 80) & (hsv[:, :, 2] > 60)
    hues = hsv[:, :, 0][mask]
    if len(hues) < 100:
        return None
    # 18 bins → each bin covers 10°
    hist, bins = np.histogram(hues, bins=18, range=(0, 180))
    peak_bin = int(np.argmax(hist))
    return int(bins[peak_bin]) + 5   # centre of the winning bin


def _build_bounds(hue):
    """
    Build HSV lower/upper bounds from a dominant hue value.
    Returns (lower, upper, lower2, upper2, is_red_wrap).
    lower2/upper2 are only meaningful when is_red_wrap=True.
    """
    tol = 15
    if hue <= tol or hue >= 179 - tol:
        # Red wraps around 0 — need two ranges
        lower  = np.array([0,          80,  60], dtype=np.uint8)
        upper  = np.array([tol,       255, 255], dtype=np.uint8)
        lower2 = np.array([179 - tol,  80,  60], dtype=np.uint8)
        upper2 = np.array([179,        255, 255], dtype=np.uint8)
        return lower, upper, lower2, upper2, True
    else:
        lower  = np.array([max(0,   hue - tol),  80,  60], dtype=np.uint8)
        upper  = np.array([min(179, hue + tol), 255, 255], dtype=np.uint8)
        # No second range needed — set lower2 == upper2 → empty result
        lower2 = np.array([0, 0, 0], dtype=np.uint8)
        upper2 = np.array([0, 0, 0], dtype=np.uint8)
        return lower, upper, lower2, upper2, False


def update(drone):
    global _done, line_cx, line_cy
    global LINE_LOWER, LINE_UPPER, LINE_LOWER2, LINE_UPPER2, IS_RED_WRAP
    if _done:
        return True

    drone.flight.stop()   # hover while scanning

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    #
    # ── Step 1: get the downward image ────────────────────────────────────────
    # image = drone.camera.get_downward_image()
    #
    # ── Step 2: find the dominant saturated hue ───────────────────────────────
    # hue = _dominant_hue(image)
    # if hue is None:
    #     return False    # no saturated pixels yet — keep hovering
    #
    # ── Step 3: build HSV bounds from that hue ────────────────────────────────
    # LINE_LOWER, LINE_UPPER, LINE_LOWER2, LINE_UPPER2, IS_RED_WRAP = \
    #     _build_bounds(hue)
    #
    # ── Step 4: verify the line is actually visible with those bounds ─────────
    # contours1 = uav_utils.find_contours(image, LINE_LOWER,  LINE_UPPER)
    # contours2 = uav_utils.find_contours(image, LINE_LOWER2, LINE_UPPER2)
    # best = uav_utils.get_largest_contour(contours1 + contours2, MIN_AREA)
    # if best is None:
    #     return False    # bounds not confirmed yet — keep trying
    #
    # ── Step 5: store centroid and finish ─────────────────────────────────────
    # cx, cy = uav_utils.get_contour_center(best)
    # line_cx = cy
    # line_cy = cx
    # area    = uav_utils.get_contour_area(best)
    # colour_names = {True: "Red", False: f"hue={hue}"}
    # print(f"[Step 2] Line colour detected: hue={hue} "
    #       f"| col={line_cx}, row={line_cy}, area={area:.0f}")
    # _done = True

    ###### END PUT CODE HERE #########
    ##################################

    return _done
