# Kevin's Time Tracker: 8.5 hours
import random

class Adventurer:
    """Adventurer that traverses through the maze. Picks up potions, falls into pits, and
    must complete the maze with all OOP pillars (APIE) collected to win.
    """
    # TODO:
    # 1) Determine how to manage potion inventory <- no need for a list, create as needed by user
    # 2) How does adventurer check the state of the room? <- Given by dungeon methods, recieved as tuples
    # 3) Auto pick up potion in a room <- Method provided by dungeon
    # 4) Working observer pattern with adventurer and potion factory <- At this point, no needed
    # 5) Random hitpoint generator <-
    # 6) Write tests
    # 7) Using health potions, pit damage <-

    def __init__(self, name = None, challenge = "easy"):
        """Adventurer object that maintains the inventory collection of potions,
        pillars collected, and current hitpoints.

        :param name: name of the adventurer provided by user, defaults to None
        :type name: str
        :param challenge: challenge provided by user, defaults to 'easy'
        :type challenge: str
        """
        self.__name = name
        self.__dev_powers = False
        self.__max_hitpoints = 75           # At this stage, baseline health
        self.__current_hitpoints = None
        self.__health_pots = 0
        self.__vision_pots = 0
        self.__pillars_collected = {
            "A" : False,
            "P" : False,
            "I" : False,
            "E" : False
        }

        self._create_adventurer(name, challenge)

    def is_alive(self):
        """Helper method to determine that the adventurer is alive during the dungeon adventure
        :return: True if hitpoints are greater than 0
        """
        return self.current_hitpoints > 0

    def has_all_pillars(self):
        """ Helper method to determine when all pillars have been collected by the adventurer
        :return: True if all pillars are collected
        """
        return all(pillar is True for pillar in self.__pillars_collected.values())

    def add_potions(self, potions):
        """ Helper method to add potions found in a room to the adventurer's
        inventory. To be used by the main method.
        :param: tuple (health_potions : int, vision_potions : int)
        :raise: TypeError when tuple length is not 2
        """
        if len(potions) == 2:
            if all(isinstance(val, int) for val in potions):
                room_health, room_vision = potions
                self.health_pots += room_health
                self.vision_pots += room_vision
            else:
                raise TypeError("Potion values are not integers.")
        else:
            raise ValueError("Length of tuple is not 2.")

    def add_pillar(self, pillar):
        """ Helper method to add pillars found in a room to the adventurer's
        inventory. To be used by the main method.
        :param: str - pillar values: "A", "P", "I", "E"
        """
        if isinstance(pillar, str):
            for val in self.pillars_collected:
                if val == pillar:
                    self.pillars_collected[pillar] = True
        else:
            print("You should not see this message.")

    def damage_adventurer(self, pit_damage):
        """ Helper method to damage adventurer based on the pit damage
        provided by the room. To be used by the main method.
        :param: int - damage values that will decrement current health
        """
        if isinstance(pit_damage, int):
            print(f"{self.name} fell into a pit and took {pit_damage} points of damage.")

            new_health = self.current_hitpoints - pit_damage
            if new_health <= 0:
                self.current_hitpoints = 0
            else:
                self.current_hitpoints = new_health

    def heal_adventurer(self, heal_amount):
        """ Helper method to heal adventurer based on the health potion.
        To be used by the main method.
        :param: int - heal values that will increment current health
        """
        if isinstance(heal_amount, int):
            new_health = self.current_hitpoints + heal_amount
            if new_health > self.max_hitpoints:
                self.current_hitpoints = self.max_hitpoints
            else:
                self.current_hitpoints = new_health

    def use_health_potion(self):
        """ Helper method to decrement health potions in the adventurer's
        inventory. To be used by the main method.
        """
        if self.health_pots > 0:
            self.health_pots -= 1
            print(f"{self.name} used a health potion.")
        else:
            print(f"{self.name} does not have a health potion.")

    def use_vision_potion(self):
        """ Helper method to decrement vision potions in the adventurer's
        inventory. To be used by the main method.
        """
        if self.vision_pots > 0:
            self.vision_pots -= 1
            print(f"{self.name} used a vision potion.")
        else:
            print(f"{self.name} does not have a vision potion.")

    def _create_adventurer(self, name, challenge):
        """Helper method for character creation. Difficulty and name are checked,
        based on those values, create an adventurer with modified base values.

        :param: name: str if found in cheat_code dictionary, modification applied to adventurer
        :param: challenge: str sets to following challenge level:
             'easy' 3x, 'medium' 2x, 'hard' 1x, 'inhumane' 0x
        """
        difficulty = {
            'easy' : 3,
            'medium' : 2,
            'hard' : 1,
            'inhumane' : 0
        }

        cheat_codes = {
            'tom' : 'no health lost',
            'kevin' : 'unlimited potions'
        }

        if name in cheat_codes:
            self.dev_powers = True

        if challenge in difficulty:
            hp_mod = difficulty[challenge]
            self.max_hitpoints += hp_mod * random.randint(0, 10)
            self.current_hitpoints = self.max_hitpoints

    def __str__(self):
        player_stats = f'Name: {self.name}\n'
        player_stats += f'HP: {self.current_hitpoints} / {self.max_hitpoints}\n'
        player_stats += f'Health potions: {self.health_pots}\n'
        player_stats += f'Vision potions: {self.vision_pots}\n'
        player_stats += f'Pillars collected: {self.pillars_collected}\n'
        return player_stats

    @property
    def name(self):
        """Getter for name property

        :return: name of adventurer
        :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for the name property

        :param value: name provided by user
        :type value: str
        """
        if isinstance(value, str):
            self.__name = value

    @property
    def dev_powers(self):
        """Getter for the dev_powers property

        :return: status if cheat codes are enabled
        :rtype: bool
        """
        return self.__dev_powers

    @dev_powers.setter
    def dev_powers(self, value):
        """Setter for the dev_powers property

        :param value: boolean if cheat codes are enabled
        """
        if isinstance(value, bool):
            self.__dev_powers = value

    @property
    def max_hitpoints(self):
        """Getter for hitpoints property

        :return: health remaining of adventurer
        :rtype: int
        """
        return self.__max_hitpoints

    @max_hitpoints.setter
    def max_hitpoints(self, value):
        """Setter for the hitpoints property

        :param value: damage incurred from pits
        :type value: int
        """
        if isinstance(value, int):
            self.__max_hitpoints = value

    @property
    def current_hitpoints(self):
        """Getter for the current hitpoints property, to be used by main

        :return: value of the current hitpoints for adventurer
        :rtype: int
        """
        return self.__current_hitpoints

    @current_hitpoints.setter
    def current_hitpoints(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__current_hitpoints = value
            else:
                raise ValueError("Cannot set current hitpoints to a negative value.")

    @property
    def health_pots(self):
        """Getter for health potion property

        :return: number of health potions for adventurer
        :rtype: int
        """
        return self.__health_pots

    @health_pots.setter
    def health_pots(self, value):
        """Setter for the health potion property

        :param value: number of potions found in the room
        :type value: int
        :raises ValueError for values that are negative
        """
        if isinstance(value, int):
            if value >= 0:
                self.__health_pots = value
            else:
                raise ValueError('Cannot set health potions to a negative value.')

    @property
    def vision_pots(self):
        """Getter for vision pots property

        :return: number of vision potions for adventurer
        :rtype: int
        """
        return self.__vision_pots

    @vision_pots.setter
    def vision_pots(self, value):
        """Setter for the health pots property

        :param value: number of potions found in the room, value can not be negative
        :type value: int
        :raises ValueError for values that are negative
        """
        if isinstance(value, int):
            if value >= 0:
                self.__vision_pots = value
            else:
                raise ValueError('Cannot set vision potions to a negative value.')

    @property
    def pillars_collected(self):
        """Returns the pillars that have been collected during the game session

        :return: str of dictionary values {pillar : bool}
        """
        return self.__pillars_collected


    # Not sure why this setter does not work with the dictionary. Will need to re-examine.
    # @pillars_collected.setter
    # def pillars_collected(self, value):
    #     """Setter for the pillars collected property

    #     :param value: value of the pillar found in room
    #     :type value: string
    #     :raises KeyError: invalid key that is not found in the
    #     """
    #     if isinstance(value, str):
    #         if value in self.pillars_collected.keys():
    #             self.pillars_collected[value] = True
    #         else:
    #             raise KeyError('Invalid key passed, valid pillar keys are: "A", "P", "I", "E"')
