from Node import *

from ParentNodes import *


class Tree:
    def run(self):
        bt = Priority(leaf_node={1: Sequence(leaf_node=[BatteryCheck(), FindHome(), GoHome(), Dock()]), 2: Selection(
            leaf_node=[Sequence(leaf_node=[Spot(), Timer(leaf_node=CleanSpot(), time_left=20), DoneSpot()]), Sequence(
                leaf_node=[GeneralClean(), Sequence(leaf_node=[Priority(
                    leaf_node={1: Sequence(leaf_node=[DustySpot(), Timer(leaf_node=CleanSpot(), time_left=35)]),
                               2: UntilSucceed(leaf=CleanFloor())}), DoneGeneral()])])]), 3: DoNothing()}).run()
        return bt
