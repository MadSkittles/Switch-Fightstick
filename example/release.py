from tqdm import trange

from NXController import Controller

start_index = 1
N = 157  # Number of Pokemon

with Controller() as ctr:
    for ii in trange(start_index - 1, N, unit="egg"):
        print(f"{ii+1}/{N} released")
        ctr.A()
        ctr.pause(0.1)
        ctr.UP()
        ctr.UP()
        ctr.A()
        ctr.pause(0.7)
        ctr.UP()
        ctr.A()
        ctr.pause(1.3)
        ctr.A()

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
