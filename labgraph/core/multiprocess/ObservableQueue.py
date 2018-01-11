from multiprocessing import Queue


class ObservableQueue(object):
    def __init__(self):
        self._observers_queues = []

    def register(self, observer: Queue):
        if not observer in self._observers_queues:
            self._observers_queues.append(observer)

    def unregister(self, observer: Queue):
        if observer in self._observers_queues:
            self._observers_queues.remove(observer)

    def unregister_all(self):
        if self._observers_queues:
            del self._observers_queues[:]

    def notify_observers(self, data):
        for observer in self._observers_queues:
            observer.put(data)