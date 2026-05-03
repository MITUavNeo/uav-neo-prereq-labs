"""
Module 3 Part 1 — Step 1: Positioning
Take off and climb to the search altitude where the camera can see objects.

Your task:
    Phase 0: Call drone.flight.takeoff() each frame. After TAKEOFF_WAIT seconds → Phase 1.
    Phase 1: Proportional throttle to reach SEARCH_ALTITUDE.
             When |error| < ALT_THRESHOLD → stop, print, set _done = True.
"""

import drone_core

SEARCH_ALTITUDE = 2.0   # metres — height from which camera sees objects
TAKEOFF_WAIT    = 3.5   # seconds
ALT_THRESHOLD   = 0.12

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

    if _phase == 0:   # takeoff
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Hint: drone.flight.takeoff()
        # After _timer >= TAKEOFF_WAIT → _phase = 1; _timer = 0.0

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:  # climb to search altitude
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Hint: alt = drone.physics.get_altitude()
        #       error = SEARCH_ALTITUDE - alt
        # If |error| < ALT_THRESHOLD → stop, print, set _done = True
        # Else → throttle = max(-0.5, min(0.5, error * 2.5))
        #        drone.flight.send_pcmd(0, 0, 0, throttle)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return _done
