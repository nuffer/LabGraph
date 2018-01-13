from multiprocessing import Process as BaseProcess


class Processing(BaseProcess):

    def __init__(self):
        BaseProcess.__init__(self)
        pass
