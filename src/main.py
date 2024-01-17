# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       emmam                                                        #
# 	Created:      1/13/2024, 5:50:55 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

#defining states
idle = 0
driving = 1

wait(500)

# Brain should be defined by default
brain = Brain()

#define ultrasonic
ultrasonic_A = Sonar(brain.three_wire_port.a)
distanceToCup = ultrasonic_A.distance(DistanceUnits.CM)

# motor definitions
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
right_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)

#initial robot state
current_robot_state = idle

CONVERT_RADIANS = math.pi/180
DIAMETER = 4
CIRCUMFERENCE = DIAMETER*math.pi

def go_inches(distance, speed):
    left_motor.spin_to_position(distance*5/CIRCUMFERENCE, TURNS, velocity=speed*5, wait=False) # wait = blocking 
    right_motor.spin_to_position(distance*5/CIRCUMFERENCE, TURNS, velocity=speed*5, wait=False)


while (distanceToCup > 5):
    distanceToCup = ultrasonic_A.distance(DistanceUnits.CM)
    print(distanceToCup)

    