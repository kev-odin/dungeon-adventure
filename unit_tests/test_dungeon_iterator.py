import unittest
from dungeon import Dungeon


class TestDungeonIterator(unittest.TestCase):
    def test_iterator_whole_dungeon(self):
        test = Dungeon(5, 5)
        test_iter = test.DungeonIterator(test.dungeon, 5)
        row_max = 5
        col_max = 5
        index = 0
        while index < (row_max * col_max):
            next(test_iter)
            index += 1
        with self.assertRaises(StopIteration):
            next(test_iter)

    def test_iterator_get_correct_room_full_access(self):
        test = Dungeon(5, 5)
        row = col = 0
        col_max = 5
        for room in test:
            self.assertEqual(room, test.get_room((row, col)), "Returned room should match get room.  Check iteration.")
            col += 1
            if col >= col_max:
                col = 0
                row += 1
