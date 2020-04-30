from NXController import Controller
from pokemon_bot import PokemonBot

LAPS = 3
N = 74
SLEEP_AFTER_COLLECTING = True

if __name__ == "__main__":
    with Controller() as ctrl:
        bot = PokemonBot(ctrl)
        bot.collect_eggs(N, LAPS, SLEEP_AFTER_COLLECTING)
