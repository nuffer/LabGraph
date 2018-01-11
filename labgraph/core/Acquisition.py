from multiprocessing import Process as BaseProcess


class Acquisition(BaseProcess):

    def __init__(self):
        BaseProcess.__init__(self)
        pass

    def run(self):

        