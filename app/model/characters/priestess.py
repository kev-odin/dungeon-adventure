from app.model.characters.adventurer import Adventurer
from app.model.characters.healable import HealAble


class Priestess(Adventurer, HealAble):
    def __init__(self, char_dict):
        super().__init__(char_dict)
        self.__char_dict["max_heal"] = self.__char_dict["max_hp"]
        self.__char_dict["min_heal"] = self.__char_dict["max_hp"] * 0.25

    def use_special(self):
        """
        Priestess heals self.
        :return: int heal_amount
        """
        heal_amount = self.__heal(self.__char_dict)
        self.current_hitpoints += heal_amount
        return heal_amount
