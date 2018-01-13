from labgraph.core.multiprocess import *


class Kernel:

    def __init__(self):
        self.processes = []
        pass

    def register(self,process: Process):
        self.processes.append(process)
        return self

    def start(self):
        for process in self.processes:
            if isinstance(process,Process):
                process.start()

    def join(self):
        for process in self.processes:
            if isinstance(process,Process):
                process.join()

    def connect(self,key:str ,output_process: OutputQueuesConnectors, input_process: InputQueuesConnectors):
        queue = Queue()
        output_process.attach_output_queue(key,queue)
        input_process.attach_input_queue(key,queue)
        return self




