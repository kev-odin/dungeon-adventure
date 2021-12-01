import unittest
from dungeon import Dungeon


class TestDungeon(unittest.TestCase):
    def test_dungeon_init(self):
        test = Dungeon(5, 5)

        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
