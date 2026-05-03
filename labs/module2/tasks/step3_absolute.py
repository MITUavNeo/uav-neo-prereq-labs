"""
Step 3 — Absolute Position
Fly to a fixed world position using dead-reckoning (velocity integration).

"Absolute" means relative to the drone's starting position at the
beginning of this step (0, 0 = where the drone was when reset() was called).

Your task:
    1. Each frame, integrate velocity to estimate position:
           _fwd += velocity[2] * dt    (vel[2] = forward speed in m/s)
           _rgt += velocity[0] * dt    (vel[0] = rightward speed in m/s)
    2. Compute error vectors to TARGET_FORWARD / TARGET_RIGHT / TARGET_ALTITUDE.
    3. Send proportional PCMD commands for pitch, roll, and throttle.
    4. Return True when within POSITION_THRESHOLD of the target.
"""

import sys, os, math
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../library'))

import drone_core

# ── Target position (metres from start of this step) ──────────────────────────────
TARGET_FORWARD  =  5.0   # metres ahead
TARGET_RIGHT    =  0.0   # metres right (0 = fly straight ahead)
TARGET_ALTITUDE =  3.0   # metres above origin
POSITION_THRESHOLD = 0.4 # metres — close enough

# ── Flight limits ──────────────────────────────────────────────────────────────────
MAX_SPEED    = 0.4   # PCMD pitch/roll magnitude
MAX_THROTTLE = 0.5

# ── Module-level state ─────────────────────────────────────────────────────────────
_fwd  = 0.0   # dead-reckoning: metres forward from reset origin
_rgt  = 0.0   # dead-reckoning: metres right   from reset origin
_done = False

# ──────────────────────────────────────────────────────────────────────────────────

def reset():
    global _fwd, _rgt, _done
    _fwd  = 0.0
    _rgt  = 0.0
    _done = False


def update(drone):
    """
    Fly to (TARGET_FORWARD, TARGET_RIGHT) from the reset origin.

    Dead-reckoning:
        position += velocity × delta_time   (body frame: vel[2]=fwd, vel[0]=right)

    Returns True when within POSITION_THRESHOLD of the target.
    """
    global _fwd, _rgt, _done
    if _done:
        return True

    dt  = drone.get_delta_time()
    vel = drone.physics.get_linear_velocity()   # [right, up, forward] m/s

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Step 1: Integrate velocity to update _fwd and _rgt
    #         _fwd += vel[2] * dt
    #         _rgt += vel[0] * dt
    #
    # Step 2: Compute error to target
    #         err_fwd = TARGET_FORWARD - _fwd
    #         err_rgt = TARGET_RIGHT   - _rgt
    #         err_alt = TARGET_ALTITUDE - drone.physics.get_altitude()
    #         distance_2d = math.sqrt(err_fwd**2 + err_rgt**2)
    #
    # Step 3: If close enough → stop, print, set _done = True, return True
    #
    # Step 4: Send proportional PCMD
    #         pitch    = max(-MAX_SPEED,    min(MAX_SPEED,    err_fwd * 0.2))
    #         roll     = max(-MAX_SPEED,    min(MAX_SPEED,    err_rgt * 0.2))
    #         throttle = max(-MAX_THROTTLE, min(MAX_THROTTLE, err_alt * 2.5))
    #         drone.flight.send_pcmd(pitch, roll, 0, throttle)

    ###### END PUT CODE HERE #########
    ##################################

    return False


# ── Standalone runner ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    _drone = drone_core.create_drone()
    _phase = 0

    def start():
        global _phase
        _phase = 0
        reset()
        print("Step 3: Absolute Position")

    def _update():
        global _phase
        if _phase == 0:
            _drone.flight.takeoff()
            if _drone.physics.get_altitude() > 1.0:
                _phase = 1; reset()
        else:
            done = update(_drone)
            if done:
                _drone.flight.land()

    _drone.set_start_update(start, _update)
    _drone.go()
