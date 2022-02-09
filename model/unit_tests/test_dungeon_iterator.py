import unittest

from model.dungeon.dungeon_builder import DungeonBuilder


class TestDungeonIterator(unittest.TestCase):
    def test_iterator_whole_dungeon(self):
        db = DungeonBuilder()
        test = db.build_dungeon()
        test_iter = test.DungeonIterator(test.dungeon, 5)
        row_max = 5  # Defaults
        col_max = 5  # Defaults
        index = 0
        while index < (row_max * col_max):
            next(test_iter)
            index += 1
        with self.assertRaises(StopIteration):
            next(test_iter)

    def test_iterator_get_correct_room_full_access(self):
        db = DungeonBuilder()
        test = db.build_dungeon()
        row = col = 0
        col_max = 5
        for room in test:
            self.assertEqual(room, test.get_room((row, col)), "Returned room should match get room.  Check iteration.")
            col += 1
            if col >= col_max:
                col = 0
                row += 1
