from app.model.characters.adventurer import Adventurer
from random import randint


class Thief(Adventurer):
    def __init__(self, adv_dict):
        super().__init__(adv_dict)

    def use_special(self):
        """
        Uses sneak attack.  40% chance of doing two attacks.  20% chance of no attacks.  40% chance of normal attack.
        :return: tuple of ints if sneak attack succeeds.  Returns 0 if fails.  Else returns single int if normal attack.
        """
        random = randint(0, 100)
        if random <= 40:
            first = self.attack()
            second = self.attack()
            return first, second
        elif 40 > random <= 60:
            return 0
        else:
            return self.attack()
