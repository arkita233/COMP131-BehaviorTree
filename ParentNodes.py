import time
from Status import TaskStatus


def assign_parents(robot):
    global cleaner
    cleaner = robot


class Parents:
    pass


# Decorator

class UntilSucceed(Parents):
    def __init__(self, leaf):
        self.leaf = leaf

    def run(self):
        if cleaner.BATTERY_LEVEL == 0:  # check battery level while running tasks
            print("OUT OF BATTERY")
            return TaskStatus.FAILURE

        time.sleep(1)
        while self.leaf.run() == TaskStatus.FAILURE:
            cleaner.action()
            if cleaner.BATTERY_LEVEL == 0:
                print("OUT OF BATTERY")
                return TaskStatus.FAILURE

        return TaskStatus.SUCCESS


class Timer(Parents):
    def __init__(self, leaf_node, time_left):
        self.leaf = leaf_node
        self.timer = time_left

    def run(self):
        time.sleep(1)
        if cleaner.BATTERY_LEVEL == 0:  # check battery level while running tasks
            print("OUT OF BATTERY")
            return TaskStatus.FAILURE

        print("Set up timer for " + str(self.timer) + " seconds")
        while self.timer > 0:
            self.leaf.run(done=False)
            cleaner.action()
            if cleaner.BATTERY_LEVEL == 0:  # check battery level while running tasks
                print("OUT OF BATTERY")
                return TaskStatus.FAILURE

            self.timer -= 1
            print(str(self.timer) + " seconds left")
        self.leaf.run(done=True)

        return TaskStatus.SUCCESS


# composites
class Sequence(Parents):
    def __init__(self, leaf_node):
        self.leaf = leaf_node

    def run(self):
        for t in self.leaf:
            if t.run() == TaskStatus.FAILURE:
                return TaskStatus.FAILURE
        return TaskStatus.SUCCESS


class Selection(Parents):
    def __init__(self, leaf_node):
        self.leaf = leaf_node

    def run(self):
        for t in self.leaf:
            if t.run() == TaskStatus.SUCCESS:
                return TaskStatus.SUCCESS
        return TaskStatus.FAILURE


class Priority(Parents):  # leaf_node is a dictionary of tasks, index is priority, values are nodes
    def __init__(self, leaf_node):
        self.leaf = leaf_node

    def run(self):
        for key in sorted(self.leaf): # sort tasks by priority
            if self.leaf[key].run() == TaskStatus.SUCCESS:
                return TaskStatus.SUCCESS
        return TaskStatus.FAILURE
