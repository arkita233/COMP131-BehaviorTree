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
        time.sleep(1)
        while self.leaf.run() == TaskStatus.FAILURE:
            cleaner.action()

        return TaskStatus.SUCCESS


class Timer(Parents):
    def __init__(self, leaf_node, time_left):
        self.leaf = leaf_node
        self.timer = time_left

    def run(self):
        time.sleep(1)
        print("Set up timer for " + str(self.timer) + " seconds")
        while self.timer > 0:
            self.leaf.run(done=False)
            cleaner.action()
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


class Priority(Parents):
    def __init__(self, leaf_node):
        self.leaf = leaf_node

    def run(self):
        for key in sorted(self.leaf):
            if self.leaf[key].run() == TaskStatus.SUCCESS:
                return TaskStatus.SUCCESS
        return TaskStatus.FAILURE
