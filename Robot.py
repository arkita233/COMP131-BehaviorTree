from Node import assign_nodes


class Robot:
    # constructor
    def __init__(self, dic):
        self.BATTERY_LEVEL = dic["BATTERY_LEVEL"]
        self.SPOT_CLEANING = dic["SPOT_CLEANING"]
        self.GENERAL_CLEANING = dic["GENERAL_CLEANING"]
        self.DUSTY_SPOT = dic["DUSTY_SPOT"]
        self.HOME_PATH = dic["HOME_PATH"]

    # decreases blackboard battery
    def action(self):
        self.BATTERY_LEVEL -= 1


def boot_robot(board):
    cleaner = Robot(board)
    assign_nodes(cleaner)