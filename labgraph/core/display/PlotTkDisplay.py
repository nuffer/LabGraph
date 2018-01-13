import abc
from labgraph.core.display.TkDisplay import *


class TkDisplay(TkDisplay):

    def __init__(self):
        TkDisplay.__init__(self)
        self._plot_frame = Canvas(self)
        self._plot_frame.pack(fill=BOTH,expand=True)
        self._plot_frame.create_line(0,0,50,50,fill="blue")
        pass

    @abc.abstractmethod
    def initialize(self):
        pass


