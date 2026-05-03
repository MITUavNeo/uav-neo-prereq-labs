"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

File Name: demo.py

Title: Demo Drone Program

Purpose: To verify that basic drone functions work properly and the student has set up
the system correctly to run Python scripts with the drone start/update paradigm in the
Unity simulator.

Expected Outcome: Terminal output and drone movement occurs when buttons are pressed
- When the "A" button is pressed, print a message to the terminal window
- When the "B" button is pressed, the drone takes off, flies forward and to the right
  for 1 second, and then lands
"""

########################################################################################
# Imports
########################################################################################

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.join(_HERE, '../library'))
sys.path.insert(0, os.path.join(_HERE, '../../uav-neo-library/library'))
import drone_core

########################################################################################
# Global variables
########################################################################################

drone = drone_core.create_drone()

# Declare any global variables here
counter = 0
isFlying = False

########################################################################################
# Functions
########################################################################################

# [FUNCTION] start() is run once when the simulation begins
def start():
    # If we use a global variable in our function, we must list it at
    # the beginning of our function like this
    global counter
    global isFlying

    # The start function is a great place to give initial values to global variables
    counter = 0
    isFlying = False

    # This tells the drone to begin at a standstill
    drone.flight.stop()

# [FUNCTION] update() is called once every frame (~60 fps)
def update():

    global counter
    global isFlying

    # This prints a message every time the A button is pressed on the controller
    if drone.controller.was_pressed(drone.controller.Button.A):
        print("The A button was pressed")

    # Launch the drone and fly forward+right when the B button is pressed
    if drone.controller.was_pressed(drone.controller.Button.B):
        counter = 0
        isFlying = True
        drone.flight.takeoff()

    if isFlying:
        # drone.get_delta_time() gives the time in seconds since the last time
        # the update function was called
        counter += drone.get_delta_time()

        if counter < 2:
            # Wait 2 seconds after takeoff for the drone to stabilize
            drone.flight.stop()
        elif counter < 4:
            # Fly forward and to the right for one second
            # send_pcmd(pitch, roll, yaw, throttle)
            drone.flight.send_pcmd(0.75, 0.75, 0, 0)
        elif counter < 6:
            # stop the drone to stabilize
            drone.flight.stop()
        else:
            # Land the drone
            drone.flight.land()
            isFlying = False

# [FUNCTION] update_slow() is called once per second — useful for debug prints
def update_slow():
    # This prints a message every time that the right bumper is pressed during
    # a call to to update_slow.  If we press and hold the right bumper, it
    # will print a message once per second
    if drone.controller.is_down(drone.controller.Button.RB):
        print("The right bumper is currently down (update_slow)")


########################################################################################
# DO NOT MODIFY: Register callbacks and begin execution
########################################################################################

if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
