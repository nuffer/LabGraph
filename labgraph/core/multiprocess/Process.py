from multiprocessing import Process as BaseProcess


class Process(BaseProcess):

    def __init__(self):
        BaseProcess.__init__(self)
        pass