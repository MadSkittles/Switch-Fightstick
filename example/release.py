from NXController import Controller
from tqdm_helpers import trange

start_index = 1
N = 30  # Number of Pokemon

with Controller() as ctr:
    for ii in trange(start_index - 1, N, desc="Releasing", unit="egg"):
        ctr.A()
        ctr.pause(0.5)
        ctr.UP()
        ctr.UP()
        ctr.A()
        ctr.pause(0.7)
        ctr.UP()
        ctr.A()
        ctr.pause(1.3)
        ctr.A()
        ctr.pause(0.3)
        # Move to next
        ctr.RIGHT()

        # Change row
        if ii % 6 == 5:
            ctr.RIGHT()
            ctr.DOWN()

        # Change boxs
        if ii % 30 == 29:
            ctr.R()
            ctr.pause(0.5)
            ctr.DOWN()
            ctr.DOWN()

        ctr.pause(0.3)
