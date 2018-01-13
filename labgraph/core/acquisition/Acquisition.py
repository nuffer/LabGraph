import abc
from labgraph.core.multiprocess import *


class Acquisition(Process,OutputQueuesConnectors):

    def __init__(self):
        Process.__init__(self)
        OutputQueuesConnectors.__init__(self)
        pass

    @abc.abstractclassmethod
    def initialize(self):
        pass

    @abc.abstractclassmethod
    def loop(self):
        pass

    def run(self):
        self.initialize()
        while(True):
            self.loop()







