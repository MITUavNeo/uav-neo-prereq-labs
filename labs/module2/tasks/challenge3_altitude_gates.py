"""
Challenge 3 — Altitude Profile Gates
Fly through 6 gates in a straight line, each at a DIFFERENT altitude.

                        ___          ___
                   ____|   |________|   |____
              ____|                          |____
    ---------|                                    |------- (finish)
   takeoff

Gate profile:
    Gate 1 (z=15 m) →  1.5 m  Blue    ← low entry
    Gate 2 (z=30 m) →  4.0 m  Green   ← start climbing
    Gate 3 (z=45 m) →  7.0 m  Yellow  ← high pass
    Gate 4 (z=60 m) →  7.0 m  Red     ← hold altitude
    Gate 5 (z=75 m) →  3.5 m  Orange  ← descend
    Gate 6 (z=90 m) →  1.5 m  Purple  ← low finish

NEW CONCEPT vs. Challenge 2:
    In Challenge 2 you held ONE altitude the whole way.
    Now the altitude TARGET changes after each gate is passed.
    You need a P-controller that smoothly transitions between targets
    WHILE still flying forward — both axes at the same time.

    Key insight:
        throttle = Kp_alt * (target_alt - current_alt)
        pitch    = FLY_SPEED   (constant forward)
    Both commands go into send_pcmd every frame simultaneously.

HOW GATE DETECTION WORKS:
    Unlike Challenge 2, where we integrated velocity (vel[2]*dt), here we
    use the drone's GPS to read the actual world Z position directly.

        gps = drone.physics.get_gps()   # returns (latitude, longitude, altitude_msl)
        # The simulator maps Unity world Z → GPS latitude:
        #   latitude = GPS_ORIGIN_LAT + world_z / METERS_PER_DEG_LAT
        # Rearranging:
        world_z = (gps[0] - GPS_ORIGIN_LAT) * METERS_PER_DEG_LAT

    When world_z >= target_z, the drone is at or past that gate's Z position.
    This is more accurate than velocity integration because there is no drift —
    it reads the actual position every frame.

    The Unity scene also has invisible physics triggers at each gate crossbar.
    When the drone's collider enters a trigger, a message is printed to the
    Unity Console confirming the drone physically passed through the gate opening.
    These two checks are independent and complementary.

Your task:
    Each frame:
    1. gps = drone.physics.get_gps()
       world_z = (gps[0] - GPS_ORIGIN_LAT) * METERS_PER_DEG_LAT

    2. Look up the current gate's target:
       target_z, target_alt = GATES[_gate_index]

    3. Compute altitude error and throttle:
       err_alt  = target_alt - drone.physics.get_altitude()
       throttle = clamp(KP_ALT * err_alt, -MAX_THROTTLE, MAX_THROTTLE)

    4. Fly forward AND correct altitude simultaneously:
       drone.flight.send_pcmd(FLY_SPEED, 0, 0, throttle)

    5. When world_z >= target_z (reached this gate):
           print gate passed + current altitude
           _gate_index += 1

    6. When all 6 gates passed:
           drone.flight.stop()
           print summary
           _done = True

Challenge extension:
    Can you make the transition smoother?  Instead of switching to the
    next altitude target instantly, try blending between the current
    target and the next one as a function of how close the next gate is.
    Hint: use linear interpolation (lerp).
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../library'))

import drone_core

# ── Gate definitions: (cumulative forward distance m, target altitude m) ─────
# These match the positions built by BuildAltitudeGates.cs in Unity.
GATES = [
    (15,  1.5),   # Gate 1 — Blue    — low entry
    (30,  4.0),   # Gate 2 — Green   — climbing
    (45,  7.0),   # Gate 3 — Yellow  — high pass
    (60,  7.0),   # Gate 4 — Red     — hold altitude
    (75,  3.5),   # Gate 5 — Orange  — descending
    (90,  1.5),   # Gate 6 — Purple  — low finish
]

# ── GPS constants (match PhysicsModule.cs) ────────────────────────────────────
# The simulator encodes world Z (metres) into GPS latitude as:
#   lat = GPS_ORIGIN_LAT + world_z / METERS_PER_DEG_LAT
# Rearranging gives: world_z = (lat - GPS_ORIGIN_LAT) * METERS_PER_DEG_LAT
GPS_ORIGIN_LAT     = 42.3601    # latitude at Unity world origin (deg)
METERS_PER_DEG_LAT = 111320.0   # metres per degree of latitude

# ── Tuning constants ──────────────────────────────────────────────────────────
FLY_SPEED    = 0.35   # forward pitch (0.0 – 1.0)
KP_ALT       = 2.5    # proportional gain for altitude controller
MAX_THROTTLE = 0.5    # clamp throttle to this magnitude

# ── State ─────────────────────────────────────────────────────────────────────
_gate_index = 0
_world_z    = 0.0    # last-read world Z position (m), for display only
_done       = False

# ─────────────────────────────────────────────────────────────────────────────

def reset():
    global _gate_index, _world_z, _done
    _gate_index = 0
    _world_z    = 0.0
    _done       = False


def update(drone):
    global _gate_index, _world_z, _done
    if _done:
        return True

    if _gate_index >= len(GATES):
        drone.flight.stop()
        print(f"[Challenge 3] All {len(GATES)} altitude gates cleared!")
        _done = True
        return True

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    #
    # ── Step 1: get current world Z from GPS ───────────────────────────────────
    # gps     = drone.physics.get_gps()         # (latitude, longitude, alt_msl)
    # world_z = (gps[0] - GPS_ORIGIN_LAT) * METERS_PER_DEG_LAT
    # _world_z = world_z                         # save for update_slow display
    #
    # ── Step 2: look up current gate target ────────────────────────────────────
    # target_z, target_alt = GATES[_gate_index]
    #
    # ── Step 3: altitude P-controller ─────────────────────────────────────────
    # err_alt  = target_alt - drone.physics.get_altitude()
    # throttle = max(-MAX_THROTTLE, min(MAX_THROTTLE, KP_ALT * err_alt))
    #
    # ── Step 4: fly forward AND hold altitude simultaneously ───────────────────
    # drone.flight.send_pcmd(FLY_SPEED, 0, 0, throttle)
    #
    # ── Step 5: check if gate reached ─────────────────────────────────────────
    # if world_z >= target_z:
    #     print(f"[Gate {_gate_index + 1}] Passed at alt={drone.physics.get_altitude():.2f}m "
    #           f"(target={target_alt}m, error={drone.physics.get_altitude()-target_alt:+.2f}m)")
    #     _gate_index += 1

    ###### END PUT CODE HERE #########
    ##################################

    return _done


# ── Standalone runner ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    _drone = drone_core.create_drone()
    _phase = 0

    def start():
        global _phase
        _phase = 0
        reset()
        print("\n=== Challenge 3: Altitude Profile Gates ===")
        print("Gates:", [(f"z={z}m", f"alt={a}m") for z, a in GATES])
        print("Gate detection: GPS world-Z position (no drift)")
        print()

    def _update():
        global _phase
        if _phase == 0:
            _drone.flight.takeoff()
            if _drone.physics.get_altitude() > 1.0:
                _phase = 1
                reset()
        else:
            if update(_drone):
                _drone.flight.land()

    def _update_slow():
        if _gate_index < len(GATES):
            target_z, target_alt = GATES[_gate_index]
            print(f"world_z={_world_z:.1f}m | alt={_drone.physics.get_altitude():.2f}m | "
                  f"target_alt={target_alt}m | gate={_gate_index+1}/{len(GATES)}")

    _drone.set_start_update(start, _update, _update_slow)
    _drone.go()
