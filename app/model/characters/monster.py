from app.model.characters.dungeon_character import DungeonCharacter
from random import random
from app.model.characters.healable import HealAble


class Monster(DungeonCharacter, HealAble):
    def __init__(self, mon_dict):
        super().__init__(mon_dict)

    def take_damage(self, damage):
        """
        When a monster takes damage, it has a chance to heal.
        :param damage: int damage monster takes.
        :return: int reflecting amount monster healed if any
        """
        super().take_damage(damage)
        if damage > 0:
            healed = self._heal()
        else:
            healed = 0
        print(f"DEBUG in Monster, damage: {damage}, healed: {healed}")
        return healed

    def _heal(self):
        """
        If monster is alive and meets heal percentage, heals health for number between min and max.
        :return: int amount healed or 0 if not healed at all.
        """
        monster = self.char_dict
        if monster["heal_chance"] >= random():
            heal_amount = self.heal(self.char_dict)
            self.current_hitpoints += heal_amount
            return heal_amount
        return 0
