from abc import ABC
import random


class HealAble(ABC):
    def __init__(self, char_dict):
        self.__heal_data = {"min_heal": char_dict["min_heal"], "max_heal": char_dict["max_heal"],
                            "current_hp": char_dict["current_hp"], "max_hp": char_dict["max_hp"]}

    def __update_heal_data(self, char_dict):
        """
        Updates heal data from a dictionary with a current_hp value.
        :param char_dict: dict containing current_hp, min_heal, max_heal, max_hp
        :return:
        """
        self.__heal_data["current_hp"] = char_dict["current_hp"]

    def heal(self, char_dict):
        """
        Calculates heal amount and returns amount healed, minus going over the max HP.
        :return:
        """
        self.__update_heal_data(char_dict)
        heals = self.__heal_data
        if heals["current_hp"] > 0:
            heal_amount = random.randint(heals["min_heal"], heals["max_heal"])
            heals["current_hp"] += heal_amount
            if heals["current_hp"] > heals["max_hp"]:
                reduction = heals["current_hp"] - heals["max_hp"]
                heal_amount -= reduction
            return heal_amount
        return None, 0
