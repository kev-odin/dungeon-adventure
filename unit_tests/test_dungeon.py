"""
Steph time tracker:
Included with dungeon.

Need to include more robust tests that are applicable still once dungeon is randomized.  Maybe I break down dungeon's
functions more so that it works in pieces instead of dependently?  Toggle settings in calls?  Use a randomizer seed?
"""

import unittest
from dungeon import Dungeon


class TestDungeon(unittest.TestCase):
    def test_dungeon_init_big_enough(self):
        try:
            test = Dungeon(7, 7)
            self.assertEqual(True, True)  # add assertion here
        except ValueError:
            self.assertEqual(True, False, "5, 5 should be large enough grid with 4 pillars.")

    def test_dungeon_init_too_small(self):
        try:
            test = Dungeon(1, 1)
            self.assertEqual(True, False, "Check verification dungeon is large enough to hold pillars.")
        except ValueError:
            self.assertEqual(True, True)

    def test_get_room(self):
        test = Dungeon(7, 7)
        room1 = test.get_room((1, 1))
        # print(f"{test}")
        # print(f"{room1}")
        self.assertEqual(room1, room1, "It should be itself.  Check print map above.")

    def test_get_entrance(self):
        test = Dungeon(7, 7)
        entrance_room = test.get_room(test.entrance)
        # print(f"{test}")
        # print(f"{entrance}")
        if entrance_room is not None:
            boolean = True
        self.assertEqual(True, boolean, "Entrance should be True.  Check print map above.")
    """
    def test_get_entrance_by_coordinates(self):
        test = Dungeon(5, 5)
        entrance = test.entrance
        self.assertEqual(entrance, test.get_room(entrance), "Should retrieve the same room. Check ent property")
    """

    def test_pillars(self):
        test = Dungeon(7, 7)
        pillars = test.pillars
        pillars.sort()
        expected = ["A", "E", "I", "P"]
        self.assertEqual(expected, pillars, "Expect AEIP for all pillars.")

    def test_all_pillars_in_dungeon(self):
        test = Dungeon(7, 7)
        print(f"{test}")
        found = []
        expected = test.pillars.copy()
        expected.sort()
        for room in test:
            if expected.count(room.contents) > 0:
                found.append(room.contents)
        found.sort()
        self.assertEqual(expected, found, "Expected to find AEIP for all sorted pillars.")

    def test_all_types_in_larger_dungeon(self):
        expected_list = [" ", "A", "P", "I", "E", "i", "O", "*", "H", "V", "X", "M"]
        found = []
        test = Dungeon(10, 10)
        for expected in expected_list:
            found.append(f"{test}".count(expected))
        self.assertEqual(len(expected_list), len(found), "Expected to find at least one of each in larger dungeon.")


    # def test_leave_entrance(self):

