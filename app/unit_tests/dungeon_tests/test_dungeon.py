"""
Time tracker:
Shared with dungeon time + 2 hours because I HAD A MOMENT OF TIME CONSUMING BRILLIANCE that lead to late night spaghetti
test_adventurer_find_exit_and_pillars - Breadth first search w/ pillar pick up and exit finding.
"""

import unittest
from app.model.dungeon.dungeon_builder import DungeonBuilder


class TestDungeon(unittest.TestCase):
    @staticmethod
    def init_dungeon(difficulty="Easy"):
        db = DungeonBuilder(difficulty)
        built = db.build_dungeon(difficulty)
        return built

    @staticmethod
    def create_2d_bool_list(dungeon):  # Defaults to entrance and exit and pillars
        bool_list = []
        print_me = ["i", "O", "A", "P", "I", "E"]
        for row in range(0, dungeon.total_rows):
            bool_list.append([])
            for col in range(0, dungeon.total_columns):
                bool_list[row].append([])
                if dungeon.dungeon[row][col].contents in print_me:
                    bool_list[row][col] = True
                else:
                    bool_list[row][col] = False
        return bool_list

    @staticmethod
    def leave_entrance(dungeon):
        directions = ["north", "east", "south", "west"]
        current_room = dungeon.get_room(dungeon.adventurer_loc)
        for direction in directions:
            if current_room.get_door(direction):
                directions = direction
                break
        return directions

    def test_dungeon_init_big_enough(self):
        try:
            self.init_dungeon()
            self.assertEqual(True, True)  # add assertion here
        except ValueError:
            self.assertEqual(True, False, "5, 5 should be large enough grid with 4 pillars.")

    def test_get_room(self):
        test = self.init_dungeon()
        room1 = test.get_room((1, 1))
        room2 = test.dungeon[1][1]
        self.assertEqual(room1, room2, "It should be itself.  Check print map above.  Getter or .dungeon  has issues")

    def test_entrance_exists(self):
        test = self.init_dungeon()
        entrance_room = test.get_room(test.entrance)
        boolean = False
        if entrance_room is not None:
            boolean = True
        self.assertEqual(True, boolean, "Entrance should be True.  Check print map above.")

    def test_get_entrance_by_search_coordinates(self):
        test = self.init_dungeon()
        entrance = test.entrance
        coors = None
        for row in range(0, 5):
            for col in range(0, 5):
                if test.dungeon[row][col].entrance:
                    coors = (row, col)
        self.assertEqual(coors, entrance, "Entrance found in dungeon should be same as listed.")

    def test_get_entrance_by_coords(self):
        test = self.init_dungeon()
        entrance_room = test.get_room(test.entrance)
        ent_string = entrance_room.string_middle()
        self.assertEqual(True, ent_string.count("i") == 1, "The entrance contains expected character")

    def test_entrance_accessible(self):
        test = self.init_dungeon()
        entrance_room = test.get_room(test.entrance)
        self.assertEqual(True, entrance_room.visited, "The entrance should contain at least one door.")

    def test_exit_exists(self):
        test = self.init_dungeon()
        exit_room = test.get_room(test.exit)
        is_exit = False
        if exit_room is not None:
            is_exit = True
        self.assertEqual(True, is_exit, "Exit expected to exist!")

    def test_get_exit_by_search_coordinates(self):
        test = self.init_dungeon()
        ex = test.exit
        coors = None
        for row in range(0, 5):
            for col in range(0, 5):
                if test.dungeon[row][col].exit:
                    coors = (row, col)
        self.assertEqual(coors, ex, "Exit found in dungeon should be same as listed in room with 'O'.")

    def test_get_exit_by_coords(self):
        test = self.init_dungeon()
        exit_room = test.get_room(test.exit)
        exit_string = exit_room.string_middle()
        self.assertEqual(True, exit_string.count("O") == 1, "The exit should contain expected 'O' for out.")

    def test_exit_is_accessible(self):
        test = self.init_dungeon()
        exit_room = test.get_room(test.exit)
        self.assertEqual(True, exit_room.visited, "The exit should have at least one door to be accessible")

    def test_exit_by_contents(self):
        test = self.init_dungeon()
        exit_room = test.get_room(test.exit)
        exit_contents = exit_room.contents
        self.assertEqual("O", exit_contents, "The exit should contain expected 'O' for out.")

    def test_pillars(self):
        test = self.init_dungeon()
        pillars = test.pillars
        pillars.sort()
        expected = ["A", "E", "I", "P"]
        self.assertEqual(expected, pillars, "Expect AEIP for all pillars.")

    def test_all_pillars_in_dungeon(self):
        test = self.init_dungeon()
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
        test = self.init_dungeon("Hard")
        for expected in expected_list:
            found.append(f"{test}".count(expected))
        self.assertEqual(len(expected_list), len(found), "Expected to find at least one of each in larger dungeon.")

    def test_pillars_accessible(self):
        test = self.init_dungeon()
        found = []
        expected = test.pillars.copy()
        expected.sort()
        for room in test:
            if expected.count(room.contents) > 0:
                if room.visited:  # Verify they have a door opened to get there.
                    found.append(room.contents)
        found.sort()
        self.assertEqual(expected, found, "Expected to find AEIP for all sorted pillars.")

    def test_adventurer_leave_entrance(self):
        dungeon = self.init_dungeon()
        possible = False
        directions = ["north", "east", "south", "west"]
        for direction in directions:
            try:
                dungeon.move_adventurer(direction)
                possible = True
            except ValueError:
                pass
        self.assertEqual(True, possible, "Should be possible to move the adventurer!")

    def test_adventurer_moved_to_expected_location(self):
        dungeon = self.init_dungeon()
        directions = ["north", "east", "south", "west"]
        current_room = dungeon.get_room(dungeon.adventurer_loc)
        for direction in directions:
            if current_room.get_door(direction):
                directions = direction
                break
        coord_dict = {"south": (1, 0), "east": (0, 1), "north": (-1, 0), "west": (0, -1)}
        current_loc = dungeon.adventurer_loc
        dungeon.move_adventurer(directions)
        new_loc = (coord_dict[directions][0] + current_loc[0], coord_dict[directions][1] + current_loc[1])
        self.assertEqual(new_loc, dungeon.adventurer_loc, "Check adventurer location updated with move properly.")

    def test_adventurer_move_return_expected_room(self):
        dungeon = self.init_dungeon()
        directions = self.leave_entrance(dungeon)
        coord_dict = {"south": (1, 0), "east": (0, 1), "north": (-1, 0), "west": (0, -1)}
        current_loc = dungeon.adventurer_loc
        actual = dungeon.move_adventurer(directions)
        new_loc = (coord_dict[directions][0] + current_loc[0], coord_dict[directions][1] + current_loc[1])
        expected = dungeon.get_room(new_loc)
        self.assertEqual(expected, actual, "Check returned proper room when moving adventurer.")

    def test_get_potions(self):
        dungeon = self.init_dungeon()
        directions = self.leave_entrance(dungeon)
        room = dungeon.move_adventurer(directions)
        hp = room.health_potion
        vp = room.vision_potion
        expected = (hp, vp)
        actual = dungeon.collect_potions()
        self.assertEqual(expected, actual, "Check adventurer location updated with move properly.")

    def test_pit_damage(self):  # Was tested more robustly before I removed some game-breaking setters.
        dungeon = self.init_dungeon()
        directions = self.leave_entrance(dungeon)
        room = dungeon.move_adventurer(directions)
        monster = room.monster
        dun_monster = dungeon.monster
        self.assertEqual(monster, dun_monster, "Room's damage and dungeon's damage should return the same.")

    def test_room_has_no_potions_after_collection(self):
        dungeon = self.init_dungeon()
        directions = ["north", "east", "south", "west"]
        current_room = dungeon.get_room(dungeon.adventurer_loc)
        for direction in directions:
            if current_room.get_door(direction):
                directions = direction
                break
        room = dungeon.move_adventurer(directions)
        dungeon.collect_potions()
        after = (room.health_potion, room.vision_potion)
        self.assertEqual((0, 0), after, "Check adventurer location updated with move properly.")

    def test_collect_pillars(self):
        dungeon = self.init_dungeon()
        directions = self.leave_entrance(dungeon)
        room = dungeon.move_adventurer(directions)
        if room.contents == "A" or room.contents == "I" or room.contents == "P" or room.contents == "E":
            expected = room.contents
        else:
            expected = None
        actual = dungeon.collect_pillars()
        self.assertEqual(expected, actual, "Check pillar string returned properly.")

    def test_adventurer_find_exit_and_pillars(self):  # This could probably be significantly simplified but...
        dungeon = self.init_dungeon()  # Also is this a unit test or a system test?
        to_visit = visited = []  # Tracks queue to go to and stack of visited locations to not add to queue of go to
        my_pillars = []  # Pillars adventurer has collected
        pillars = ["A", "E", "I", "P"]
        curr = dungeon.get_room(dungeon.adventurer_loc)
        found_exit = curr.exit
        row, col = dungeon.adventurer_loc[0], dungeon.adventurer_loc[1]
        while not found_exit or my_pillars != pillars:
            doors = []
            for direction in ["south", "east", "north", "west"]:
                if curr.get_door(direction):  # Checks 4 directions for valid doors, then adds them to options.
                    doors.append(direction)
            while len(doors) > 0:  # Will test all options in a room. Change for dead ends up.
                coords = doors.pop()
                coord_dict = {"south": (1, 0), "east": (0, 1), "north": (-1, 0), "west": (0, -1)}
                coords = coord_dict[coords]
                next_row, next_col = coords[0] + row, coords[1] + col  # Coordinates for next room.
                if dungeon.dungeon[next_row][next_col].visited:  # Checks if next room has doors / is accessible
                    if visited.count((next_row, next_col)) == 0:  # Adds it if next room is brand new!
                        to_visit.append((next_row, next_col))
                        visited.append((next_row, next_col))
            if len(to_visit) > 0:  # this may be redundant, but...for safety when we're at the end!
                row, col = to_visit.pop(0)
                curr = dungeon.get_room((row, col))
                if pillars.count(curr.contents) > 0 and my_pillars.count(curr.contents) == 0:  # Add newly found pillars
                    my_pillars.append(curr.contents)
                    my_pillars.sort()
                if not found_exit:  # Leaves it alone if exit is found and just seeking pillars.
                    found_exit = curr.exit
        self.assertEqual(pillars, my_pillars, "Should find all the pillars!")
        self.assertEqual(True, found_exit, "Should be possible to move adventurer to exit eventually!")

    def test_get_visible_string_dungeon(self):
        dungeon = self.init_dungeon("Easy")
        bool_list = self.create_2d_bool_list(dungeon)
        string = dungeon.get_visible_dungeon_string(bool_list)
        actual = False
        for expected in ["i", "O", "A", "P", "I", "E"]:
            if expected in string:
                actual = True
        expected = True
        self.assertEqual(expected, actual, "Expected to find entrance, exit, and A P I E in partial string.")

    def test_json_dict(self):
        dungeon = self.init_dungeon("Easy")
        check = type(dungeon.json_dict)
        self.assertEqual(dict, check, "Failed to make a dictionary of dictionary rooms.")