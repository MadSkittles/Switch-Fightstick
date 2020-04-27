from NXController import Controller
from tqdm_helpers import trange

LAPS = 3
N = 17 * 30
SLEEP_AFTER_COLLECTING = False


def fly_to_daycare_at_5(ctrl: Controller):
    ctrl.X(0.1)
    ctrl.pause(0.5)
    ctrl.DOWN(0.5)
    ctrl.LEFT(1.7)

    ctrl.A(0.1)
    ctrl.pause(2)
    ctrl.LEFT(3)
    ctrl.DOWN(5)
    ctrl.pause(0.5)

    ctrl.UP(1.22)
    ctrl.pause(0.5)
    ctrl.RIGHT(0.4)
    ctrl.pause(0.5)
    ctrl.UP(0.07)
    ctrl.pause(0.5)

    ctrl.A(0.3)
    ctrl.A(0.3)
    ctrl.pause(3)


def get_egg(ctrl: Controller):
    ctrl.A()
    ctrl.pause(0.5)
    ctrl.A()
    ctrl.pause(4.5)
    ctrl.B()
    ctrl.pause(2)
    ctrl.B()
    ctrl.pause(1)
    ctrl.B()
    ctrl.pause(1)
    ctrl.B()
    ctrl.pause(1)


def cruise(ctrl: Controller, loop: int):
    for i in range(loop):
        ctrl.LS_UP(0.3)
        ctrl.LS_LEFT(1.5)
        ctrl.LS_UP(0.3)
        if i == loop - 1:
            ctrl.LS_RIGHT(1.55)
            ctrl.LS_UP(0.3)
        else:
            ctrl.LS_RIGHT(1.5)

    ctrl.pause(1)
    get_egg(ctrl)


with Controller() as ctrl:
    # fly_to_daycare_at_5(ctrl)
    N = int(N * 1.25)

    ctrl.LS_LEFT(0.1)
    ctrl.LS_UP(0.5)
    ctrl.LS_RIGHT(0.2)

    for i in trange(N, desc="Collecting", unit="egg"):
        cruise(ctrl, LAPS)

    if SLEEP_AFTER_COLLECTING:
        ctrl.sleepmode()
