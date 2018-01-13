from labgraph.core import *
import random
from labgraph.utils.timing import wait


class RandomAcquisition(Acquisition):

    def initialize(self):
        print("random was initialized")
        pass

    def loop(self):

        num = random.random()

        print(num)
        self.notify_output_queue("random", num)

        wait.wait_seconds(1)
        pass