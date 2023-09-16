import re
import datetime


class MyGamer():

    def __init__(self, name, bithdate):
        self.name = self.val_name(name)
        self.birthdate = self.val_bd(bithdate)
        self.age = self.calc_age(self.birthdate)

    def val_name(self, name):
        name = str(name).strip()
        if not name.replace(' ', '').isalpha() or name.count(
                ' ') > 1 or ' ' not in name:
            raise ValueError("Invalid name format.\n\n")
        return name.title()

    def val_bd(self, bd):
        date_pattern = r"^\d{8}$"
        bd = str(bd)
        # Check if the input string matches the pattern
        if not re.match(date_pattern, bd):
            raise ValueError(f"Invalid date format: {bd}")
        return bd

    def calc_age(self, bd):
        now = datetime.date.today()
        bday = datetime.datetime.strptime(bd, '%Y%m%d').date()
        age = now.year - bday.year

        if age >= 18:
            return age
        else:
            raise ValueError("You are too young to play")
