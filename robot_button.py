from rrb3 import *
import robot_controller as robot


rr = RRB3()

while True:
    if rr.sw1_closed():
        robot.main()
        
    if rr.sw1_closed():
        robot.robot_stop()
