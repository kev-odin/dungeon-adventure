# Kevin's Time Tracker: 2 hours

from potion import Potion
from random import randint

class HealthPotion(Potion):
    """Health potion that an adventurer can use to increase current hitpoints
    """
    def __init__(self, random = True):
        """Basic health potion

        :param extra_effects: provides random integer values, defaults to True (used for testing)
        :type extra_effects: bool, optional
        """
        self.__name = "Health Potion"
        self.__heal_amount = 0

        if random:
            self._potion_effect()

    def __str__(self):
        plural = "s" if self.heal_amount != 1 else ""
        return f"Item: {self.name}\nEffect: Restores {self.heal_amount} hitpoint{plural}."

    def __repr__(self):
        return f"{self.name}, {self.heal_amount}"

    def action(self):
        """
        User decides to use a potion in the inventory, to be used by main
        :return: value of the amount healed by potion
        :rtype: int
        """
        return self.heal_amount

    def _potion_effect(self):
        """Private helper method that is used to determine the strength
        of a health potion. Uses a random integer between 5 and 15.
        """
        min_heal = 1
        max_heal = 21
        potion_strength = randint(min_heal, max_heal)
        self.heal_amount += potion_strength

        if potion_strength <= 7:
            self.name = "Lesser Health Potion"
        elif potion_strength >= 15:
            self.name = "Greater Health Potion"

    @property
    def name(self):
        """Getter for the name of the Health Potion

        :return: Name of the health potion
        :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for the heal amount of the Health Potion

        :param value: value to replace the name
        :type value: str
        :raises TypeError: When a string is not provided to the setter
        """
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("Value passed into method was not a string.")

    @property
    def heal_amount(self):
        """Getter for the heal amount of the Health Potion

        :return: value of the amount that can be added to adventurer hitpoints
        :rtype: int
        """
        return self.__heal_amount

    @heal_amount.setter
    def heal_amount(self, value):
        """Setter for the heal amount of the Health Potion

        :param value: value to be added to the potion amount
        :type value: int
        :raises TypeError: When an integer is not provided to the setter
        """
        if isinstance(value, int):
            self.__heal_amount += value
        else:
            raise TypeError("Value passed into method was not an integer value.")
