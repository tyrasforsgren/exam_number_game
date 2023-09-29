"""
test_gamer_module

This module contains unit tests for the 'MyGamer' class from the 'gamer_module' module.
It tests various scenarios for validating player names and birthdates.

Classes
-------
TestMyGamer(unittest.TestCase)
    Class to test the 'MyGamer' class.

Methods
-------
test_valid_name()
    Test valid names.
test_invalid_name()
    Test invalid names, including no input, only numbers, numbers and letters,
    and too many names.
test_valid_birthdate()
    Test valid birthdates.
test_invalid_birthdate()
    Test invalid birthdates, including too many digits, letters, too young,
    and nonexistent dates.
test_calc_age()
    Test the result of certain ages. Too young and old enough. 

Example usage
-------------
Run this script to test every method.

"""

import unittest
from unittest.mock import patch
from gamer_module import MyGamer

class TestMyGamer(unittest.TestCase):
    """Class to test the 'MyGamer' class from the 'gamer_module' module."""

    def test_valid_name(self) -> None:
        """Test the passing of valid names."""
        # Examples of valid names
        valid_names = ["John Peterson", "ben johnson"]
        for name in valid_names:
            gamer = MyGamer(name, "20001231")
            # Assert that both names were accepted and properly capitalized.
            self.assertEqual(gamer.name, name.title())

    def test_invalid_name(self) -> None:
        """Test the passing of invalid names:
        - No input
        - Only numbers
        - Numbers and letters
        - Too many names

        """
        invalid_names = ["", "12345", "Steve 123", "Merry Lee Smith"]
        for name in invalid_names:
            # Assert that every invalid name raises a ValueError.
            with self.assertRaises(ValueError):
                MyGamer(name, "20001231")

    def test_valid_birthdate(self) -> None:
        """Test the passing of valid birthdates.

        """
        valid_birthdates = ['20030519', '19991212']
        for birth_date in valid_birthdates:
            gamer = MyGamer("Simon Bell", birth_date)
            # Assert that valid birthdates are accepted.
            self.assertEqual(gamer.birthdate, birth_date)

    def test_invalid_birthdate(self) -> None:
        """Test the passing of invalid birthdates:
        - Too many digits
        - Letters
        - Too young
        - Nonexistent dates

        """
        invalid_birthdates = [9 * "0", "1h15", "20230419", '10005050']
        # Tests for too long input, numbers, too young, nonexistent dates.
        for birth_date in invalid_birthdates:
            # Assert that every invalid birthdate raises a ValueError.
            with self.assertRaises(ValueError):
                MyGamer("Johnathan Gilbert", birth_date)

    def test_calc_age_old_enough(self) -> None:
        """Test the result of certain ages.
        - Right age
        - Too young

        """
        # Valid
        birthdate_18 = '20050101'
        gamer_18 = MyGamer("Alice Moose", birthdate_18)
        self.assertEqual(gamer_18.calc_age(birthdate_18), 18)

        # Invalid
        birthdate_young = '20100101'
        with self.assertRaises(ValueError):
            young_player = MyGamer("Charlie Willie", birthdate_young)
            young_player.calc_age(birthdate_young)

    def calc_age_correct_age(self) -> None:
        """Tests that age has been correctly calculated."""
        mock_gamer = MyGamer('','')
        with patch ('datetime.date.today') as mock_today, \
            patch ('datetime.datetime.strptime') as mock_birth:
            mock_today.return_value.year = 2023
            mock_birth.return_value.date.return_value.year = 2003 
            age = mock_gamer.calc_age('')
            expected_age = mock_today.return_value.year - mock_birth.return_value.date.return_value.year

        self.assertEqual(age, expected_age)


if __name__ == '__main__':
    unittest.main()
