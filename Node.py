import time
from Status import TaskStatus


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
            print("Below 30% TRUE\n")
            return TaskStatus.SUCCESS
        else:
            print("Over 30% FALSE\n")
            return TaskStatus.FAILED


class Task(Node):
    def run(self):
        return TaskStatus.SUCCESS


class FindHome(Task):
    def run(self):

        time.sleep(1)

        print("Finding home path......")
        cleaner["HOME_PATH"] = input("Please enter a home path......")

        if cleaner["HOME_PATH"]:
            print("Find path success")
            return TaskStatus.SUCCESS
        else:
            print("Error find path")
            return TaskStatus.FAILURE


class GoHome(Task):
    def run(self):

        time.sleep(1)

        print("GO home......")

        if cleaner["HOME_PATH"]:
            print("FGO HOME success")
            return TaskStatus.SUCCESS
        else:
            print("Error GO HOME")
            return TaskStatus.FAILURE
