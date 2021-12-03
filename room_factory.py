"""
Steph time tracker:
5 minutes (copy pastaed from dungeon and moved it here with some minor edits to make a static simple factory)
Limitations: Currently has hardcoded defaults.  We could modify this somewhat simply with a difficulty setting parameter
instead.  May possibly implement once most refactoring is done to keep that over 100% grade ;)
"""

from room import Room
import random


class RoomFactory:
    @staticmethod
    def create_room(total_rooms: int, impassable_chance=0.05, hp_pot_chance=0.1, vision_chance=0.05, many_chance=0.05,
                    pit_chance=0.1, max_hp_pots=2, max_vision=1, max_pit_damage=20):
        random_number = random.randint(0, total_rooms)
        intrigue = random_number / total_rooms
        many_trigger = impassable_chance + many_chance  # range of impassable through many
        hp_trigger = many_trigger + hp_pot_chance  # range of many trigger through hp pot chance
        vision_trigger = hp_trigger + vision_chance  # range of hp trigger through vision trigger
        pit_trigger = vision_trigger + pit_chance
        if intrigue <= impassable_chance:
            new_room = Room(impassable=True)
        elif intrigue <= many_trigger:
            new_room = Room(health_potion=random.randint(0, max_hp_pots),
                            vision_potion=random.randint(0, max_vision),
                            pit=random.randint(0, max_pit_damage))
        elif intrigue <= hp_trigger:
            new_room = Room(health_potion=random.randint(0, max_hp_pots))
        elif intrigue <= vision_trigger:
            new_room = Room(vision_potion=random.randint(0, max_vision))
        elif intrigue <= pit_trigger:
            new_room = Room(pit=random.randint(1, max_pit_damage))
        else:  # Boring empty room.
            new_room = Room()
        return new_room
