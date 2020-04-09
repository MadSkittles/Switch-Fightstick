from NXController import Controller

N = 90  # Number of Pokemon

with Controller() as ctr:
    for ii in range(N):
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
            ctr.DOWN()
            ctr.DOWN()
