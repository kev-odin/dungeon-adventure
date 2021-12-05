"""
        :param hp_pot_chance: float, chance of HP potion appearing in dungeon.
        :param vision_chance: float, chance of vision potion appearing in dungeon.
        :param many_chance: float, chance of pits, hp potions, vision potions appearing in a single room.
        :param pit_chance: float, chance of pits appearing in the dungeon.
        :param max_hp_pots: int, maximum number of HP potions in a room.
        :param max_vision: int, maximum number of vision potions possible to be found in a room.
        :param max_pit_damage: int, maximum amount of damage an adventurer can experience if they land in a pit.
"""


class DungeonBuilder:
    def __init__(self, difficulty):
        diff_index = {"easy": 0, "medium": 1, "hard": 2, "inhumane": 3}
        if diff_index.get(difficulty) >= 0:
            pass
        else:
            raise ValueError("difficulty must be easy, medium, hard, or inhumane")

    def build_dungeon(self):
        pass
