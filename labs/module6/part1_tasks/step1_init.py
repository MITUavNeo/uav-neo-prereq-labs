"""Module 6 Part 1 — Step 1: Init (takeoff + reach line-following altitude)
This file is provided complete as a reference for the reset()/update() pattern.

The drone takes off and climbs to LINE_ALTITUDE metres — the correct height for the
downward camera to see the full width of the red line below.
"""

import drone_core

LINE_ALTITUDE = 1.2    # metres — fly at this height to see the line below
TAKEOFF_WAIT  = 3.5    # seconds to wait after takeoff command before altitude control

_phase = 0
_timer = 0.0
_done  = False


def reset():
    global _phase, _timer, _done
    _phase = 0; _timer = 0.0; _done = False


def update(drone):
    global _phase, _timer, _done
    if _done:
        return True

    _timer += drone.get_delta_time()

    if _phase == 0:
        drone.flight.takeoff()
        if _timer >= TAKEOFF_WAIT:
            _phase = 1; _timer = 0.0

    elif _phase == 1:
        err = LINE_ALTITUDE - drone.physics.get_altitude()
        if abs(err) < 0.10:
            drone.flight.stop()
            print(f"[Module 6 Step 1] Ready at {drone.physics.get_altitude():.2f} m")
            _done = True
        else:
            drone.flight.send_pcmd(0, 0, 0, max(-0.5, min(0.5, err * 2.5)))

    return _done
