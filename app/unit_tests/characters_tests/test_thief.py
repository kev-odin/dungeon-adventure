from unittest import TestCase
from app.model.characters.warrior import Warrior
from app.model.characters.adventurer import Adventurer
from app.model.dungeon.dungeon_builder import DungeonBuilder

class TestThief(TestCase):
    def setUp(self) -> None:
        db = DungeonBuilder()
        self._thief = db.build_adventurer("Little Bee with a Stabby", "Thief")

    def test_init(self):
        try:
            self.setUp()
            self.assertEqual(True, True)
        except BaseException:
            self.fail("Something went wrong with initializing.")

    def test_use_special(self):
        actual = self._thief.use_special()
        if actual == 0:
            self.assertTrue(True)
        elif type(actual) is tuple:
            if 0 <= actual[0] <= 40 and 0 <= actual[1] <= 40:
                self.assertTrue(True)
            else:
                self.fail("Didn't properly provide a tuple in valid ranges.")
        elif 20 <= actual <= 40:
            self.assertTrue(True)
        else:
            self.fail("Either should hit for 0, twice, or for 20-40")

    def test_is_instance(self):
        self.assertTrue(isinstance(self._thief, Adventurer))

    def test_use_super_methods(self):
        self.assertEqual(0.4, self._thief.block_chance, "Check can access super methods")

    def test_take_damage(self):
        self._thief.take_damage(10)
        self.assertEqual(65, self._thief.current_hitpoints, "Check damage registered")

    def test_attack(self):
        actual = self._thief.attack()
        if actual == 0:
            self.assertTrue(True)
        elif 20 <= actual <= 40:
            self.assertTrue(True)
        else:
            self.fail("Either should hit for 0 or 20-40")
