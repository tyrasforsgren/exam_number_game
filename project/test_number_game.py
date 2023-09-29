"""
Test NumberGame Class

This module contains unit tests for the NumberGame class in the number_game module.
It includes test cases for various methods and functionalities of the game.

Classes
-------
TestNumberGame
    A test class for NumberGame unit tests.

Example usage
-------------
Run this script to test every method.

Notes:
There are no parameters for any test method because it is a test class
(and 'with'-statements are used instead of decorators when mocking.)
No test method has returns because this is a test class.

Lack of parameters and returns are not explicitly stated in each method
documentation under the assumption that readers understand
this concept and that suggestions of this in method heads are enough.

"""

import unittest
from unittest.mock import patch
from number_game import NumberGame
from gamer_module import MyGamer

class TestNumberGame(unittest.TestCase):
    """
    TestNumberGame class for unit testing the NumberGame class.

    Methods
    -------
    setUp()
        Set up the testing environment by creating a MyGamer instance and a
        NumberGame instance for testing.
    tearDown()
        Reset the testing environment to ensure independence between every test.
    test_start_menu_quit()
        Test the start_menu method with quitting the game.
    test_start_menu_show_stats()
        Test the start_menu method with showing statistics.
    test_start_menu_play()
        Test the start_menu method with starting a new game.
    test_win_menu()
        Test the win_menu method.
    test_take_guess()
        Test the take_guess method with valid and invalid inputs.
    test_generate_lucky_list()
        Test the generate_lucky_list method.
    test_generate_lucky_nr()
        Test the generate_lucky_nr method.
    test_check_guess_true()
        Test the check_guess method with a correct guess.
    test_check_guess_false()
        Test the check_guess method with an incorrect guess.
    test_shorten_list_first_try()
        Test the shorten_list method on the first try.
    test_shorten_list_drop()
        Test the shorten_list method when dropping a number.
    test_shorten_list_equal()
        Test the shorten_list method when the list has only one element.
    test_show_stats()
        Test the show_stats method.
    test_save_to_csv()
        Test the save_to_csv method.

    """
    def setUp(self):
        """
        Set up the testing environment by creating a MyGamer instance and a
        NumberGame instance for testing.
        """
        self.gamer = MyGamer("John Doe", "19950101")
        self.game = NumberGame(self.gamer)

    def tearDown(self):
        """
        Reset the testing environment to ensure independence between every
        test. This method is automatically called after each test case.
        """
        test_method_name = self._testMethodName
        print(
            f'\n\nTEST {test_method_name.replace("test_","").upper()} ' \
            'CLEARED\n\n'.center(40))
        self.game = None
        self.gamer = None

    def test_start_menu_quit(self):
        """
        Test the start_menu method with quitting the game.

        This test simulates user input 'q' followed by 'y' to quit the game.
        It asserts that the sys.exit function is called exactly once.
        """
        with patch('builtins.input', side_effect=['q', 'y']), \
            patch('sys.exit') as mock_exit: 
            self.game.start_menu()
            mock_exit.assert_called_once()

    def test_start_menu_show_stats(self):
        """
        Test the start_menu method with showing statistics.

        This test simulates user input 's' to see game statistics. It asserts
        that the NumberGame.show_stats method is called exactly once.
        """
        with patch('builtins.input', return_value='s'), \
            patch('number_game.NumberGame.show_stats') as mock_stats:
            self.game.start_menu()
            mock_stats.assert_called_once()

    def test_start_menu_play(self):
        """
        Test the start_menu method with starting a new game.

        This test simulates user input 'p' to start a new game. It asserts
        that the NumberGame.game_loop method is called exactly once.
        """
        with patch('builtins.input', return_value='p'), \
            patch('number_game.NumberGame.game_loop') as mock_play:
            self.game.start_menu()
            mock_play.assert_called_once()

    def test_win_menu(self): 
        """
        Test the win_menu method.

        This test simulates the win_menu method. It asserts that the
        NumberGame.save_to_csv method is called exactly once and that the
        NumberGame.game_loop method is called with begin=True.
        """
        with patch('number_game.NumberGame.save_to_csv') as mock_save, \
            patch('number_game.NumberGame.game_loop') as mock_loop:
            self.game.win_menu()
            mock_save.assert_called_once()
            mock_loop.assert_called_once_with(begin=True)

    def test_take_guess(self):
        """  
        Test the take_guess method with valid and invalid inputs.

        This test simulates user input 'Not numeric' followed by '7' as guesses.
        It asserts that the return value from take_guess is an integer.
        """
        with patch('builtins.input', side_effect=['Not numeric', '7']):
            return_value = self.game.take_guess()
            self.assertIsInstance(return_value, int)

    def test_generate_lucky_list(self):
        """
        Test the generate_lucky_list method.

        This test sets the lucky number to 10 and generates a lucky list. It
        asserts that the lucky number is in the generated list, the length of
        the list is 10, and the lucky number appears only once in the list.
        """
        self.game.lucky_nr = 10
        mock_list = self.game.generate_lucky_list()
        self.assertIn(self.game.lucky_nr, mock_list)
        self.assertEqual(len(mock_list), 10)
        self.assertEqual(mock_list.count(self.game.lucky_nr), 1)

    def test_generate_lucky_nr(self):
        """
        Test the generate_lucky_nr method.

        This test simulates random.randint to return 10 as the lucky number.
        It asserts that the returned value is 10.
        """
        with patch('random.randint', return_value=10):
            mock_luck = self.game.generate_lucky_nr()
            self.assertEqual(mock_luck, 10)

    def test_check_guess_true(self):
        """
        Test the check_guess method with a correct guess.

        This test sets the lucky number to 10 and passes 10 as the guess. It
        asserts that the check_guess method returns True.
        """
        self.game.lucky_nr = 10
        value = self.game.check_guess(10)
        self.assertTrue(value)

    def test_check_guess_false(self):
        """
        Test the check_guess method with an incorrect guess.

        This test sets the lucky number to 10 and passes 1 as the guess. It
        asserts that the check_guess method returns False.
        """
        self.game.lucky_nr = 10
        value = self.game.check_guess(1)
        self.assertFalse(value)

    def test_shorten_list_first_try(self):
        """
        Test the shorten_list method on the first try.

        This test sets the number of tries to 1 and the lucky number to 15.
        It shortens the lucky list and asserts that it matches the expected list.
        """
        self.game.tries = 1
        self.game.lucky_nr = 15
        self.game.lucky_list = [1, 5, 10, self.game.lucky_nr, 20, 25, 30]
        self.game.shorten_list()
        expected_list = [10, 15, 20]
        self.assertEqual(expected_list, self.game.lucky_list)

    def test_shorten_list_drop(self):
        """
        Test the shorten_list method when dropping a number.

        This test sets the lucky list to [1, 2, 3, 4] and shortens it. It
        asserts that the length of the list is reduced by 1.
        """
        self.game.lucky_list = [1, 2, 3, 4]  # len = 4
        self.game.shorten_list()
        self.assertEqual(len(self.game.lucky_list), 3)

    def test_shorten_list_equal(self):
        """
        Test the shorten_list method when the list has only one element.

        This test sets the lucky list to [1] and shortens it. It asserts that
        the length of the list remains 1.
        """
        self.game.lucky_list = [1]  # len = 1
        self.game.shorten_list()
        self.assertEqual(len(self.game.lucky_list), 1)

    def test_show_stats(self):
        """
        Test the show_stats method.

        This test simulates the show_stats method and checks if the print
        function is called.
        """
        with patch('builtins.print') as mock_print:
            self.game.show_stats()
            mock_print.assert_called_once()

    def test_save_to_csv(self):
        """
        Test the save_to_csv method.

        This test simulates the save_to_csv method and checks if the to_csv
        function is called with the correct arguments.
        """
        with patch('pandas.DataFrame.to_csv') as mock_to_csv:
            self.game.save_to_csv()
            mock_to_csv.assert_called_once_with(self.game.path, index=False)
# """
if __name__ == '__main__':
    unittest.main()
