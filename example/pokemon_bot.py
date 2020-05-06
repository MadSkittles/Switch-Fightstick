import math

from NXController import Controller
from tqdm_helpers import trange


class PokemonBot:
    def __init__(self, controller: Controller):
        self.controller = controller

    def collect_eggs(self, egg_quantity: int, laps: int, sleep_after_collecting=True):
        egg_quantity = int(egg_quantity * 1.25)

        self.controller.LS_LEFT(0.1)
        self.controller.LS_UP(0.5)
        self.controller.LS_RIGHT(0.2)

        for i in trange(egg_quantity, desc="Collecting", unit="egg"):
            self._cruise(laps)

        if sleep_after_collecting:
            self.controller.sleepmode()

    def hatch_eggs(
        self,
        egg_quantity: int,
        cycles: int,
        current_column_index=1,
        sleep_after_collecting=True,
    ):
        self.controller.buttondelay = 0

        for i in trange(math.ceil(egg_quantity / 5), desc="Hatching", unit="5 eggs"):
            self.fly_in_situ()

            if i == 0:
                self._move_egg(current_column_index, True, True)

            self._get_ready_to_hatch()

            for c in range(cycles):
                if c > 0 and c % 20 == 0:
                    self.fly_in_situ()
                    self._get_ready_to_hatch()
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

            self._move_egg(current_column_index, reset_postion=(i > 0 or cycles > 20))
            current_column_index = current_column_index % 6 + 1

        if sleep_after_collecting:
            self.controller.sleepmode()

    def move_placeholder_pokemon(self, box_move_pace: int):
        self.controller.X()
        self.controller.pause(0.5)
        self.controller.UP()
        self.controller.pause(0.5)
        self.controller.RIGHT()
        self.controller.pause(0.5)
        self.controller.A()
        self.controller.pause(1.7)
        self.controller.LR()
        self.controller.pause(2)

        for _ in range(abs(box_move_pace)):
            if box_move_pace < 0:
                self.controller.L()
                self.controller.pause(0.3)
            else:
                self.controller.R()
                self.controller.pause(0.3)

        self._switch_range_select_mode()
        self.controller.LEFT()
        self.controller.pause(0.3)
        self.controller.DOWN()
        self.controller.pause(0.3)

        self._range_selct()
        self.controller.RIGHT()
        self.controller.pause(0.1)
        self.controller.UP()
        self.controller.pause(0.3)
        self.controller.A()
        self.controller.pause(0.3)

        for _ in range(abs(box_move_pace)):
            if box_move_pace > 0:
                self.controller.L()
                self.controller.pause(0.3)
            else:
                self.controller.R()
                self.controller.pause(0.3)

        self.controller.B()
        self.controller.pause(2)
        self.controller.B()
        self.controller.pause(1.7)
        self.controller.B()
        self.controller.pause(1)

    def fly_to_daycare_at_bridgefield(self):
        self.controller.X(0.1)
        self.controller.pause(0.5)
        self.controller.DOWN(0.5)
        self.controller.LEFT(1.7)
        self.controller.A(0.1)
        self.controller.pause(2)

        self.controller.LEFT(3)
        self.controller.DOWN(5)
        self.controller.pause(0.5)

        self.controller.UP(1.12)
        self.controller.pause(0.5)
        self.controller.RIGHT(0.65)
        self.controller.pause(0.5)

        self.controller.A(0.3)
        self.controller.A(0.3)
        self.controller.pause(10)

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
        self._get_egg()

    def _switch_range_select_mode(self):
        for _ in range(2):
            self.controller.Y()
            self.controller.pause(0.1)

    def _range_selct(self):
        self.controller.A()
        self.controller.pause(0.3)
        self.controller.DOWN(0.7)
        self.controller.pause(0.3)
        self.controller.A()
        self.controller.pause(0.3)

    def _move_egg(self, column: int, start_up=False, reset_postion=False):
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
            for _ in range(column - 1):
                self.controller.RIGHT()
                self.controller.pause(0.3)
            self._switch_range_select_mode()
            self._range_selct()
            self.controller.pause(0.3)
            for _ in range(column):
                self.controller.LEFT()
                self.controller.pause(0.1)
            self.controller.DOWN()
            self.controller.pause(0.3)
            self.controller.A()
            self.controller.pause(0.5)

        else:
            self._switch_range_select_mode()
            self.controller.LEFT()
            self.controller.pause(0.3)
            self.controller.DOWN()
            self.controller.pause(0.3)

            self._range_selct()
            for _ in range(column):
                self.controller.RIGHT()
                self.controller.pause(0.1)
            self.controller.UP()
            self.controller.pause(0.3)
            self.controller.A()
            self.controller.pause(0.3)

            if column == 6:
                self.controller.R()
                self.controller.pause(0.5)
                for _ in range(5):
                    self.controller.LEFT()
                    self.controller.pause(0.1)
                column = 0
            else:
                self.controller.RIGHT()
            self.controller.pause(0.1)
            self._range_selct()
            self.controller.pause(0.3)
            for _ in range(column + 1):
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


if __name__ == "__main__":
    with Controller() as ctrl:
        bot = PokemonBot(ctrl)
        bot.fly_to_daycare_at_bridgefield()
