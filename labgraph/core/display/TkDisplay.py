import abc
from tkinter import *
from labgraph.core.display.Display import *


class TkDisplay(Display,Frame):

    def __init__(self):
        Display.__init__(self)
        self._root = Tk()
        Frame.__init__(self,self._root,width=500,height=500)
        self.pack(fill=BOTH,expand=True,padx=20,pady=20)
        pass

    @abc.abstractmethod
    def initialize(self):
        pass

    def loop(self):
        print("call loop tk")
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
