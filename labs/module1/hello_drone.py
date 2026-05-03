"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

File Name: hello_drone.py
Title: Module 1 — Hello Drone
Python Topics: Variables, Math, Intro to Colab
Drone Topic: Introduction, basic flight

Author: [PLACEHOLDER] << Write your name here

Purpose:
    Introduce the drone control paradigm (start / update / update_slow)
    and demonstrate basic sensor reading using variables and math.

Expected Outcome:
    - Drone takes off and hovers for 2 seconds
    - Terminal prints altitude, heading, and speed once per second
    - Drone flies forward for 3 seconds, then slows and lands
    - Total distance flown is calculated and printed at the end
"""

########################################################################################
# Imports
########################################################################################

import sys
import os
import math

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../library'))

import drone_core
import drone_utils as uav_utils

########################################################################################
# Global variables
########################################################################################

drone = drone_core.create_drone()

# ── Flight phases ──────────────────────────────────────────────────────────────────
TAKEOFF     = 0
HOVER       = 1
FLY_FORWARD = 2
SLOW_DOWN   = 3
LAND        = 4

phase       = TAKEOFF
phase_timer = 0.0

# ── Tracking variables (demonstrate variables + math) ─────────────────────────────
max_altitude   = 0.0   # metres  — highest altitude reached this flight
total_distance = 0.0   # metres  — estimated distance flown (speed × time)

# ── Tunable constants ──────────────────────────────────────────────────────────────
TAKEOFF_WAIT   = 3.5   # seconds to wait for takeoff sequence to complete
HOVER_DURATION = 2.0   # seconds to hover before flying forward
FLY_DURATION   = 3.0   # seconds to fly forward
FLY_SPEED      = 0.4   # PCMD pitch ratio: 0.0 (stationary) – 1.0 (max speed)

########################################################################################
# Functions
########################################################################################

def start():
    """
    Called once when the program starts.
    Initialise all global variables here.
    """
    global phase, phase_timer, max_altitude, total_distance

    phase          = TAKEOFF
    phase_timer    = 0.0
    max_altitude   = 0.0
    total_distance = 0.0

    drone.flight.stop()
    print("=== Module 1: Hello Drone ===")
    print("Initiating takeoff sequence…")


def update():
    """
    Called every frame (~60 fps).
    Implement the phase state machine below.

    Phases:
        TAKEOFF     — call drone.flight.takeoff() each frame; advance after TAKEOFF_WAIT s
        HOVER       — call drone.flight.stop();   advance after HOVER_DURATION s
        FLY_FORWARD — send forward PCMD;           advance after FLY_DURATION s
        SLOW_DOWN   — stop and wait 1.5 s, then print stats and advance to LAND
        LAND        — call drone.flight.land()
    """
    global phase, phase_timer, max_altitude, total_distance

    dt          = drone.get_delta_time()
    phase_timer += dt

    altitude = drone.physics.get_altitude()

    # Track maximum altitude (use an if-statement and the variable above)
    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Hint: if altitude > max_altitude, update max_altitude

    ###### END PUT CODE HERE #########
    ##################################

    # Accumulate total distance = speed × time
    velocity = drone.physics.get_linear_velocity()   # [right, up, forward] m/s
    speed    = math.sqrt(velocity[0]**2 + velocity[1]**2 + velocity[2]**2)
    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Hint: total_distance += speed * dt

    ###### END PUT CODE HERE #########
    ##################################

    # Phase state machine
    if phase == TAKEOFF:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Hint: call drone.flight.takeoff() here
        # After phase_timer >= TAKEOFF_WAIT, set phase = HOVER and reset phase_timer

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif phase == HOVER:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Hint: call drone.flight.stop()
        # After phase_timer >= HOVER_DURATION, set phase = FLY_FORWARD and reset timer

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif phase == FLY_FORWARD:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Hint: drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)
        # After phase_timer >= FLY_DURATION, advance to SLOW_DOWN

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif phase == SLOW_DOWN:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Hint: stop, wait 1.5 s, then print max_altitude and total_distance, then set phase = LAND

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif phase == LAND:
        drone.flight.land()


def update_slow():
    """
    Called once per second — print status messages here.
    """
    altitude = drone.physics.get_altitude()
    attitude = drone.physics.get_attitude()    # [pitch, yaw, roll] degrees
    velocity = drone.physics.get_linear_velocity()
    speed    = math.sqrt(velocity[0]**2 + velocity[1]**2 + velocity[2]**2)

    heading = attitude[1] % 360

    phase_names = ["TAKEOFF", "HOVER", "FLY_FWD", "SLOW", "LAND"]
    print(
        f"Alt: {altitude:5.2f} m | "
        f"Heading: {heading:6.1f}° | "
        f"Speed: {speed:.2f} m/s | "
        f"Phase: {phase_names[phase]}"
    )


########################################################################################
# DO NOT MODIFY: Register callbacks and begin execution
########################################################################################

if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
