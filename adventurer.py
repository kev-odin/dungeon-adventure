# Kevin"s Time Tracker: 20 hours
from health_potion import HealthPotion
import random
class Adventurer:
    """Adventurer that traverses through the maze. Picks up potions, falls into pits, and
    must complete the maze with all OOP pillars (APIE) collected to win.
    """

    def __init__(self, name = None, challenge = "easy"):
        """Adventurer object that maintains the inventory collection of potions,
        pillars collected, and current hitpoints.

        :param name: name of the adventurer provided by user, defaults to None
        :type name: str
        :param challenge: challenge provided by user, defaults to "easy"
        :type challenge: str
        """
        self.__name = name
        self.__dev_powers = False
        self.__max_hitpoints = None
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
        return all(pillar is True for pillar in self.pillars_collected.values())

    def add_potions(self, room_potions):
        """ Helper method to add potions found in a room to the adventurer's
        inventory. To be used by the main method.

        Abstraction/Polymorphism pillar power increases potions found in each room.

        :param: tuple (health_potions : int, vision_potions : int)
        :raise: TypeError when tuple length is not 2
        :return:
            room_health - health potions added to inventory,
            room_vision - vision potions added to inventory
        :rtype: int
        """
        better_collect = 2

        if len(room_potions) == 2:
            if all(isinstance(val, int) for val in room_potions):
                room_health, room_vision = room_potions

                if self.pillars_collected["A"] and room_health > 0:
                    room_health = room_health * better_collect

                if self.pillars_collected["P"] and room_vision > 0:
                    room_vision = room_vision * better_collect

                self.health_pots += room_health
                self.vision_pots += room_vision

                return room_health, room_vision

            else:
                raise TypeError("Potion values are not integers.")
        else:
            raise ValueError("Length of tuple is not 2.")

    def add_pillar(self, pillar):
        """ Helper method to add pillars found in a room to the adventurer's
        inventory. To be used by the main method.
        :param: str - pillar values: "A", "P", "I", "E"
        """
        if pillar is not None:
            if isinstance(pillar, str):

                if self.pillars_collected[pillar]:
                    return

                for val in self.pillars_collected:
                    if val == pillar:
                        self.pillars_collected[pillar] = True
            else:
                print("You should not see this message.")

    def damage_adventurer(self, pit_damage):
        """ Helper method to damage adventurer based on the pit damage
        provided by the room. To be used by the main method.

        Inheritance pillar power reduces pit damage by half.

        :param: int - damage values that will decrement current health
        :return: pit_damage inflicted on the adventurer
        :rtype: int
        """
        if isinstance(pit_damage, int):

            if self.pillars_collected["I"]:
                pit_damage = pit_damage // 2

            new_health = self.current_hitpoints - pit_damage
            if new_health <= 0:
                self.current_hitpoints = 0
            else:
                self.current_hitpoints = new_health
            
            return pit_damage

    def heal_adventurer(self, heal_pot : HealthPotion):
        """ Helper method to heal adventurer based on the health potion.
        To be used by the main method. Adventurer has to be alive to use potion.

        Encapsulation pillar power doubles the potency of healing potions.
        All pillars collected increases maximum hit points

        :param: HealthPotion - heal values that will increment current health
        :raise: TypeError - raised when a health potion is not a parameter
        :return:
            heal - potion heal amount,
            actual_heal - adventurer health increased by potion
        :rtype: int
        """
        if isinstance(heal_pot, HealthPotion):
            heal = heal_pot.action()

            if self.has_all_pillars():
                self.max_hitpoints += heal

            if self.pillars_collected["E"]:     # Non adjusted health intentional, otherwise too strong.
                heal *= 2

            old_health = self.current_hitpoints
            new_health = self.current_hitpoints + heal

            if new_health >= self.max_hitpoints:
                self.current_hitpoints = self.max_hitpoints
            else:
                self.current_hitpoints = new_health

            actual_heal = self.current_hitpoints - old_health
            
            return heal, actual_heal

        else:
            raise TypeError("Health potion needs to passed into this method.")

    def has_health_potion(self):
        """ Helper method to decrement health potions in the adventurer's
        inventory. To be used by the main method.
        :return: boolean - True if adventurer is able to use a potion.
        """
        if self.health_pots > 0:
            self.health_pots -= 1
            return True

        return False

    def has_vision_potion(self):
        """ Helper method to decrement vision potions in the adventurer's
        inventory. To be used by the main method.
        :return: boolean - True if adventurer is able to use a potion.
        """
        if self.vision_pots > 0:
            self.vision_pots -= 1
            return True

        return False

    def _create_adventurer(self, name, challenge):
        """Helper method for character creation. Difficulty and name are checked,
        based on those values, create an adventurer with modified base values.

        :param: name: str if found in cheat_code dictionary, modification applied to adventurer
        :param: challenge: str sets to following challenge level:

        difficulty
            (hp modification, max hitpoints, default health potion, default vision potion)
        cheat_codes
            (max_hp, potions, pillar_collect_status)
        """
        difficulty = {
            "easy"      : (3, 100, 2, 2),
            "medium"    : (2, 95, 1, 1),
            "hard"      : (1, 90, 1, 1),
            "inhumane"  : (1, 85, 0, 1)
        }

        cheat_codes = {
            "gary"      : (150, 5, True),
            "hcf"       : (1, 15, True),
            "kevin"     : (185, 25, False),
            "tom"       : (1000, 0, False)
        }

        if challenge in difficulty:
            hp_mod = difficulty[challenge][0]
            self.max_hitpoints = difficulty[challenge][1]
            self.max_hitpoints += hp_mod * random.randint(0, 10)

            self.health_pots = difficulty[challenge][2]
            self.vision_pots = difficulty[challenge][3]

        if name in cheat_codes:
            self.dev_powers = True
            self.max_hitpoints = cheat_codes[name][0]

            self.health_pots = cheat_codes[name][1]
            self.vision_pots = cheat_codes[name][1]

            for value in self.pillars_collected:
                self.pillars_collected[value] = cheat_codes[name][2]

        self.current_hitpoints = self.max_hitpoints

    def _readable_pillars(self):
        """ Helper method for converting pillars collection to a player readable string.
        This took longer than I care to admit...
        :return: string
        """

        pillar_str = []
        status_str = []
        readable = "| "

        for pillar in self.pillars_collected:
            if pillar == "A":
                pillar_str.append("Abstraction")
            elif pillar == "P":
                pillar_str.append("Polymorphism")
            elif pillar == "I":
                pillar_str.append("Inheritance")
            else:
                pillar_str.append("Encapsulation")

        for status in self.pillars_collected.values():
            if status is True:
                status_str.append("Collected")
            else:
                status_str.append("Not collected")

        for pillar, status in zip(pillar_str, status_str):
            readable += pillar + ": " + status + " | "

        return readable

    def __str__(self):
        player_stats = f"Name: {self.name}\n"
        player_stats += f"HP: {self.current_hitpoints} / {self.max_hitpoints}\n"
        player_stats += f"Health potions: {self.health_pots}\n"
        player_stats += f"Vision potions: {self.vision_pots}\n"
        player_stats += f"Object Oriented Pillars Collected\n{self._readable_pillars()}\n"
        return player_stats

    def __repr__(self):
        player_stats = f"{self.name}\n"
        player_stats += f"{self.current_hitpoints} / {self.max_hitpoints}\n"
        player_stats += f"{self.health_pots}\n"
        player_stats += f"{self.vision_pots}\n"
        player_stats += f"{self.pillars_collected}\n"
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
                raise ValueError("Cannot set health potions to a negative value.")

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
                raise ValueError("Cannot set vision potions to a negative value.")

    @property
    def pillars_collected(self):
        """Returns the pillars that have been collected during the game session

        :return: str of dictionary values {pillar : bool}
        """
        return self.__pillars_collected
