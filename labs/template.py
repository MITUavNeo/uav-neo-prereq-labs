"""
MIT BWSI Autonomous Drone Racing Course - UAV Neo
GNU General Public License v3.0

File Name: template.py << [Modify with your own file name!]

Title: [PLACEHOLDER] << [Modify with your own title]

Author: [PLACEHOLDER] << [Write your name or team name here]

Purpose: [PLACEHOLDER] << [Write the purpose of the script here]

Expected Outcome: [PLACEHOLDER] << [Write what you expect will happen when you run
the script.]
"""

########################################################################################
# Imports
########################################################################################

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))

# Path to the drone library — adjust if your file is in a sub-folder:
#   same folder as labs/:       '../library'   (default below)
#   one level deeper (e.g. module2/tasks/):  '../../library'
sys.path.insert(0, os.path.join(_HERE, '../library'))
sys.path.insert(0, os.path.join(_HERE, '../../uav-neo-library/library'))
import drone_core

########################################################################################
# Global variables
########################################################################################

drone = drone_core.create_drone()

# Declare any global variables here


########################################################################################
# Functions
########################################################################################

# [FUNCTION] start() is run once when the simulation begins
def start():
    pass  # Remove 'pass' and write your source code for start() here


# [FUNCTION] update() is called once every frame (~60 fps)
def update():
    pass  # Remove 'pass' and write your source code for update() here


# [FUNCTION] update_slow() is called once per second — useful for debug prints
def update_slow():
    pass  # Remove 'pass' and write your source code for update_slow() here


########################################################################################
# DO NOT MODIFY: Register callbacks and begin execution
########################################################################################

if __name__ == "__main__":
    drone.set_start_update(start, update, update_slow)
    drone.go()
