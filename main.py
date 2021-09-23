# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Robot import boot_robot

blackboard = {
    "BATTERY_LEVEL": 100,
    "SPOT_CLEANING": 1,
    "GENERAL_CLEANING": 1,
    "DUSTY_SPOT": 1,
    "HOME_PATH": ""
}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cleaner = boot_robot(blackboard)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
