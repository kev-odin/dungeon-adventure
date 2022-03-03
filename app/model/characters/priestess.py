from app.model.characters.adventurer import Adventurer
from app.model.characters.healable import HealAble
from random import randint


class Priestess(Adventurer, HealAble):  # Tried doing multiple inheritance, lead to many problems
    def __init__(self, char_dict):
        super().__init__(char_dict)

    def use_special(self):
        """
        Priestess heals self.
        :return: int heal_amount
        """
        heal_amount = self.heal(self.char_dict)
        self.current_hitpoints += heal_amount
        return heal_amount
