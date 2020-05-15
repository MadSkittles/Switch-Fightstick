from NXController import Controller
from pokemon_bot import PokemonBot

COLLECTING_NEEDED = True
HATCHING_NEEDED = True

N_COLLECTING = 18 * 30
LAPS = 3

N_HATCHING = 11 * 30 - 10
CYCLE = 20
CURRENT_COLUMN = 3

PLACEHOLDER_MOVE_PACE = -11

SLEEP_AFTER_COMPLETION = True
NO_EGG_LEFT_MODE = False

if __name__ == "__main__":
    with Controller() as ctrl:
        bot = PokemonBot(ctrl)
        if COLLECTING_NEEDED:
            bot.collect_eggs(N_COLLECTING, LAPS, not HATCHING_NEEDED and SLEEP_AFTER_COMPLETION)
            ctrl.pause(1)

        if COLLECTING_NEEDED and HATCHING_NEEDED:
            ctrl.release()
            bot.fly_to_daycare_at_bridgefield()
            ctrl.pause(1)
            bot.move_placeholder_pokemon(PLACEHOLDER_MOVE_PACE)
            ctrl.pause(1)

        if HATCHING_NEEDED:
            ctrl.release()
            bot.hatch_eggs(N_HATCHING, CYCLE, CURRENT_COLUMN, SLEEP_AFTER_COMPLETION, NO_EGG_LEFT_MODE)
