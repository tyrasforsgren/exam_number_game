'''Class defines number game in OOP style'''

# pylint: disable=import-error
# autopep8 --in-place --aggressive --aggressive number_game.py

import random
import pandas as pd
from gamer_module import MyGamer

class NumberGame():
    '''Number game class'''

    def __init__(self, the_gamer: MyGamer):
        self.gamer = the_gamer
        self.lucky_nr = self.generate_lucky_nr()
        self.lucky_list = self.generate_lucky_list()
        self.tries = 0
        self.path = 'game_save.csv'
        self.save_file = pd.read_csv(self.path)

    def game_loop(self, begin):
        '''Starts the main menu and checks for player input'''
        if begin:
            self.start_menu()
        win_flag = False
        while win_flag is not True:
            win_flag = self.check_guess(self.take_guess())
        self.win_menu()

    def generate_lucky_list(self):
        '''Generates a lucky list 0-100 with a lycky nr in it. Sorts it as weluck_list'''
        luck_list = []
        while len(luck_list) < 9:
            ran = random.randint(0, 100)
            if ran not in luck_list and ran != self.lucky_nr:
                luck_list.append(ran)

        luck_list.append(self.lucky_nr)
        luck_list.sort()
        return luck_list

    def generate_lucky_nr(self):
        '''Generates a lucky nr to put in list, and choose to win game'''
        return random.randint(0, 100)

    def take_guess(self):
        '''Get the guess choic3e from the player'''
        self.tries += 1
        player_input = int(input(
            f'Lucky number list: {self.lucky_list} \n'
            f'Your guess: ', end=''))
        return player_input

    def check_guess(self, guess):
        '''Checks i the guess is true and if it is in the list'''
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

    def shorten_list(self):
        '''Shorten the list.
        If it is the first try, limit the nrs in the list to those
        within a 10 radius of the lucky nr.
        Otherwise drop the incorrect guessed nr from the list'''
        if self.tries == 1:
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

    def start_menu(self):
        '''Prints the satart menu and checks for inputs.
        COntinues to relative methods absed on choice'''
        prompt = \
            '\nPLAY [P]\n'\
            'SEE STATS [S]\n'\
            'QUIT [Q]\n\n'

        choice = input(prompt)
        while True:

            if choice.lower() == 'q':
                q_choice = input('ARE YOU SURE [Y] ', end='')
                if q_choice.lower() == 'y':
                    exit()

            elif choice.lower() == 's':
                self.show_stats()

            elif choice.lower() == 'p':
                self.game_loop(begin=False)

            choice = input(prompt)

    def win_menu(self):
        '''The menu if the game is won.
        Checks if the player wants to continue or not
        saves data'''
        print('Gongrats, game is over!\n'
              f'And you got the lucky number on try#{self.tries}')
        self.save_to_csv()
        print('Your results have been saved.')
        self.game_loop(begin=False)

    def show_stats(self):
        '''Shows the csv with stats from previous games'''
        print(self.save_file.sort_index(ascending=False))

    def save_to_csv(self):
        '''Saves the stats from the game'''
        new_row = {
            'name': self.gamer.name,
            'birthday': self.gamer.birthdate,
            'age': self.gamer.age,
            'lucky_number': self.lucky_nr,
            'total_tries': self.tries
        }
        self.save_file = self.save_file.append(new_row, ignore_index=True)
        self.save_file.to_csv(self.path, index=False)
