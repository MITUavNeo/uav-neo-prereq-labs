"""Module 5 Part 1 — Step 1: Init (takeoff + reach maze altitude)
This file is provided complete as a reference for the reset()/update() pattern."""
import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core
MAZE_ALTITUDE = 1.5; TAKEOFF_WAIT = 3.5
_phase = 0; _timer = 0.0; _done = False
def reset():
    global _phase, _timer, _done; _phase = 0; _timer = 0.0; _done = False
def update(drone):
    global _phase, _timer, _done
    if _done: return True
    _timer += drone.get_delta_time()
    if _phase == 0:
        drone.flight.takeoff()
        if _timer >= TAKEOFF_WAIT: _phase = 1; _timer = 0.0
    elif _phase == 1:
        err = MAZE_ALTITUDE - drone.physics.get_altitude()
        if abs(err) < 0.12:
            drone.flight.stop(); print(f"[Part1 Step 1] Ready at {drone.physics.get_altitude():.2f}m"); _done = True
        else:
            drone.flight.send_pcmd(0, 0, 0, max(-0.5, min(0.5, err * 2.5)))
    return _done
