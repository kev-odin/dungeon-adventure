import unittest
from dungeon import Dungeon


class TestDungeon(unittest.TestCase):
    def test_dungeon_init_big_enough(self):
        try:
            test = Dungeon(5, 5)
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
        test = Dungeon(5, 5)
        room1 = test.get_room(1, 1)
        # print(f"{test}")
        # print(f"{room1}")
        self.assertEqual(room1, room1, "It should be itself.  Check print map above.")

    def test_get_entrance(self):
        test = Dungeon(5, 5)
        entrance = test.get_entrance()
        # print(f"{test}")
        # print(f"{entrance}")
        self.assertEqual(True, entrance.entrance, "Entrance should be True.  Check print map above.")

    def test_get_entrance_by_coordinates(self):
        test = Dungeon(5, 5)
        entrance = test.get_entrance()
        ent_row = test.entrance_row
        ent_col = test.entrance_col
        self.assertEqual(entrance, test.get_room(ent_row, ent_col), "Should retrieve the same room. Check ent property")

    def test_pillars(self):
        test = Dungeon(5, 5)
        pillars = test.pillars
        pillars.sort()
        expected = ["A", "E", "I", "P"]
        self.assertEqual(expected, pillars, "Expect AEIP for all pillars.")

    def test_all_pillars_in_dungeon(self):
        test = Dungeon(5, 5)
        print(f"{test}")
        found = []
        expected = ["A", "E", "I", "P"]
        for room in test:
            if room.pillar:
                found.append(room.pillar)
        found.sort()
        self.assertEqual(expected, found, "Expected to find AEIP for all sorted pillars.")


    # def test_leave_entrance(self):

