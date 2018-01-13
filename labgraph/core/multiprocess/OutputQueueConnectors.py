from labgraph.core.multiprocess import Queue


class OutputQueuesConnectors:

    def __init__(self):
        self.output_queues = {}
        pass

    def attach_output_queue(self,key:str, queue: Queue):
        self.output_queues[key] = queue
        return self

    def get_output_queue(self,key:str) -> Queue:
        return self.output_queues[key]

    def notify_output_queue(self,key:str,data):
        self.get_output_queue(key).put(data)
