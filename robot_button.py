from rrb3 import *
import robot_controller as robot

def main():
    rr = RRB3()

    while True:
        print(rr.sw1_closed())
        if rr.sw1_closed():
            robot.main()


if __name__ == '__main__':
    main()
