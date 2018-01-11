from multiprocessing import Queue as BaseQueue


class Queue(BaseQueue):
    def __init__(self):
        BaseQueue.__init__(self)
        pass