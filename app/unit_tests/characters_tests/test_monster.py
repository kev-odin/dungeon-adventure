from unittest import TestCase
from app.model.characters.monster import Monster
from app.model.dungeon.dungeon_builder import DungeonBuilder


class TestMonster(TestCase):
    def setUp(self) -> None:
        db = DungeonBuilder()
        self._ogre = db._build_monster(True)
        self._not_ogre = db._build_monster(False)

    def test_take_damage_valid(self):
        healed = self._ogre.take_damage(10)
        self.assertLessEqual(0, healed, "Verify healed occured")

    def test_take_damage_dead_no_heal(self):
        healed = self._ogre.take_damage(200)
        self.assertEqual(0, healed, "Verify healed occured")

    def test_attacking_ogre(self):
        damage = self._ogre.attack(hit_chance=100)
        if 30 <= damage <= 60:
            self.assertTrue(True)
        else:
            self.fail(f"Damage outside of bounds {damage}")
