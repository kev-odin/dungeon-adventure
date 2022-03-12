from abc import ABC
import random


class DungeonCharacter(ABC):
    def __init__(self, char_dict: dict):
        self.__char_dict = char_dict

    def take_damage(self, damage):
        """ Method to have characters take damage.

        :param: int - damage values that will decrement current health
        :return: pit_damage inflicted on the adventurer
        :rtype: int
        """
        if isinstance(damage, int):
            new_health = self.current_hitpoints - damage
            if new_health <= 0:
                self.current_hitpoints = 0
            else:
                self.current_hitpoints = new_health
            return damage
        else:
            raise TypeError(f"{damage} is not type int.")

    @property
    def name(self):
        """Getter for name property

        :return: name of adventurer
        :rtype: str
        """
        return self.char_dict["name"]

    @name.setter
    def name(self, value):
        """Setter for the name property

        :param value: name provided by user
        :type value: str
        """
        if isinstance(value, str):
            self.char_dict["name"] = value

    @property
    def max_hitpoints(self):
        """Getter for hitpoints property

        :return: health remaining of adventurer
        :rtype: int
        """
        return self.char_dict["max_hp"]

    @max_hitpoints.setter
    def max_hitpoints(self, value):
        """Setter for the hitpoints property

        :param value: damage incurred from pits
        :type value: int
        """
        if isinstance(value, int):
            self.char_dict["max_hp"] = value

    @property
    def current_hitpoints(self):
        """Getter for the current hitpoints property, to be used by main

        :return: value of the current hitpoints for adventurer
        :rtype: int
        """
        return self.char_dict["current_hp"]

    @current_hitpoints.setter
    def current_hitpoints(self, value):
        """
        Sets hitpoints to the new value.  Do the math from current HP to setter to get value for setting.
        :param value: int of new value for current_hp
        """
        if isinstance(value, int):
            if value >= 0:
                self.char_dict["current_hp"] = value
            else:
                raise ValueError("Cannot set current hitpoints to a negative value.")

    @property
    def attack_speed(self):
        return self.char_dict["attack_speed"]

    @property
    def hit_chance(self):
        return self.char_dict["hit_chance"]

    def attack(self, hit_chance=None, min_dmg=None, max_dmg=None):
        """
        Checks if character hits.  If they do, returns damage between min and max dmg, else returns 0.
        :param hit_chance: float representing percent change of hit succeeding, 1 for will definitely hit.
        :param min_dmg: int representing minimum damage that will be dealt.  Defaults to dictionary value if None.
        :param max_dmg: int representing maximum damage that can be dealt.  Defaults to dictionary value if None.
        :return: int representing damage dealt, 0 for a miss.
        """
        if hit_chance is None:  # Implemented this way for overriding with Warrior skill.
            hit_chance = self.hit_chance
        if min_dmg is None:
            min_dmg = self.char_dict["min_dmg"]
        if max_dmg is None:
            max_dmg = self.char_dict["max_dmg"]

        if random.randint(0, 100) <= (hit_chance * 100):
            return random.randint(min_dmg, max_dmg)
        else:
            return 0

    @property
    def char_dict(self):
        """
        Getter for char_dict.  Returns dictionary representing the character stats.
        :return: dict representing character stats and attributes.
        """
        return self.__char_dict
