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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    robot = boot_robot(blackboard)
    bt = Tree()
    bt.run()

    print(robot.BATTERY_LEVEL)








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
