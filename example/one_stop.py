from NXController import Controller
from pokemon_bot import PokemonBot

COLLECTING_ONLY = False
HATCHING_ONLY = False

N_COLLECTING = 360
LAPS = 3

N_HATCHING = 360
CYCLE = 20
CURRENT_COLUMN = 1

SLEEP_AFTER_COMPLETION = True

if __name__ == "__main__":
    with Controller() as ctrl:
        bot = PokemonBot(ctrl)
        if not HATCHING_ONLY:
            bot.collect_eggs(N_COLLECTING, LAPS, COLLECTING_ONLY and SLEEP_AFTER_COMPLETION)
            ctrl.pause(1)
        if not COLLECTING_ONLY and not HATCHING_ONLY:
            bot.fly_to_daycare_at_bridgefield()
            ctrl.pause(1)
            bot.move_placeholder_pokemon(-10)
            ctrl.pause(1)
        if not COLLECTING_ONLY:
            bot.hatch_eggs(N_HATCHING, CYCLE, CURRENT_COLUMN, SLEEP_AFTER_COMPLETION)
