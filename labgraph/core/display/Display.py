import abc
from labgraph.core.multiprocess import *


class Display(Process,InputQueuesConnectors):

    def __init__(self):
        Process.__init__(self)
        InputQueuesConnectors.__init__(self)
        pass

    @abc.abstractmethod
    def initialize(self):
        pass

    def loop(self):
        for key,queue in self.input_queues.items():
            data = queue.get(True)
            self.on_input_queue_data(key,data)
        pass

    @abc.abstractmethod
    def on_input_queue_data(self,pipe_key:str,data):
        pass

    def run(self):
        self.initialize()
        while (True):
            self.loop()
