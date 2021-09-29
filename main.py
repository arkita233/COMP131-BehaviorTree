# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from TreePresentation import *
from Robot import *

blackboard = {
    "BATTERY_LEVEL": 10,
    "SPOT_CLEANING": 0,
    "GENERAL_CLEANING": 1,
    "DUSTY_SPOT": 1,
    "HOME_PATH": ""
}


# update blackboard from user input
def updateBoard():
    print("Start getting blackboard")

    while True:
        try:
            blackboard["BATTERY_LEVEL"] = int(input("Please enter BATTERY_LEVEL (0-100): "))
            blackboard["SPOT_CLEANING"] = int(input("Please enter SPOT_CLEANING (0/1): "))
            blackboard["GENERAL_CLEANING"] = int(input("Please enter GENERAL_CLEANING (0/1): "))
            blackboard["HOME_PATH"] = ""
            break
        except ValueError:
            print("Please enter right value")
            continue

    return blackboard


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # keep running until user wants to stop
    while True:
        blackboard = updateBoard()
        robot = boot_robot(blackboard)

        bt = Tree()
        bt.run()
        print("BATTERY_LEVEL: %d" % robot.BATTERY_LEVEL)
        print("SPOT_CLEANING: %d" % robot.SPOT_CLEANING)
        print("GENERAL_CLEANING: %d" % robot.GENERAL_CLEANING)
        print("DUSTY_SPOT: %d" % robot.DUSTY_SPOT)
        print("HOME_PATH: %s" % robot.HOME_PATH)

        keep = int(input("Run again? (0/1): "))
        while True:
            if keep != 0 and keep != 1:
                keep = int(input("Please enter 0 or 1: "))
                continue
            else:
                break
        if keep == 0:
            print("Stop running")
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
