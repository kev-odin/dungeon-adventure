import random
from abc import abstractmethod


class DungeonCharacter:
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

    @property
    def name(self):
        """Getter for name property

        :return: name of adventurer
        :rtype: str
        """
        return self.__char_dict["name"]

    @name.setter
    def name(self, value):
        """Setter for the name property

        :param value: name provided by user
        :type value: str
        """
        if isinstance(value, str):
            self.__char_dict["name"] = value

    @property
    def max_hitpoints(self):
        """Getter for hitpoints property

        :return: health remaining of adventurer
        :rtype: int
        """
        return self.__char_dict["max_hp"]

    @max_hitpoints.setter
    def max_hitpoints(self, value):
        """Setter for the hitpoints property

        :param value: damage incurred from pits
        :type value: int
        """
        if isinstance(value, int):
            self.__char_dict["max_hp"] = value

    @property
    def current_hitpoints(self):
        """Getter for the current hitpoints property, to be used by main

        :return: value of the current hitpoints for adventurer
        :rtype: int
        """
        return self.__char_dict["current_hp"]

    @current_hitpoints.setter
    def current_hitpoints(self, value):
        """
        Sets hitpoints to the new value.  Do the math from current HP to setter to get value for setting.
        :param value: int of new value for current_hp
        """
        if isinstance(value, int):
            if value >= 0:
                self.__char_dict["current_hp"] = value
            else:
                raise ValueError("Cannot set current hitpoints to a negative value.")

    @property
    def attack_speed(self):
        return self.__char_dict["attack_speed"]

    @property
    def hit_chance(self):
        return self.__char_dict["hit_chance"]

    def attack(self):
        """
        Checks if character hits.  If they do, returns the damage dealt.
        :return:
        """
        if random.randint(0, 100) <= (self.hit_chance * 100):
            return random.randint(self.__char_dict["min_dmg"], self.__char_dict["max_dmg"])
        else:
            return 0
