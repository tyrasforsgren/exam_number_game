import unittest
from gamer_module import MyGamer
# autopep8 --in-place --aggressive --aggressive test_gamer_module.py


class TestMyGamer(unittest.TestCase):
    'Class to test test_gamer_module.py'

    def test_valid_name(self):
        '''Test valid names'''
        valid_names = ["John Peterson", "ben johnson"]
        for name in valid_names:
            gamer = MyGamer(name, "20001231")
            self.assertEqual(gamer.name, name.title())

    def test_invalid_name(self):
        '''Test invalid names:
        - No input
        - Only numbers
        - Numbers and letters
        - Too many names'''
        invalid_names = ["", "12345", "Steve 123", "Merry Lee Smith"]
        for name in invalid_names:
            with self.assertRaises(ValueError):
                MyGamer(name, "20001231")

    def test_valid_birthdate(self):
        '''Test valid birthdates'''
        valid_birthdates = ['20030519', '19991212']
        for birth_dates in valid_birthdates:
            gamer = MyGamer("Simon Bell", birth_dates)
            self.assertEqual(gamer.birthdate, birth_dates)

    def test_invalid_birthdate(self):
        '''TEst invalid birthdates:
        - too many nrs
        - letters
        - too young
        - Noneexistant dates'''
        invalid_birthdates = [9 * "0", "1h15", "20230419", '10005050']
        # Tests for too long input, numbers, too young, nonexistent dates.
        for birth_dates in invalid_birthdates:
            with self.assertRaises(ValueError):
                MyGamer("Johnathan Gilbert ", birth_dates)

    # Not neccesry cause ages arent calculated until after the birth_datess are
    # validated


if __name__ == '__main__':
    unittest.main()
