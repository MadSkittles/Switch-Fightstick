import math

from tqdm import trange

from NXController import Controller


class PokemonBot:
    def __init__(self, controller: Controller):
        self.controller = controller

    def collect_eggs(self, egg_quantity: int, laps: int, sleep_after_collecting=True):
        self.controller.LS_LEFT(0.1)
        self.controller.LS_UP(0.5)
        self.controller.LS_RIGHT(0.2)

        for i in trange(egg_quantity, desc="Collecting", unit="egg"):
            self._cruise(self.controller, laps)

        if sleep_after_collecting:
            self.controller.sleepmode()

    def hatch_eggs(self, egg_quantity: int, cycles: int, current_column_index=0, sleep_after_collecting=True):
        self.controller.buttondelay = 0

        for i in trange(math.ceil(egg_quantity / 5), desc="Hatching", unit="5 eggs"):
            fly_in_situ(self.controller)

            if i == 0:
                _move_egg(self.controller, current_column_index, True, True)

            self._get_ready_to_hatch(self.controller)

            for c in range(cycles):
                if c > 0 and c % 20 == 0:
                    self.fly_in_situ(self.controller)
                    self._get_ready_to_hatch(self.controller)
                    continue

                self.controller.LS_RIGHT(0.95)
                self.controller.LS_DOWN(0.95)
                self.controller.LS_LEFT(0.75)
                self.controller.LS_UP(0.75)

            for c in range(5):
                self.controller.A()
                self.controller.pause(15)
                self.controller.A()
                self.controller.pause(5)

                self.controller.LS_DOWN(0.3)
                self.controller.pause(0.5)

            _move_egg(self.controller, current_column_index, reset_postion=True)
            current_column_index = current_column_index % 6 + 1

        if sleep_after_collecting:
            self.controller.sleepmode()

    def fly_to_daycare_at_5(self):
        self.controller.X(0.1)
        self.controller.pause(0.5)
        self.controller.DOWN(0.5)
        self.controller.LEFT(1.7)

        self.controller.A(0.1)
        self.controller.pause(2)
        self.controller.LEFT(3)
        self.controller.DOWN(5)
        self.controller.pause(0.5)

        self.controller.UP(1.22)
        self.controller.pause(0.5)
        self.controller.RIGHT(0.4)
        self.controller.pause(0.5)
        self.controller.UP(0.07)
        self.controller.pause(0.5)

        self.controller.A(0.3)
        self.controller.A(0.3)
        self.controller.pause(3)

    def _get_egg(self):
        self.controller.A()
        self.controller.pause(0.5)
        self.controller.A()
        self.controller.pause(4.5)
        self.controller.B()
        self.controller.pause(2)
        self.controller.B()
        self.controller.pause(1)
        self.controller.B()
        self.controller.pause(1)
        self.controller.B()
        self.controller.pause(1)

    def _cruise(self, loop: int):
        for i in range(loop):
            self.controller.LS_UP(0.3)
            self.controller.LS_LEFT(1.5)
            self.controller.LS_UP(0.3)
            if i == loop - 1:
                self.controller.LS_RIGHT(1.55)
                self.controller.LS_UP(0.3)
            else:
                self.controller.LS_RIGHT(1.5)

        self.controller.pause(1)
        self._get_egg(self.controller)

    def _move_egg(self, strt_column: int, start_up=False, reset_postion=False):
        def switch_range_select_mode():
            for _ in range(2):
                self.controller.Y()
                self.controller.pause(0.1)

        def range_selct():
            self.controller.A()
            self.controller.pause(0.3)
            self.controller.DOWN(0.7)
            self.controller.pause(0.3)
            self.controller.A()
            self.controller.pause(0.3)

        self.controller.X()
        self.controller.pause(0.5)
        if reset_postion:
            self.controller.UP()
            self.controller.pause(0.5)
            self.controller.RIGHT()
            self.controller.pause(0.5)
        self.controller.A()
        self.controller.pause(1.7)
        self.controller.LR()
        self.controller.pause(2)

        if start_up:
            for _ in range(strt_column - 1):
                self.controller.RIGHT()
                self.controller.pause(0.3)
            switch_range_select_mode()
            range_selct()
            self.controller.pause(0.3)
            for _ in range(strt_column):
                self.controller.LEFT()
                self.controller.pause(0.1)
            self.controller.DOWN()
            self.controller.pause(0.3)
            self.controller.A()
            self.controller.pause(0.5)

        else:
            switch_range_select_mode()
            self.controller.LEFT()
            self.controller.pause(0.3)
            self.controller.DOWN()
            self.controller.pause(0.3)

            range_selct()
            for _ in range(strt_column):
                self.controller.RIGHT()
                self.controller.pause(0.1)
            self.controller.UP()
            self.controller.pause(0.3)
            self.controller.A()
            self.controller.pause(0.3)

            if strt_column == 6:
                self.controller.R()
                self.controller.pause(0.5)
                for _ in range(5):
                    self.controller.LEFT()
                    self.controller.pause(0.1)
                strt_column = 0
            else:
                self.controller.RIGHT()
            self.controller.pause(0.1)
            range_selct()
            self.controller.pause(0.3)
            for _ in range(strt_column + 1):
                self.controller.LEFT()
                self.controller.pause(0.1)
            self.controller.DOWN()
            self.controller.pause(0.3)
            self.controller.A()
            self.controller.pause(0.5)

        self.controller.B()
        self.controller.pause(2)
        self.controller.B()
        self.controller.pause(1.7)
        self.controller.B()
        self.controller.pause(1)

    def fly_in_situ(self):
        self.controller.X()
        self.controller.pause(1)
        self.controller.LS_DOWN(0.5)
        self.controller.LS_LEFT(0.7)
        self.controller.A()
        self.controller.pause(2.5)
        self.controller.A()
        self.controller.pause(0.5)
        self.controller.A()
        self.controller.pause(2.8)

    def _get_ready_to_hatch(self):
        self.controller.LS_UP(1.5)
        self.controller.LS_RIGHT(1.8)
