"""
Time tracker:
5 minutes (copy pastaed from dungeon and moved it here with some minor edits to make a static simple factory)
"""

from room import Room
import random


class RoomFactory:
    def __init__(self, difficulty="easy"):
        diff_dict = {"easy": 0, "medium": 1, "hard": 2, "inhumane": 3}
        index = diff_dict[difficulty]
        if index is not None and index >= 0:
            self.__impassable_chance = (0.05, 0.07, 0.08, 0.1)[index]
            self.__hp_pot_chance = (0.1, 0.1, 0.1, 0.01)[index]
            self.__vision_chance = (0.05, 0.05, 0.05, 0.01)[index]
            self.__many_chance = (0.05, 0.1, 0.15, 0.3)[index]
            self.__pit_chance = (0.1, 0.12, 0.15, 0.2)[index]
            self.__max_hp_pots = (2, 2, 1, 1)[index]
            self.__max_vision = (1, 1, 1, 0)[index]
            self.__max_pit_damage = (10, 20, 30, 80)[index]
        else:
            raise ValueError("difficulty must be easy, medium, hard, or inhumane")

    def create_room(self, total_rooms: int):
        random_number = random.randint(0, total_rooms)
        intrigue = random_number / total_rooms
        many_trigger = self.__impassable_chance + self.__many_chance
        hp_trigger = many_trigger + self.__hp_pot_chance  # range of many trigger through hp pot chance
        vision_trigger = hp_trigger + self.__vision_chance  # range of hp trigger through vision trigger
        pit_trigger = vision_trigger + self.__pit_chance
        if intrigue <= self.__impassable_chance:  # Is it less than or equal to impassable chance?  Make no access room!
            new_room = Room(contents="*")
        elif intrigue <= many_trigger:
            new_room = Room(health_potion=random.randint(1, self.__max_hp_pots),
                            vision_potion=random.randint(0, self.__max_vision),
                            pit=random.randint(1, self.__max_pit_damage), contents="M")
        elif intrigue <= hp_trigger:
            new_room = Room(health_potion=random.randint(0, self.__max_hp_pots), contents="H")
        elif intrigue <= vision_trigger:
            new_room = Room(vision_potion=random.randint(0, self.__max_vision), contents="V")
        elif intrigue <= pit_trigger:
            new_room = Room(pit=random.randint(1, self.__max_pit_damage), contents="X")
        else:  # Boring empty room.  The best kind of room.
            new_room = Room()
        return new_room
