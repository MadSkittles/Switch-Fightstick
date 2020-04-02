from NXController import Controller
import math

CYCLE = 20  # Egg cycles
N = 35  # Number of eggs to receive
current_column = 6
MOVE_EGG_ON_STARTUP = True
SLEEP_AFTER_HATCHING = True


def move_egg(ctr: Controller, column: int, start_up=False, reset_postion=False):
    def range_mode():
        for _ in range(2):
            ctr.Y()
            ctr.pause(0.1)

    def range_selct():
        ctr.A()
        ctr.pause(0.3)
        ctr.DOWN(0.7)
        ctr.pause(0.3)
        ctr.A()
        ctr.pause(0.3)

    ctr.X()
    ctr.pause(0.5)
    if reset_postion:
        ctr.UP()
        ctr.pause(0.5)
        ctr.RIGHT()
        ctr.pause(0.5)
    ctr.A()
    ctr.pause(1.7)
    ctr.LR()
    ctr.pause(2)

    if start_up:
        for _ in range(column - 1):
            ctr.RIGHT()
            ctr.pause(0.3)
        range_mode()
        range_selct()
        ctr.pause(0.3)
        for _ in range(column):
            ctr.LEFT()
            ctr.pause(0.1)
        ctr.DOWN()
        ctr.pause(0.3)
        ctr.A()
        ctr.pause(0.5)

    else:
        range_mode()
        ctr.LEFT()
        ctr.pause(0.3)
        ctr.DOWN()
        ctr.pause(0.3)

        range_selct()
        for _ in range(column):
            ctr.RIGHT()
            ctr.pause(0.1)
        ctr.UP()
        ctr.pause(0.3)
        ctr.A()
        ctr.pause(0.3)

        if column == 6:
            ctr.R()
            ctr.pause(0.5)
            for _ in range(5):
                ctr.LEFT()
                ctr.pause(0.1)
            column = 0
        else:
            ctr.RIGHT()
        ctr.pause(0.1)
        range_selct()
        ctr.pause(0.3)
        for _ in range(column + 1):
            ctr.LEFT()
            ctr.pause(0.1)
        ctr.DOWN()
        ctr.pause(0.3)
        ctr.A()
        ctr.pause(0.5)

    ctr.B()
    ctr.pause(2)
    ctr.B()
    ctr.pause(1.7)
    ctr.B()
    ctr.pause(1)


with Controller() as ctr:
    ctr.buttondelay = 0

    for i in range(math.ceil(N / 5)):
        # Fly to Day Care in Wild Area
        ctr.X()
        ctr.pause(1)
        ctr.LS_DOWN(0.5)
        ctr.LS_LEFT(0.7)
        ctr.A()
        ctr.pause(2.5)
        ctr.A()
        ctr.pause(0.5)
        ctr.A()
        ctr.pause(2.8)

        if i == 0 and MOVE_EGG_ON_STARTUP:
            move_egg(ctr, current_column, True, True)

        ctr.LS_UP(1.5)
        ctr.LS_RIGHT(1.8)

        for c in range(CYCLE):
            print(f"Loop #{c+1}")
            ctr.LS_RIGHT(0.95)
            ctr.LS_DOWN(0.95)
            ctr.LS_LEFT(0.75)
            ctr.LS_UP(0.75)

        for c in range(5):
            print(f"Get egg #{i*5+c+1}")

            ctr.A()
            ctr.pause(15)
            ctr.A()
            ctr.pause(5)

            ctr.LS_DOWN(0.3)
            ctr.pause(0.5)

        move_egg(ctr, current_column, reset_postion=i != 0 or not MOVE_EGG_ON_STARTUP)
        current_column = current_column % 6 + 1

    if SLEEP_AFTER_HATCHING:
        ctr.sleepmode()
