# Kevin's Time Tracker: 1 hours

from potion import Potion
from random import randint

class VisionPotion(Potion):
    """Vision potion that an adventurer can use to reveal surrounding rooms
    """
    def __init__(self, extra_effects = False):
        self.__name = 'Vision Potion'
        self.__rooms_revealed = 8       #Default value, for surrounding rooms revealed
        if extra_effects:
            self._potion_effect()

    def __str__(self):
        return f'Item: {self.name}\nEffect: {self.rooms_revealed} adjacent rooms are revealed.'

    def action(self):
        return self.rooms_revealed

    def _potion_effect(self):
        self.rooms_revealed = 0
        potion_strength = randint(1, 8)
        self.rooms_revealed += potion_strength

    @property
    def name(self):
        return self.__name

    @property
    def rooms_revealed(self):
        return self.__rooms_revealed

    @rooms_revealed.setter
    def rooms_revealed(self, value):
        if isinstance(value, int):
            self.__rooms_revealed = value
        else:
            raise ValueError("Value passed into method was not an integer value.")
