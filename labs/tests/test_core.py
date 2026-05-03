"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

File Name: test_core.py

Title: Test Core

Purpose: A simple program which can be used to manually test drone_core functionality.
"""

########################################################################################
# Imports
########################################################################################

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.join(_HERE, '../library'))
sys.path.insert(0, os.path.join(_HERE, '../../uav-neo-library/library'))
import drone_core
import drone_utils as uav_utils

########################################################################################
# Global variables
########################################################################################

drone = drone_core.create_drone()

max_speed = 0
update_slow_time = 0
show_triggers = False
show_joysticks = False

########################################################################################
# Functions
########################################################################################


def start():
    """
    This function is run once every time the start button is pressed
    """
    global max_speed
    global update_slow_time
    global show_triggers
    global show_joysticks

    print("Start function called")
    max_speed = 0.25
    update_slow_time = 0.5
    show_triggers = False
    show_joysticks = False

    drone.set_update_slow_time(update_slow_time)
    drone.flight.set_max_speed(max_speed)
    drone.flight.stop()

    # Print start message
    print(
        ">> Test Core: A testing program for the drone_core library.\n"
        "\n"
        "Controls:\n"
        "    Right trigger = pitch forward\n"
        "    Left trigger = pitch backward\n"
        "    Left joystick X = roll, Y = throttle\n"
        "    Right joystick X = yaw\n"
        "    Left bumper = decrease max speed\n"
        "    Right bumper = increase max speed\n"
        "    Left joystick click = print trigger values\n"
        "    Right joystick click = print joystick values\n"
        "    A button = Display forward color image\n"
        "    B button = Display downward color image\n"
        "    X button = Display depth image\n"
        "    Y button = Display sensor data (IMU, altitude, attitude)\n"
    )


def update():
    """
    After start() is run, this function is run every frame until the back button
    is pressed
    """
    global max_speed
    global update_slow_time
    global show_triggers
    global show_joysticks

    # Check if each button was_pressed or was_released
    for button in drone.controller.Button:
        if drone.controller.was_pressed(button):
            print(f"Button [{button.name}] was pressed")
        if drone.controller.was_released(button):
            print(f"Button [{button.name}] was released")

    # Click left and right joystick to toggle showing trigger and joystick values
    left_trigger = drone.controller.get_trigger(drone.controller.Trigger.LEFT)
    right_trigger = drone.controller.get_trigger(drone.controller.Trigger.RIGHT)
    left_joystick = drone.controller.get_joystick(drone.controller.Joystick.LEFT)
    right_joystick = drone.controller.get_joystick(drone.controller.Joystick.RIGHT)

    if drone.controller.was_pressed(drone.controller.Button.LJOY):
        show_triggers = not show_triggers

    if drone.controller.was_pressed(drone.controller.Button.RJOY):
        show_joysticks = not show_joysticks

    if show_triggers:
        print(f"Left trigger: [{left_trigger}]; Right trigger: [{right_trigger}]")

    if show_joysticks:
        print(f"Left joystick: [{left_joystick}]; Right joystick: [{right_joystick}]")

    # Use triggers for pitch, left joystick for roll/throttle, right joystick for yaw
    pitch = right_trigger - left_trigger
    roll = left_joystick[0]
    throttle = left_joystick[1]
    yaw = right_joystick[0]
    drone.flight.send_pcmd(pitch, roll, yaw, throttle)

    # Change max speed and update_slow time when the bumper is pressed
    if drone.controller.was_pressed(drone.controller.Button.LB):
        max_speed = max(1 / 16, max_speed / 2)
        drone.flight.set_max_speed(max_speed)
        update_slow_time *= 2
        drone.set_update_slow_time(update_slow_time)
        print(f"max_speed set to [{max_speed}]")
        print(f"update_slow_time set to [{update_slow_time}] seconds")
    if drone.controller.was_pressed(drone.controller.Button.RB):
        max_speed = min(1, max_speed * 2)
        drone.flight.set_max_speed(max_speed)
        update_slow_time /= 2
        drone.set_update_slow_time(update_slow_time)
        print(f"max_speed set to [{max_speed}]")
        print(f"update_slow_time set to [{update_slow_time}] seconds")

    # A button: Display forward color image
    if drone.controller.is_down(drone.controller.Button.A):
        drone.display.show_color_image(drone.camera.get_color_image())

    # B button: Display downward color image
    elif drone.controller.is_down(drone.controller.Button.B):
        drone.display.show_color_image(drone.camera.get_downward_image())

    # X button: Display depth image
    elif drone.controller.is_down(drone.controller.Button.X):
        depth_image = drone.camera.get_depth_image()
        drone.display.show_depth_image(depth_image)
        depth_center_distance = uav_utils.get_depth_image_center_distance(depth_image)
        print(f"Depth center distance: [{depth_center_distance:.2f}] cm")

    # Y button: Display all sensor data (IMU, altitude, attitude)
    if drone.controller.is_down(drone.controller.Button.Y):
        a = drone.physics.get_linear_acceleration()
        v = drone.physics.get_linear_velocity()
        w = drone.physics.get_angular_velocity()
        alt = drone.physics.get_altitude()
        att = drone.physics.get_attitude()
        print(
            f"Accel: ({a[0]:6.2f},{a[1]:6.2f},{a[2]:6.2f}) m/s^2  "
            f"Vel: ({v[0]:6.2f},{v[1]:6.2f},{v[2]:6.2f}) m/s  "
            f"Gyro: ({w[0]:5.2f},{w[1]:5.2f},{w[2]:5.2f}) rad/s\n"
            f"Altitude: {alt:6.2f} m  "
            f"Attitude: (P:{att[0]:6.1f}, R:{att[1]:6.1f}, Y:{att[2]:6.1f}) deg"
        )


def update_slow():
    """
    After start() is run, this function is run at a constant rate that is slower
    than update().  By default, update_slow() is run once per second
    """
    # Check if each button is_down
    for button in drone.controller.Button:
        if drone.controller.is_down(button):
            print(f"Button [{button.name}] is down")


########################################################################################
# DO NOT MODIFY: Register callbacks and begin execution
########################################################################################

if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
