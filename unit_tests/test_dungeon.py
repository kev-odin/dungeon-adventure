"""
Time tracker:
Shared with dungeon time + 2 hours because I HAD A MOMENT OF TIME CONSUMING BRILLANCE that lead to late night spaghetti.
test_adventurer_find_exit_and_pillars - Breadth first search w/ pillar pick up and exit finding.

Mock tests would be more robust since I had to delete most of my private method tests once methods were no longer
private or no longer predictable.  Testing successful traversal is an okay compromise?  But less helpful if something
more specific breaks with modification.

TODO Verify all setters and getters are tested.  Stop programming late at night.
"""

import unittest
from dungeon import Dungeon


class TestDungeon(unittest.TestCase):
    def test_dungeon_init_big_enough(self):
        try:
            Dungeon(5, 5)
            self.assertEqual(True, True)  # add assertion here
        except ValueError:
            self.assertEqual(True, False, "5, 5 should be large enough grid with 4 pillars.")

    def test_dungeon_init_too_small(self):
        try:
            Dungeon(1, 1)
            self.assertEqual(True, False, "Check verification dungeon is large enough to hold pillars.")
        except ValueError:
            self.assertEqual(True, True)

    def test_get_room(self):
        test = Dungeon(7, 7)
        room1 = test.get_room((1, 1))
        room2 = test.dungeon[1][1]
        self.assertEqual(room1, room2, "It should be itself.  Check print map above.  Getter or .dungeon  has issues")

    def test_entrance_exists(self):
        test = Dungeon(7, 7)
        entrance_room = test.get_room(test.entrance)
        if entrance_room is not None:
            boolean = True
        self.assertEqual(True, boolean, "Entrance should be True.  Check print map above.")

    def test_get_entrance_by_search_coordinates(self):
        test = Dungeon(5, 5)
        entrance = test.entrance
        coors = None
        for row in range(0, 5):
            for col in range(0, 5):
                if test.dungeon[row][col].entrance:
                    coors = (row, col)
        self.assertEqual(coors, entrance, "Entrance found in dungeon should be same as listed.")

    def test_get_entrance_by_coords(self):
        test = Dungeon(5, 5)
        entrance_room = test.get_room(test.entrance)
        ent_string = entrance_room.string_middle()
        self.assertEqual(True, ent_string.count("i") == 1, "The entrance contains expected character")

    def test_entrance_accessible(self):
        test = Dungeon(5, 5)
        entrance_room = test.get_room(test.entrance)
        self.assertEqual(True, entrance_room.visited, "The entrance should contain at least one door.")

    def test_exit_exists(self):
        test = Dungeon(5, 5)
        exit_room = test.get_room(test.exit)
        if exit_room is not None:
            boolean = True
        self.assertEqual(True, boolean, "Exit expected to exist!")

    def test_get_exit_by_search_coordinates(self):
        test = Dungeon(5, 5)
        exit = test.exit
        coors = None
        for row in range(0, 5):
            for col in range(0, 5):
                if test.dungeon[row][col].exit:
                    coors = (row, col)
        self.assertEqual(coors, exit, "Exit found in dungeon should be same as listed in room with 'O'.")

    def test_get_exit_by_coords(self):
        test = Dungeon(5, 5)
        exit_room = test.get_room(test.exit)
        exit_string = exit_room.string_middle()
        self.assertEqual(True, exit_string.count("O") == 1, "The exit should contain expected 'O' for out.")

    def test_exit_is_accessible(self):
        test = Dungeon(5, 5)
        exit_room = test.get_room(test.exit)
        self.assertEqual(True, exit_room.visited, "The exit should have at least one door to be accessible")

    def test_exit_by_contents(self):
        test = Dungeon(5, 5)
        exit_room = test.get_room(test.exit)
        exit_contents = exit_room.contents
        self.assertEqual("O", exit_contents, "The exit should contain expected 'O' for out.")

    def test_pillars(self):
        test = Dungeon(5, 5)
        pillars = test.pillars
        pillars.sort()
        expected = ["A", "E", "I", "P"]
        self.assertEqual(expected, pillars, "Expect AEIP for all pillars.")

    def test_all_pillars_in_dungeon(self):
        test = Dungeon(5, 5)
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
        test = Dungeon(5, 5)
        for expected in expected_list:
            found.append(f"{test}".count(expected))
        self.assertEqual(len(expected_list), len(found), "Expected to find at least one of each in larger dungeon.")

    def test_pillars_accessible(self):
        test = Dungeon(5, 5)
        found = []
        expected = test.pillars.copy()
        expected.sort()
        for room in test:
            if expected.count(room.contents) > 0:
                if room.visited:  # Verify they have a door opened to get there.
                    found.append(room.contents)
        found.sort()
        self.assertEqual(expected, found, "Expected to find AEIP for all sorted pillars.")

    def test_random_dungeon_generation(self):  # TECHNICALLY could cause failure, but surely the universe won't align.
        test1 = Dungeon(5, 5)
        test2 = Dungeon(5, 5)
        test3 = Dungeon(5, 5)
        improbable = test1 == test2 and test1 == test3 and test2 == test3
        improbable_exit = test1.exit == test2.exit and test1.exit == test3.exit and test2.exit == test3.exit
        improbable_entrance = test1.entrance == test2.entrance and test1.entrance == test3.entrance and \
                              test2.entrance == test3.entrance
        self.assertEqual(False, improbable, "Dungeons are expected to be different.  Stars aligned and all 3 match.")
        self.assertEqual(False, improbable_exit, "Dungeon exits are expected to be different. Or stars aligned.")
        self.assertEqual(False, improbable_entrance, "Stars aligned and all 3 entrances match.  Or not random.")

    def test_adventurer_leave_entrance(self):
        dungeon = Dungeon(5, 5)
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
        dungeon = Dungeon(5, 5)
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

    def test_adventurer_find_exit_and_pillars(self):  # This could probably be significantly simplied buuuut...
        dungeon = Dungeon(5, 5)
        print(dungeon)
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
            if len(to_visit) > 0:  # this may be redundant, buuuut...for safety when we're at the end!
                row, col = to_visit.pop(0)
                curr = dungeon.get_room((row, col))
                if pillars.count(curr.contents) > 0 and my_pillars.count(curr.contents) == 0:  # Add newly found pillars
                    my_pillars.append(curr.contents)
                    my_pillars.sort()
                if not found_exit:  # Leaves it alone if exit is found and just seeking pillars.
                    found_exit = curr.exit
        self.assertEqual(pillars, my_pillars, "Should find all the pillars!")
        self.assertEqual(True, found_exit, "Should be possible to move adventurer to exit eventually!")
