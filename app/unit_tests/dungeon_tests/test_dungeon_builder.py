import unittest
from app.model.dungeon.dungeon_builder import DungeonBuilder
from app.model.dungeon.room import Room
from app.model.dungeon.dungeon import Dungeon
from app.model.dungeon.adventurer import Adventurer
from app.model.db.query_helper import QueryHelper


class TestDungeonBuilder(unittest.TestCase):
    @staticmethod
    def init_diff_expected(difficulty):
        qh = QueryHelper()
        expected = qh.query(difficulty)
        return expected

    @staticmethod
    def get_builder_diff_params(difficulty):
        db = DungeonBuilder(difficulty)
        actual = db._DungeonBuilder__settings
        return actual

    def test_init_medium(self):
        difficulty = "medium"
        expected = self.init_diff_expected(difficulty)
        actual = self.get_builder_diff_params(difficulty)
        self.assertDictEqual(expected, actual, f"Check init for {difficulty}")

    def test_init_medium_size(self):
        db = DungeonBuilder()
        dungeon = db.build_dungeon("medium")
        self.assertEqual(8, dungeon.total_rows, f"Total rows in medium dungeon should be 8 {dungeon.total_rows}")
        self.assertEqual(8, dungeon.total_columns, f"Total rows in medium dungeon should be 8 {dungeon.total_columns}")

    def test_init_easy(self):
        difficulty = "easy"
        expected = self.init_diff_expected(difficulty)
        actual = self.get_builder_diff_params(difficulty)
        self.assertDictEqual(expected, actual, f"Check init for {difficulty}")

    def test_init_easy_size(self):
        db = DungeonBuilder()
        dungeon = db.build_dungeon("easy")
        self.assertEqual(5, dungeon.total_rows, f"Total rows in easy dungeon should be 5 {dungeon.total_rows}")
        self.assertEqual(5, dungeon.total_columns, f"Total rows in easy dungeon should be 5 {dungeon.total_columns}")

    def test_init_hard(self):
        difficulty = "hard"
        expected = self.init_diff_expected(difficulty)
        actual = self.get_builder_diff_params(difficulty)
        self.assertDictEqual(expected, actual, f"Check init for {difficulty}")

    def test_init_hard_size(self):
        db = DungeonBuilder()
        dungeon = db.build_dungeon("hard")
        self.assertEqual(10, dungeon.total_rows, f"Total rows in hard dungeon should be 10 {dungeon.total_rows}")
        self.assertEqual(10, dungeon.total_columns, f"Total rows in hard dungeon should be 10 {dungeon.total_columns}")

    def test_init_inhumane(self):
        difficulty = "inhumane"
        expected = self.init_diff_expected(difficulty)
        actual = self.get_builder_diff_params(difficulty)
        self.assertDictEqual(expected, actual, f"Check init for {difficulty}")

    def test_init_inhumane_size(self):
        db = DungeonBuilder()
        dungeon = db.build_dungeon("inhumane")
        self.assertEqual(20, dungeon.total_rows, f"Total rows in inhumane dungeon should be 20 {dungeon.total_rows}")
        self.assertEqual(20, dungeon.total_columns, f"Total rows in inhumane dungeon should be 20 {dungeon.total_columns}")

    def test_build_a_room(self):
        db = DungeonBuilder("easy", varied=False)
        room1 = db._DungeonBuilder__build_room()
        room2 = db._DungeonBuilder__build_room()
        self.assertEqual(room1, room2, "Rooms expected to be equal when not varied.")

    def test__reset(self):
        db = DungeonBuilder()
        db.build_dungeon("hard")
        db._DungeonBuilder__reset("medium")
        self.assertEqual("medium", db._DungeonBuilder__settings["difficulty"], "Should be reset to medium.")

    def test__set(self):
        db = DungeonBuilder()
        db.build_dungeon()
        db._DungeonBuilder__set_dungeon()
        self.assertIsNotNone(db._DungeonBuilder__complete_dungeon, "Should have set complete_dungeon to a variable.")

    def test__get_rand_coords(self):
        db = DungeonBuilder()
        coords = db._DungeonBuilder__get_rand_coords()
        for coord in coords:
            self.assertLessEqual(coord, 5, "Should be below 5 in default for coordinate generation.")
            self.assertGreaterEqual(coord, 0, "Should be greater than or equal to 0 for random coordinates.")

    def test__build_2d_room_maze(self):
        db = DungeonBuilder()
        db._DungeonBuilder__build_2d_room_maze()
        dungeon = db._DungeonBuilder__dungeon
        len(dungeon)
        for data in dungeon:
            for room in data:
                is_instance = isinstance(room, Room)
                self.assertEqual(True, is_instance, "All contents of dungeon array should be rooms.")
        self.assertEqual(5, len(dungeon), "Rows should be 5")

    def test__build_dungeon_path(self):
        db = DungeonBuilder("hard", varied=False)
        db._DungeonBuilder__build_2d_room_maze()
        ent_row, ent_col = (1, 1)
        exit_row, exit_col = (0, 1)
        db._DungeonBuilder__dungeon[ent_row][ent_col].entrance = True  # Clears all items then sets contents to i
        db._DungeonBuilder__dungeon[exit_row][exit_col].exit = True  # Clears all items then sets contents to O
        possible = db._DungeonBuilder__build_dungeon_path(ent_row, ent_col)
        self.assertEqual(True, possible, "Should be able to build paths with boring dungeon.")

    def test__build_pillars(self):
        db = DungeonBuilder(varied=False)
        dungeon = db.build_dungeon()  # Sort of cheating by using this instead of testing method directly
        found = []
        expected = dungeon.pillars.copy()
        expected.sort()
        for room in dungeon:
            if expected.count(room.contents) > 0:
                if room.visited:  # Verify they have a door opened to get there.
                    found.append(room.contents)
        found.sort()
        self.assertEqual(expected, found, "Expected to find AEIP for all sorted pillars.")

    def test__is_traversable_out_of_bounds(self):
        db = DungeonBuilder()
        dungeon = db.build_dungeon()
        self.assertEqual(False, db._DungeonBuilder__is_traversable(6, 6), "Coords out of bound of default dungeon.")

    def test__is_traversable_already_visited(self):
        db = DungeonBuilder()
        dungeon = db.build_dungeon()
        row, col = dungeon.entrance
        self.assertEqual(False, db._DungeonBuilder__is_traversable(row, col), "Already visited.")

    def test__is_traversable_already_visited(self):
        db = DungeonBuilder()
        with self.assertRaises(IndexError):  # Should raise an error when trying to traverse nonexistence dungeon
            db._DungeonBuilder__is_traversable(0, 0)

    def test__is_traversable_true(self):  # Index error i
        db = DungeonBuilder()
        dungeon = db.build_dungeon()
        room = dungeon.get_room((0, 0))
        for direction in ["north", "south", "east", "west"]:
            room.set_door(direction, False)
        self.assertEqual(True, db._DungeonBuilder__is_traversable(0, 0), "Should be able to traverse.")

    def test__is_valid_room(self):
        db = DungeonBuilder()
        self.assertEqual(False, db._DungeonBuilder__is_valid_room(6, 6), "Coords out of bound of default dungeon.")

    def test__get_room(self):
        db = DungeonBuilder()
        dungeon = db.build_dungeon()
        db_room = db._DungeonBuilder__get_room((0, 1))
        dun_room = dungeon.get_room((0, 1))
        self.assertEqual(db_room, dun_room, "Expect same results from both getters though different objects.")

    def test_build_dungeon(self):
        db = DungeonBuilder()
        dungeon = db.build_dungeon()
        is_a_dungeon = isinstance(dungeon, Dungeon)
        self.assertEqual(True, is_a_dungeon, "Expected type of build_dungeon results to be a dungeon")

    def test_build_adventurer(self):
        db = DungeonBuilder()
        adventurer = db.build_adventurer("Bob", "Priestess")
        is_a_adventurerer = isinstance(adventurer, Adventurer)
        self.assertTrue(is_a_adventurerer, "Expected adventurer to be type adventurer")
