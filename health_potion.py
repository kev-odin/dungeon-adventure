# Kevin's Time Tracker: 1 hours

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
        return f'Item: {self.name}\nEffect: Adventurer has been healed for {self.heal_amount} hitpoints'

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
        potion_strength = randint(5, 15)
        self.heal_amount += potion_strength

    @property
    def name(self):
        """Getter for the name of the Health Potion

        :return: Name of the health potion
        :rtype: str
        """
        return self.__name

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
