from app.model.items.health_potion import HealthPotion
from app.model.characters.dungeon_character import DungeonCharacter
from abc import abstractmethod
from abc import ABC


class Adventurer(DungeonCharacter, ABC):
    """Adventurer that traverses through the maze. Picks up potions, falls into pits, and
    must complete the maze with all OOP pillars (APIE) collected to win.
    """

    def __init__(self, adv_dict: dict):
        """Adventurer object that maintains the inventory collection of potions,
        pillars collected, and current hitpoints.

        :param adv_dict: dict of adventurer data
        """
        super().__init__(adv_dict)
        self.__char_dict = adv_dict

        self.__health_pots = 0
        self.__vision_pots = 0
        self.__pillars_collected = {
            "A": False,
            "P": False,
            "I": False,
            "E": False
        }

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

    def heal_adventurer(self, heal_pot: HealthPotion):
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

            if self.pillars_collected["E"]:  # Non adjusted health intentional, otherwise too strong.
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

    def take_damage(self, damage):
        """
        Adventurer takes damage, most likely from combat.
        Inheritance pillar power reduces pit damage by half.
        :param damage:
        :return:
        """
        if self.pillars_collected["I"]:
            damage = damage // 2

        return super().take_damage(damage)

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

    @property
    def adv_class(self):
        return self.__char_dict["adv_class"]

    @property
    def special(self):
        return self.__char_dict["special"]

    @property
    def block_chance(self):
        return self.__char_dict["block_chance"]

    @abstractmethod
    def use_special(self):
        pass
