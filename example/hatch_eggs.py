import math

from NXController import Controller
from pokemon_bot import PokemonBot

CYCLE = 20  # Egg cycles
N = 12 * 30 - 5  # Number of eggs to receive
current_column = 3
SLEEP_AFTER_HATCHING = True


if __name__ == "__main__":
    with Controller() as ctrl:
        bot = PokemonBot(ctrl)
        bot.hatch_eggs(N, CYCLE, current_column, SLEEP_AFTER_HATCHING)
