import unittest
from dungeon import Dungeon


class TestDungeon(unittest.TestCase):
    def test_dungeon_init_big_enough(self):
        test = Dungeon(5, 5)
        print(f"{test}")
        self.assertEqual(True, True)  # add assertion here

    def test_dungeon_init_too_small(self):
        try:
            test = Dungeon(1, 1)
            self.assertEqual(True, False, "Check verification dungeon is large enough to hold pillars.")
        except ValueError:
            self.assertEqual(True, True)

    def test_create_a_room(self):
        test = Dungeon(5, 5)
        room1 = test.create_room()
        room2 = test.create_room()
        room1.clear_room()
        room2.clear_room()
        self.assertEqual(f"{room1}", f"{room2}", "Cleared rooms created from dungeon expected to be equal.")


if __name__ == '__main__':
    unittest.main()
