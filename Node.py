import time
from Status import TaskStatus
from random import randint
from random import seed


# leaf nodes with no child
# task and condition


def assign_nodes(robot):
    global cleaner
    cleaner = robot


class Node:
    pass


# First kind of node - task


class Condition(Node):
    def run(self):
        return TaskStatus.SUCCESS


class BatteryCheck(Condition):
    def run(self):
        print("Check battery...")
        time.sleep(1)
        if cleaner.BATTERY_LEVEL < 30:
            print("Below 30% \n")
            return TaskStatus.SUCCESS
        else:
            print("Over 30% \n")
            return TaskStatus.FAILURE


class GeneralClean(Condition):
    def run(self):
        print("Check General Clean Command...")
        time.sleep(1)
        if cleaner.GENERAL_CLEANING:
            print("General Clean TRUE\n")
            return TaskStatus.SUCCESS
        else:
            print("General Clean FALSE\n")
            return TaskStatus.FAILURE


class Spot(Condition):
    def run(self):
        print("Check Spot Command...")
        time.sleep(1)
        if cleaner.SPOT_CLEANING:
            print("Spot Clean TRUE\n")
            return TaskStatus.SUCCESS
        else:
            print("Spot Clean FALSE\n")
            return TaskStatus.FAILURE


class DustySpot(Condition):
    def run(self):
        print("Detect Dusty Spot...")
        time.sleep(1)

        value = randint(1, 10)  # random value to decide whether detected or not
        if value <= 5:
            print("DUSTY Spot detected (1-5), Random#: " + str(value))
            cleaner.DUSTY_SPOT = 1
            return TaskStatus.SUCCESS
        else:
            print("DUSTY Spot NOT detected (6-10), Random#: " + str(value))
            cleaner.DUSTY_SPOT = 0
            return TaskStatus.FAILURE


class Task(Node):
    def run(self):
        return TaskStatus.SUCCESS


class FindHome(Task):
    def run(self):

        time.sleep(1)

        print("Finding home path......")
        cleaner.HOME_PATH = input("Please enter a home path......: ")

        if cleaner.HOME_PATH:
            print("Find path success")
            return TaskStatus.SUCCESS
        else:
            print("Error find path")
            return TaskStatus.FAILURE


class GoHome(Task):
    def run(self):

        time.sleep(1)

        print("GO home......")

        if cleaner.HOME_PATH:
            print("FGO HOME success")
            return TaskStatus.SUCCESS
        else:
            print("Error GO HOME")
            return TaskStatus.FAILURE


class DoNothing(Task):
    def run(self):
        time.sleep(1)

        print("Do Nothing......")

        return TaskStatus.SUCCESS


class CleanSpot(Task):
    def run(self, done):
        time.sleep(1)
        if not done:
            print("Keep cleaning spots")
            return TaskStatus.RUNNING
        else:
            print("Clean spots succeed")
            return TaskStatus.SUCCESS


class DoneSpot(Task):

    # run function
    def run(self):
        time.sleep(1)

        print("Done Spot Succeed")
        cleaner.SPOT_CLEANING = 0
        return TaskStatus.SUCCESS


class DoneGeneral(Task):

    # run function
    def run(self):
        time.sleep(1)

        print("Done General Succeed ")
        cleaner.GENERAL_CLEANING = 0
        return TaskStatus.SUCCESS


class CleanFloor(Task):

    # run function
    def run(self):
        # Target: clear spot
        time.sleep(1)

        value = randint(1, 10)
        if value <= 5:
            print("Clean Floor failed (1-5), Random#: " + str(value))
            return TaskStatus.FAILURE
        else:
            print("Clean Floor Succeed (6-10), Random#: " + str(value))
            cleaner.GENERAL_CLEANING = False
            return TaskStatus.SUCCESS


class Dock(Task):
    # run function
    def run(self):
        # Target: clear spot
        time.sleep(1)
        print("Recharging.....")
        cleaner.BATTERY_LEVEL = 100
        return TaskStatus.SUCCESS
