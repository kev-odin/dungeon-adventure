from abc import ABC
import random


class HealAble(ABC):
    @staticmethod
    def heal(heals):
        """
        Calculates heal amount and returns amount healed, minus going over the max HP.
        :return: int representing amount healed
        """
        if heals["current_hp"] > 0:
            heal_amount = random.randint(heals["min_heal"], heals["max_heal"])
            heals["current_hp"] += heal_amount
            if heals["current_hp"] > heals["max_hp"]:
                reduction = heals["current_hp"] - heals["max_hp"]
                heal_amount -= reduction
            return heal_amount
        return 0
