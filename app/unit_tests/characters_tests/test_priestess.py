from app.model.characters.priestess import Priestess
from app.model.characters.adventurer import Adventurer
from app.model.characters.healable import HealAble
from app.model.dungeon.dungeon_builder import DungeonBuilder

from unittest import TestCase


class TestPriestess(TestCase):
    def setUp(self) -> None:
        db = DungeonBuilder()
        self._priestess = db.build_adventurer("Lady Briarwood", "Priestess")

    def test_init(self):
        try:
            self.setUp()
            self.assertEqual(True, True)
        except BaseException:
            self.fail("Something went wrong with initializing.")

    def test_use_special_0(self):
        actual = self._priestess.use_special()
        self.assertEqual(0, actual, "Should be full health and heal 0.")

    def test_is_instance(self):
        self.assertTrue(isinstance(self._priestess, Adventurer))

    def test_use_super_methods(self):
        self.assertEqual(0.3, self._priestess.block_chance, "Check can access super methods")

    def test_take_damage(self):
        self._priestess.take_damage(10)
        self.assertEqual(65, self._priestess.current_hitpoints, "Check damage registered")

    def test_heal_damage(self):
        self._priestess.take_damage(50)
        actual = self._priestess.use_special()
        self.assertLessEqual(17, actual, "Should heal at least minimum.")
