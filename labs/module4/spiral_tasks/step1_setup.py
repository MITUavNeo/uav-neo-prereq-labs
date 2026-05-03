"""Module 4 Spiral — Step 1: Setup
Take off and fly to the centre of the search area.

Your task:
    Phase 0: Takeoff — wait TAKEOFF_WAIT seconds.
    Phase 1: Proportional throttle to SEARCH_ALTITUDE.
             When |err| < 0.12 → stop, print, set _done = True.
"""

import drone_core

SEARCH_ALTITUDE = 2.5
TAKEOFF_WAIT    = 3.5
_phase = 0; _timer = 0.0; _done = False

def reset():
    global _phase, _timer, _done
    _phase = 0; _timer = 0.0; _done = False

def update(drone):
    global _phase, _timer, _done
    if _done: return True
    _timer += drone.get_delta_time()

    if _phase == 0:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # drone.flight.takeoff()
        # After _timer >= TAKEOFF_WAIT → _phase = 1; _timer = 0.0

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # err = SEARCH_ALTITUDE - drone.physics.get_altitude()
        # If |err| < 0.12 → stop, print, _done = True
        # Else → throttle = max(-0.5, min(0.5, err * 2.5))
        #        drone.flight.send_pcmd(0, 0, 0, throttle)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return _done
