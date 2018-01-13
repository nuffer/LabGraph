from labgraph.utils.display.graph.SimpleGraph import SimpleGraph


class RandomDisplay(SimpleGraph):

    def initialize(self):
        print("Random display initialized")
        pass

    def on_input_queue_data(self,pipe_key:str,data):
        print("Random display: "+ str(data))
        self.update()
        pass