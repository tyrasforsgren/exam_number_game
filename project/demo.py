"""
number_game_demo

This script demonstrates how to create and start a number guessing game
using the 'MyGamer' and 'NumberGame' classes from the 'gamer_module'
and 'number_game' modules, respectively.

Usage:
1. Import the necessary classes: 'MyGamer' and 'NumberGame'.
2. Create a player ('MyGamer') instance with name and birthdate.
3. Create a game ('NumberGame') instance for the player.
4. Start the number guessing game by calling the 'game_loop' method.

Example
-------
gamer = MyGamer('Tyra Forsgren', "20030717")
game = NumberGame(gamer)
game.game_loop(begin=True)

"""

from gamer_module import MyGamer
from number_game import NumberGame

if __name__ == '__main__':
    # Create a MyGamer instance with player data.
    # - Name: 'Tyra Forsgren'
    # - Birthdate: '20030717' (July 17, 2003)
    gamer = MyGamer('Tyra Forsgren', "20030717") # Change these to demo errors

    # Create a NumberGame instance for the player.
    game = NumberGame(gamer)

    # Start the number guessing game by calling the game_loop method.
    # - 'begin=True' means that this is the first game round.
    game.game_loop(begin=True)
