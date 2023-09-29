
'''
number_game Module

This module holds the game logic for a game about guessing numbers. The
goal is to guess correctly a 'lucky number' from a list of generated numbers.
By every try the game gets a little easier with reductions made to the list
of potential guesses. When the game is won, the results are saved to a CSV.

Classes
-------
NumberGame
    holds game logic

Example usage
-------------
gamer = MyGamer('Tyra Forsgren',20030717)
game = NumberGame(gamer)
game.game_loop(begin=True)

Notes:
The class is dependant on the module gamer_module that handles validation
for user data.

'''

import sys
import random
import pandas as pd
from gamer_module import MyGamer


class NumberGame():
    """
    NumbersGame is a class for handling the game logic for a number-guessing
    game.

    It provides methods mainly for interaction with the player like
    menus and guessing, but also number generation, list simplification and
    saving data.

    Attributes
    ----------
    gamer : MyGamer
        Instance of class holding users data.
    lucky_nr : int
        Winning number
    lucky_list : list
        List containing random numbers including the lucky_nr.
    tries : int
        Count flag for the amount of guesses user has done.
    path : str
        Path to the game data CSV file.
    save_file : pandas.DataFrame
        DataFrame containing game data.

    Methods
    -------
    game_loop(begin):
        Manages game chronology.
    start_menu():
        Handles the player interface at the start menu.
    win_menu():
        Handles the output if the user has won, saves,
        and returns to main menu.
    take_guess():
        Recieves and validates the dttype players guesses.
    generate_lucky_list():
        Generates a list of random numbers 0-100 without repeats and adds
        the winning number.
    generate_lucky_number():
        Generates the winning number.
    check_guess(guess):
        Validates the guess and checks if it is the winning number.
    shorten_list():
        Shortens the list of options depending on how many tries there've been.
    show_satas():
        Prints the data from the game save file.
    save_to_csv():
        Saves game results to th game data file.

    """

    def __init__(self, the_gamer: MyGamer) -> None:
        """Initializes the NumberGame instance.

        Parameters
        ----------
        the_gamer : MyGamer
            Instance holding users data.

        Returns
        -------
        None

        """
        self.gamer = the_gamer
        self.lucky_nr = self.generate_lucky_nr()
        self.lucky_list = self.generate_lucky_list()
        self.tries = 0
        self.path = 'docs/game_save.csv'
        self.save_file = pd.read_csv(self.path)

    def game_loop(self, begin: bool) -> None:
        """Manages game chronology

        This method starts the main menu, iterates the user guessing and
        initiates the winning menu.

        Parameters
        ----------
        begin : bool
            Flag to check if it is the first game round or not.

        Returns
        -------
        None

        """
        if begin:
            self.start_menu()

        win_flag = False
        while win_flag is not True:
            win_flag = self.check_guess(self.take_guess())
        self.win_menu()

    # Player interface
    def start_menu(self) -> None:
        """Handles the player interface at the start menu.

        This method prompts+begins the users next action. The choices are:
        to quit, to play, or to see gamestats.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        prompt = \
            '\nPLAY [P]\n'\
            'SEE STATS [S]\n'\
            'QUIT [Q]\n\n'

        choice = input(prompt)
        while True:
            # print('loop')
            if choice.lower() == 'q':  # QUIT GAME
                q_choice = input('ARE YOU SURE [Y]')
                if q_choice.lower() == 'y':
                    sys.exit()
                    break

            elif choice.lower() == 's':  # SEE STATS
                self.show_stats()
                break

            elif choice.lower() == 'p':  # PLAY GAME
                self.game_loop(begin=False)
                break

            choice = input(prompt)

    def win_menu(self) -> None:
        """Handles the output if the user has won, saves,
        and returns to main menu.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        print('\nGongrats, game is over!\n'
              f'And you got the lucky number on try#{self.tries}')
        self.save_to_csv()
        print('Your results have been saved.')
        self.game_loop(begin=True)

    def take_guess(self) -> int:
        """Recieves and validates the dtype of players guesses.

        Parameters
        ----------
        None

        Returns
        -------
        int
            the players guess converted to int

        """
        self.tries += 1
        player_input = ''
        while player_input.isnumeric() is not True:
            player_input = (input(
                f'Lucky number list: {self.lucky_list} \n'
                f'Your guess: '))
        return int(player_input)

    # Generation
    def generate_lucky_list(self) -> list:
        """Generates a list of random numbers 0-100 without
        repeats and add winning number.

        Parameters
        ----------
        None

        Returns
        -------
        list
            list of random numbers

        """
        luck_list = []
        while len(luck_list) < 9:
            ran = random.randint(0, 100)
            if ran not in luck_list and ran != self.lucky_nr:
                luck_list.append(ran)

        luck_list.append(self.lucky_nr)
        luck_list.sort()
        return luck_list

    def generate_lucky_nr(self) -> int:
        """Generates the winning number.

        Parameters
        ----------
        None

        Returns
        -------
        int
            the winning number

        """
        return random.randint(0, 100)

    def check_guess(self, guess: int) -> bool:
        """Validates the guess and checks if it is the winning number.

        Parameters
        ----------
        guess : int
            the usesrs guess

        Returns
        -------
        bool
            Wether or not the guess was right.
        """
        if guess == self.lucky_nr:
            return True
        if guess in self.lucky_list:
            print(f'\nYou guessed the wrong number. Tries = {self.tries} \n'
                  'Let\'s make it a bit easier!\n')
            self.lucky_list.remove(guess)
            self.shorten_list()
            return False
        print('Your guess is not in the list.')
        self.tries -= 1
        return False

    def shorten_list(self) -> None:
        """Shortens the list of options depending on how many tries
        there've been.

        If it is the first try, limit the numbers in the list to those
        within a range of 10 to the lucky nr. Otherwise drop a number.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        if self.tries == 1:  # First try
            self.lucky_list = [
                number for number in self.lucky_list
                if abs(self.lucky_nr - number) < 10]
        elif len(self.lucky_list) == 1:
            pass
        else:
            while True:
                ran = random.choice(self.lucky_list)
                if ran != self.lucky_nr:
                    self.lucky_list.remove(ran)
                    break

    def show_stats(self) -> None:
        """Prints the data from the game save file.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        print(self.save_file.sort_index(ascending=False))

    def save_to_csv(self):
        """Saves the stats from the game to CSV

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        new_row = {
            'name': [self.gamer.name],
            'birthday': [self.gamer.birthdate],
            'age': [self.gamer.age],
            'lucky_number': [self.lucky_nr],
            'total_tries': [int(self.tries)]
        }
        self.save_file = pd.concat(
            [self.save_file, pd.DataFrame(new_row)],
            ignore_index=True,
            axis=0)
        self.save_file.to_csv(self.path, index=False)
