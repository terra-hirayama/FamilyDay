from rrb3 import *
import robot_controller as robot
import time

def main():
    rr = RRB3()

    while True:
        time.sleep(0.1)
        if rr.sw1_closed():
            robot.main()


if __name__ == '__main__':
    main()
