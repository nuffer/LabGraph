from labgraph.core.multiprocess import Queue


class InputQueuesConnectors:

    def __init__(self):
        self.input_queues = {}
        pass

    def attach_input_queue(self,key:str, queue: Queue):
        self.input_queues[key] = queue
        return self

    def get_input_queue(self,key:str) -> Queue:
        return self.input_queues[key]

    def notify_input_queue(self,key:str,data):
        self.get_input_queue(key).put(data)
