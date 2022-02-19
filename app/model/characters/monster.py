from app.model.characters.dungeon_character import DungeonCharacter
from random import random
from app.model.characters.healable import HealAble


class Monster(DungeonCharacter, HealAble):
    def __init__(self, mon_dict):
        super().__init__(mon_dict)

    def take_damage(self, damage):
        super().take_damage(damage)
        self._heal()

    def _heal(self):
        """
        If monster is alive and meets heal percentage, heals health for number between min and max.
        :return: int amount healed or 0 if not healed at all.
        """
        monster = self.__char_dict
        if monster["heal_chance"] < random():
            heal_amount = super().heal(self.__char_dict)
            self.current_hitpoints += heal_amount
        return 0
