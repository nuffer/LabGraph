from labgraph.core import *
from example.random.RandomAcquisition import RandomAcquisition
from example.random.RandomDisplay import RandomDisplay

if __name__ == '__main__':

    kernel = Kernel()

    aq = RandomAcquisition()
    disp = RandomDisplay()

    kernel.register(aq)
    kernel.register(disp)

    kernel.connect("random",aq,disp)

    kernel.start()
    kernel.join()
    exit(0)
