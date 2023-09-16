import unittest
from unittest.mock import patch
from number_game import NumberGame
from gamer_module import MyGamer

class TestNumberGame(unittest.TestCase):

    def setUp(self):
        self.mock_input = patch('builtins.input', side_effect=[])
        self.mock_input.start()
        self.gamer = MyGamer("John Doe", "19950101")
        self.game = NumberGame(self.gamer)

    def tearDown(self):
        self.mock_input.stop()

    def simulate_input(self, input_values):
        self.mock_input.side_effect = input_values

    def test_start_menu_quit(self):
        # Test the start_menu method with quitting the game
        self.simulate_input(['q', 'y'])
        with self.assertLogs(level='INFO') as log:
            self.game.start_menu()
            self.assertIn('INFO:root:Exiting the game', log.output)

    def test_start_menu_show_stats(self):
        # Test the start_menu method with showing stats
        self.simulate_input(['s'])
        with self.assertLogs(level='INFO') as log:
            self.game.start_menu()
            self.assertIn('INFO:root:Showing game stats', log.output)

    def test_show_stats(self):
        # Test the show_stats method
        with self.assertLogs(level='INFO') as log:
            self.game.show_stats()
            self.assertIn('INFO:root:Showing game stats', log.output)

    @patch('pandas.DataFrame.to_csv')
    def test_save_to_csv(self, mock_to_csv):
        # Test the save_to_csv method
        self.game.save_to_csv()
        mock_to_csv.assert_called_once_with(self.game.path, index=False)

if __name__ == '__main__':
    unittest.main()
