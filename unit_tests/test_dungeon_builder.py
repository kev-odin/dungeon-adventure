import unittest
from dungeon_builder import DungeonBuilder
from dataclasses import dataclass
from room import Room


class TestDungeonBuilder(unittest.TestCase):
    @staticmethod
    def init_diff_expected(difficulty):
        expected = {"easy": [0.05, 0.1, 0.05, 0.05, 0.1, 2, 1, 10, 5, 5],
                    "medium": [0.07, 0.1, 0.05, 0.1, 0.12, 2, 1, 20, 8, 8],
                    "hard": [0.08, 0.1, 0.05, 0.15, 0.15, 1, 1, 30, 10, 10],
                    "inhumane": [0.1, 0.01, 0.01, 0.3, 0.2, 1, 0, 80, 20, 20]}[difficulty]
        return expected

    @staticmethod
    def get_builder_diff_params(difficulty):
        db = DungeonBuilder(difficulty)
        actual = [db._DungeonBuilder__impassable_chance, db._DungeonBuilder__hp_pot_chance,
                  db._DungeonBuilder__vision_chance, db._DungeonBuilder__many_chance, db._DungeonBuilder__pit_chance,
                  db._DungeonBuilder__max_hp_pots, db._DungeonBuilder__max_vision, db._DungeonBuilder__max_pit_damage,
                  db._DungeonBuilder__row_count, db._DungeonBuilder__col_count]
        return actual

    def test_init_medium(self):
        difficulty = "medium"
        expected = self.init_diff_expected(difficulty)
        actual = self.get_builder_diff_params(difficulty)
        for index in range(0, len(expected)):
            self.assertEqual(expected[index], actual[index], f"Check init for {difficulty}")

    def test_init_easy(self):
        difficulty = "easy"
        expected = self.init_diff_expected(difficulty)
        actual = self.get_builder_diff_params(difficulty)
        for index in range(0, len(expected)):
            self.assertEqual(expected[index], actual[index], f"Check init for {difficulty}")

    def test_init_hard(self):
        difficulty = "hard"
        expected = self.init_diff_expected(difficulty)
        actual = self.get_builder_diff_params(difficulty)
        for index in range(0, len(expected)):
            self.assertEqual(expected[index], actual[index], f"Check init for {difficulty}")

    def test_init_inhumane(self):
        difficulty = "inhumane"
        expected = self.init_diff_expected(difficulty)
        actual = self.get_builder_diff_params(difficulty)
        for index in range(0, len(expected)):
            self.assertEqual(expected[index], actual[index], f"Check init for {difficulty}")

    def test_build_a_room(self):
        db = DungeonBuilder("easy", varied=False)
        room1 = db._DungeonBuilder__build_room()
        room2 = db._DungeonBuilder__build_room()
        self.assertEqual(room1, room2, "Rooms expected to be equal when not varied.")

    def test__reset(self):
        db = DungeonBuilder()
        db.build_dungeon("hard")
        db._DungeonBuilder__reset("medium")
        self.assertEqual("medium", db._DungeonBuilder__difficulty, "Should be reset to medium.")

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
        pass

    def test__is_traversable(self):
        pass

    def test__is_valid_room(self):
        pass

    def test__get_room(self):
        pass

    def test_get_dungeon(self):
        pass

    def test_build_dungeon(self):
        pass

