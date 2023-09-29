
import re
import datetime


class MyGamer():
    """
    MyGamer is a class for handling player data, including name, birthdate, and age.

    This class provides methods for validating and processing player information.

    Attributes
    ----------
    name : str
        The player's name.
    birthdate : str or int
        The player's birthdate in 'YYYYMMDD' format.
    age :int
        The player's age calculated based on the birthdate.

    Methods
    -------
    val_name(name):
        Validates and formats the player's name.
    val_birth_day(birth_day):
        Validates the player's birthdate format.
    calc_age(birth_day):
        Calculates the player's age based on the birthdate.

    Example usage:
    gamer = MyGamer('Tyra Forsgren', 20030717)

    Notes:
    The birthdate should be provided in 'YYYYMMDD' format.
    The name should be provided with two words. first/last name.

    """

    def __init__(self, name: str, birthdate) -> None:
        """Initialize a MyGamer instance with the provided name and birthdate.

        Parameters
        ----------
        name : str:
            The player's name.
        birthdate : str or int
            The player's birthdate in 'YYYYMMDD' format.

        """
        self.name = self.val_name(name)
        self.birthdate = self.val_birth_day(birthdate)
        self.age = self.calc_age(self.birthdate)

    def val_name(self, name: str) -> str:
        """Validates and formats the player's name.

        Parameters
        ----------
        name : str
            The player's name.

        Returns
        -------
        str
            The formatted player's name.

        Raises
        ------
        ValueError
            If the name format is invalid.

        """
        name = str(name).strip()
        if not name.replace(' ', '').isalpha() or \
                name.count(' ') > 1 or ' ' not in name:
            raise ValueError("Invalid name format.")
        return name.title()

    def val_birth_day(self, birth_day) -> str:
        """Validates the player's birthdate format.

        Parameters
        ----------
        birth_day : str
            The player's birthdate in 'YYYYMMDD' format.

        Returns
        -------
        str
            The validated birthdate.

        Raises
        ------
        ValueError
            If the birthdate format is invalid.

        """
        date_pattern = r"^\d{8}$"
        birth_day = str(birth_day)
        # Check if the input string matches the pattern
        if not re.match(date_pattern, birth_day):
            raise ValueError(f"Invalid date format: {birth_day}")
        return birth_day

    def calc_age(self, birth_day: str) -> int:
        """Calculates the player's age based on the birthdate.

        Parameters
        ----------
        birth_day : str
            The player's birthdate in 'YYYYMMDD' format.

        Returns
        -------
        int
            The player's age.

        Raises
        ------
        ValueError
            If the player is too young to play (under 18 years old).

        """
        now = datetime.date.today()
        birth = datetime.datetime.strptime(birth_day, '%Y%m%d').date()
        age = now.year - birth.year

        if age >= 18:
            return age
        raise ValueError("You are too young to play.")
