# pylint: disable=import-error

from gamer_module import MyGamer
from number_game import NumberGame

print('\n\n\n')

if __name__ == '__main__':
    gamer = MyGamer('dfg dfg',20030717)
    game = NumberGame(gamer)
    game.game_loop(begin=True)

# Check for pot errors

# DO THE TESTING ALREADY
# Do in GiT + additional files ??