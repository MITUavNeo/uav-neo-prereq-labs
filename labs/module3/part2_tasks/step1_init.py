"""
Module 3 Part 2 — Step 1: Initialise for ArUco Maze
Take off and face forward (0°) to ensure a consistent starting heading.

Your task:
    Phase 0: Takeoff — wait TAKEOFF_WAIT seconds.
    Phase 1: Climb to FLIGHT_ALTITUDE using proportional throttle.
    Phase 2: Turn to face FORWARD_HEADING (0°) using shortest-path yaw error.
             When aligned → stop, print, set _done = True.
"""

import drone_core

FLIGHT_ALTITUDE = 1.8    # metres — eye level with the ArUco markers
TAKEOFF_WAIT    = 3.5
FORWARD_HEADING = 0.0    # degrees — face east / +X axis
YAW_THRESHOLD   = 3.0

_phase = 0
_timer = 0.0
_done  = False

def reset():
    global _phase, _timer, _done
    _phase = 0; _timer = 0.0; _done = False

def _yaw_error(target, current):
    return ((target - current) + 180) % 360 - 180

def update(drone):
    global _phase, _timer, _done
    if _done:
        return True

    _timer += drone.get_delta_time()

    if _phase == 0:   # takeoff
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # drone.flight.takeoff()
        # After _timer >= TAKEOFF_WAIT → _phase = 1; _timer = 0.0

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:  # reach flight altitude
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Proportional throttle to FLIGHT_ALTITUDE
        # When |error| < 0.12 → _phase = 2; _timer = 0.0

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 2:  # face forward
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # current = drone.physics.get_attitude()[1] % 360
        # err = _yaw_error(FORWARD_HEADING, current)
        # If |err| < YAW_THRESHOLD → stop, print, _done = True
        # Else → yaw_cmd = max(-0.5, min(0.5, err / 45.0))
        #        drone.flight.send_pcmd(0, 0, yaw_cmd, 0)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return _done
