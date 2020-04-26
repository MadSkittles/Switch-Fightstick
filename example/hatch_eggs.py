import math

from NXController import Controller
from tqdm_helpers import trange

CYCLE = 25  # Egg cycles
N = 180  # Number of eggs to receive
current_column = 1
SLEEP_AFTER_HATCHING = True


def move_egg(ctrl: Controller, column: int, start_up=False, reset_postion=False):
    def range_mode():
        for _ in range(2):
            ctrl.Y()
            ctrl.pause(0.1)

    def range_selct():
        ctrl.A()
        ctrl.pause(0.3)
        ctrl.DOWN(0.7)
        ctrl.pause(0.3)
        ctrl.A()
        ctrl.pause(0.3)

    ctrl.X()
    ctrl.pause(0.5)
    if reset_postion:
        ctrl.UP()
        ctrl.pause(0.5)
        ctrl.RIGHT()
        ctrl.pause(0.5)
    ctrl.A()
    ctrl.pause(1.7)
    ctrl.LR()
    ctrl.pause(2)

    if start_up:
        for _ in range(column - 1):
            ctrl.RIGHT()
            ctrl.pause(0.3)
        range_mode()
        range_selct()
        ctrl.pause(0.3)
        for _ in range(column):
            ctrl.LEFT()
            ctrl.pause(0.1)
        ctrl.DOWN()
        ctrl.pause(0.3)
        ctrl.A()
        ctrl.pause(0.5)

    else:
        range_mode()
        ctrl.LEFT()
        ctrl.pause(0.3)
        ctrl.DOWN()
        ctrl.pause(0.3)

        range_selct()
        for _ in range(column):
            ctrl.RIGHT()
            ctrl.pause(0.1)
        ctrl.UP()
        ctrl.pause(0.3)
        ctrl.A()
        ctrl.pause(0.3)

        if column == 6:
            ctrl.R()
            ctrl.pause(0.5)
            for _ in range(5):
                ctrl.LEFT()
                ctrl.pause(0.1)
            column = 0
        else:
            ctrl.RIGHT()
        ctrl.pause(0.1)
        range_selct()
        ctrl.pause(0.3)
        for _ in range(column + 1):
            ctrl.LEFT()
            ctrl.pause(0.1)
        ctrl.DOWN()
        ctrl.pause(0.3)
        ctrl.A()
        ctrl.pause(0.5)

    ctrl.B()
    ctrl.pause(2)
    ctrl.B()
    ctrl.pause(1.7)
    ctrl.B()
    ctrl.pause(1)


def fly_to_daycare(ctrl: Controller):
    ctrl.X()
    ctrl.pause(1)
    ctrl.LS_DOWN(0.5)
    ctrl.LS_LEFT(0.7)
    ctrl.A()
    ctrl.pause(2.5)
    ctrl.A()
    ctrl.pause(0.5)
    ctrl.A()
    ctrl.pause(2.8)


def get_ready_to_hatch(ctrl: Controller):
    ctrl.LS_UP(1.5)
    ctrl.LS_RIGHT(1.8)


with Controller() as ctrl:
    ctrl.buttondelay = 0

    for i in trange(math.ceil(N / 5), desc="Hatching", unit="5 eggs"):
        fly_to_daycare(ctrl)

        if i == 0:
            move_egg(ctrl, current_column, True, True)

        get_ready_to_hatch(ctrl)

        for c in range(CYCLE):
            if c > 0 and c % 20 == 0:
                fly_to_daycare(ctrl)
                get_ready_to_hatch(ctrl)
                continue

            ctrl.LS_RIGHT(0.95)
            ctrl.LS_DOWN(0.95)
            ctrl.LS_LEFT(0.75)
            ctrl.LS_UP(0.75)

        for c in range(5):
            ctrl.A()
            ctrl.pause(15)
            ctrl.A()
            ctrl.pause(5)

            ctrl.LS_DOWN(0.3)
            ctrl.pause(0.5)

        move_egg(ctrl, current_column, reset_postion=True)
        current_column = current_column % 6 + 1

    if SLEEP_AFTER_HATCHING:
        ctrl.sleepmode()
