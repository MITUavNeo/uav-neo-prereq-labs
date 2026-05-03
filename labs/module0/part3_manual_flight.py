"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

Title: Module 0 Part 3 — Manual Flight
Python Topics: Reading analog inputs, mapping ranges, function arguments
Drone Topic: The 4 flight axes (pitch / roll / yaw / throttle) — manual control

Author: [PLACEHOLDER] << Write your name here

Purpose:
    Build intuition for what send_pcmd(pitch, roll, yaw, throttle) actually
    does PHYSICALLY before being asked to write autonomous code. Map the
    controller's two analog joysticks (and triggers) to the four drone
    flight axes using the standard Mode-2 helicopter convention.

The 4 flight axes (each in [-1.0, +1.0]):
    pitch    — nose up/down → fly forward/backward
    roll     — bank left/right → strafe left/right
    yaw      — rotate around vertical axis
    throttle — climb/descend

Mode-2 controller mapping:
    Left  joystick X → yaw         |  Right joystick X → roll
    Left  joystick Y → throttle    |  Right joystick Y → pitch
    Triggers         — alternate throttle (left=down, right=up)

Controller mapping in the simulator:
    A button = '1' key  → takeoff
    B button = '2' key  → land

Expected Outcome:
    Press '1' to take off → manual joystick control engages after ~3 s
    Press '2' to land
    Repeat as desired

How to run:
    drone sim labs/module0/part3_manual_flight.py
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../library'))
import drone_core

drone = drone_core.create_drone()

# ── State ────────────────────────────────────────────────────────────────
_state = "GROUNDED"   # GROUNDED → TAKING_OFF → FLYING → LANDING
_phase_timer = 0.0
TAKEOFF_WAIT = 3.0

# ── Tuning ───────────────────────────────────────────────────────────────
PITCH_GAIN    = 0.6
ROLL_GAIN     = 0.6
YAW_GAIN      = 0.5
THROTTLE_GAIN = 0.5


def start():
    global _state, _phase_timer
    _state = "GROUNDED"
    _phase_timer = 0.0
    print("=== Module 0 Part 3: Manual Flight ===")
    print("Press '1' (A) to take off, '2' (B) to land.\n")


def update():
    global _state, _phase_timer

    Button   = drone.controller.Button
    Trigger  = drone.controller.Trigger
    Joystick = drone.controller.Joystick

    _phase_timer += drone.get_delta_time()

    if _state == "GROUNDED":
        drone.flight.stop()
        if drone.controller.was_pressed(Button.A):
            print("Taking off…")
            drone.flight.takeoff()
            _state = "TAKING_OFF"
            _phase_timer = 0.0

    elif _state == "TAKING_OFF":
        if _phase_timer >= TAKEOFF_WAIT:
            print("Manual control engaged. Use joysticks. Press '2' (B) to land.")
            _state = "FLYING"
            _phase_timer = 0.0

    elif _state == "FLYING":
        if drone.controller.was_pressed(Button.B):
            print("Landing…")
            drone.flight.land()
            _state = "LANDING"
            _phase_timer = 0.0
            return

        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        #
        # 1) Read the two joysticks and the two triggers:
        #    left_x,  left_y  = drone.controller.get_joystick(Joystick.LEFT)
        #    right_x, right_y = drone.controller.get_joystick(Joystick.RIGHT)
        #    trig_l = drone.controller.get_trigger(Trigger.LEFT)
        #    trig_r = drone.controller.get_trigger(Trigger.RIGHT)
        #
        # 2) Map them to the four flight axes (Mode-2 convention):
        #    yaw      = left_x  * YAW_GAIN
        #    pitch    = right_y * PITCH_GAIN
        #    roll     = right_x * ROLL_GAIN
        #    throttle = left_y  * THROTTLE_GAIN
        #
        # 3) Optional: let the triggers act as an alternate throttle so the
        #    drone can be flown one-handed. e.g.
        #    trig_throttle = (trig_r - trig_l) * THROTTLE_GAIN
        #    if abs(trig_throttle) > 0.05:
        #        throttle = trig_throttle
        #
        # 4) Send the command:
        #    drone.flight.send_pcmd(pitch, roll, yaw, throttle)

        ###### END PUT CODE HERE #########
        ##################################

    elif _state == "LANDING":
        if _phase_timer >= 4.0:
            _state = "GROUNDED"
            _phase_timer = 0.0
            print("Landed. Press '1' (A) to take off again.\n")


def update_slow():
    if _state == "FLYING":
        alt = drone.physics.get_altitude()
        print(f"  [flying] alt={alt:.2f}m")
    else:
        print(f"  [{_state.lower()}]")


if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
