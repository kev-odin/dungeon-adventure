from app.model.characters.warrior import Warrior
from app.model.characters.adventurer import Adventurer
from app.model.dungeon.dungeon_builder import DungeonBuilder
from unittest import TestCase


class TestWarrior(TestCase):
    def setUp(self) -> None:
        db = DungeonBuilder()
        self._warrior = db.build_adventurer("Hajax with an Axe", "Warrior")

    def test_init(self):
        try:
            self.setUp()
            self.assertEqual(True, True)
        except BaseException:
            self.fail("Something went wrong with initializing.")

    def test_use_special(self):
        actual = self._warrior.use_special()
        if actual == 0:
            self.assertTrue(True)
        elif 75 <= actual <= 175:
            self.assertTrue(True)
        else:
            self.fail("Either should hit for 0 or 75-175")

    def test_is_instance(self):
        self.assertTrue(isinstance(self._warrior, Adventurer))

    def test_use_super_methods(self):
        self.assertEqual(0.2, self._warrior.block_chance, "Check can access super methods")

    def test_take_damage(self):
        self._warrior.take_damage(10, always_hits=True)
        self.assertEqual(115, self._warrior.current_hitpoints, "Check damage registered")

    def test_attack(self):
        actual = self._warrior.attack()
        if actual == 0:
            self.assertTrue(True)
        elif 35 <= actual <= 60:
            self.assertTrue(True)
        else:
            self.fail("Either should hit for 0 or 35-60")
