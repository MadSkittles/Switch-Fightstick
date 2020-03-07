from NXController import Controller
from datetime import date, timedelta


def change_date(now=date.today(), steps=float("inf")):
    index = 0
    while index < steps:
        next_day = now + timedelta(days=1)
        yield (next_day.year != now.year, next_day.month != now.month)
        now = next_day
        index += 1


def save(ctrl: Controller):
    ctrl.X()
    ctrl.pause(0.5)
    ctrl.R()
    ctrl.pause(1.5)
    ctrl.A()
    ctrl.pause(4)


with Controller() as ctrl:
    index = 1
    for year_change, month_change in change_date(steps=200):
        print(f"Loop: {index}")

        ctrl.A()
        ctrl.pause(0.3)
        ctrl.A()
        ctrl.pause(0.3)
        ctrl.A()
        ctrl.pause(0.3)
        ctrl.A()
        ctrl.pause(3.5)
        ctrl.HOME()
        ctrl.pause(0.5)
        ctrl.DOWN()
        ctrl.RIGHT(0.5)
        ctrl.A()
        ctrl.pause(0.5)
        ctrl.DOWN(1.5)
        ctrl.A()
        ctrl.DOWN(0.6)
        ctrl.A()
        ctrl.pause(0.5)
        ctrl.DOWN(0.4)
        ctrl.A()
        ctrl.pause(0.5)
        if year_change:
            ctrl.UP()
        ctrl.RIGHT()
        ctrl.RIGHT()
        ctrl.UP()
        if month_change:
            ctrl.LEFT()
            ctrl.UP()
            ctrl.RIGHT()
        ctrl.RIGHT(0.5)
        ctrl.A()
        ctrl.HOME()
        ctrl.pause(0.5)
        ctrl.A()
        ctrl.pause(0.5)
        ctrl.B()
        ctrl.pause(0.5)
        ctrl.A()
        ctrl.pause(5)

        if index % 50 == 0:
            save(ctrl)
        index += 1
    
    ctrl.sleepmode()

