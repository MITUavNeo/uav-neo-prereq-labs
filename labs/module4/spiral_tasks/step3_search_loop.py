"""Module 4 Spiral — Step 3: Spiral Search Loop
Expand outward in a square spiral until the SAR target is found.

Pattern (repeating pairs of legs):
    fly_leg(duration) → turn_left → fly_leg(duration) → turn_left → duration += step

Your task:
    Phase 0 (fly leg): Call step2_fly_leg.update(drone).
        - If it returns True (target found) → set _done = True, return True.
        - If step2_fly_leg._done is True (leg done, no target):
              Compute _target_yaw = (current + 90) % 360  (CCW = left turn)
              _leg_count += 1
              Every 2 legs, _leg_duration += LEG_STEP
              → Phase 1
    Phase 1 (turn left): Yaw to _target_yaw using shortest-path error.
        When aligned → stop, call step2_fly_leg.reset(_leg_duration), → Phase 0
    Max safety: if _leg_count >= MAX_LEGS → stop and return True.
"""

import drone_core
from . import step2_fly_leg

LEG_START    = 1.0    # initial leg duration (seconds)
LEG_STEP     = 0.5    # increase per two legs
MAX_LEGS     = 20     # safety limit
YAW_SPEED    = 0.5
YAW_THRESHOLD = 3.0

_leg_count   = 0
_phase       = 0   # 0=fly_leg, 1=turn_left
_leg_duration = LEG_START
_target_yaw  = 0.0
_done        = False

def reset():
    global _leg_count, _phase, _leg_duration, _target_yaw, _done
    _leg_count = 0; _phase = 0; _leg_duration = LEG_START
    _target_yaw = 0.0; _done = False
    step2_fly_leg.reset(_leg_duration)

def _yaw_error(target, current):
    return ((target - current) + 180) % 360 - 180

def update(drone):
    global _leg_count, _phase, _leg_duration, _target_yaw, _done
    if _done: return True
    if _leg_count >= MAX_LEGS:
        drone.flight.stop()
        print("[Spiral Step 3] Max legs reached — target not found.")
        _done = True; return True

    if _phase == 0:   # fly leg
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # found = step2_fly_leg.update(drone)
        # if found → _done = True; return True
        # if step2_fly_leg._done:  (leg finished, no target)
        #     current = drone.physics.get_attitude()[1] % 360
        #     _target_yaw = (current + 90) % 360   # CCW = turn left
        #     _phase = 1; _leg_count += 1
        #     if _leg_count % 2 == 0: _leg_duration += LEG_STEP

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:  # turn left
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # current = drone.physics.get_attitude()[1] % 360
        # err = _yaw_error(_target_yaw, current)
        # if |err| < YAW_THRESHOLD → stop, step2_fly_leg.reset(_leg_duration), _phase = 0
        # else → yaw_cmd = max(-YAW_SPEED, min(YAW_SPEED, err / 45.0))
        #         drone.flight.send_pcmd(0, 0, yaw_cmd, 0)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return False
