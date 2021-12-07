"""
Time tracker: 4 hours (testing still in progress -- indirectly tested via test_dungeon)
Modified simple builder pattern to allow difficulty settings and single location configuration for rooms and dungeons.
Didn't seem necessary to include the layers of abstraction for a director or multiple builders when I just wanted to put
all my creation stuff in one spot.
"""
from dungeon import Dungeon
from room import Room
import random


class DungeonBuilder:
    def __init__(self, difficulty="easy", varied=True):
        self.__reset(difficulty, varied)

    def __reset(self, difficulty="easy", varied=True):
        diff_index = {"easy": 0, "medium": 1, "hard": 2, "inhumane": 3}
        if diff_index.get(difficulty) >= 0:
            self.__diff_index = diff_index[difficulty]
        else:
            raise ValueError("difficulty must be easy, medium, hard, or inhumane")
        self.__complete_dungeon = None
        self.__varied = varied  # Toggle for whether or not to build rooms that have potions, impassible, pit. Testing.
        self.__impassable_chance = (0.05, 0.07, 0.08, 0.1)[self.__diff_index]  # chance of impassable room
        self.__hp_pot_chance = (0.1, 0.1, 0.1, 0.01)[self.__diff_index]  # chance of HP potion appearing in dungeon.
        self.__vision_chance = (0.05, 0.05, 0.05, 0.01)[self.__diff_index]  # chance of vision potion appearing
        self.__many_chance = (0.05, 0.1, 0.15, 0.3)[self.__diff_index]  # chance of pits, hp potions, vision in one room
        self.__pit_chance = (0.1, 0.12, 0.15, 0.2)[self.__diff_index]  # chance of pits appearing in the dungeon.
        self.__max_hp_pots = (2, 2, 1, 1)[self.__diff_index]  # maximum number of HP potions in a room.
        self.__max_vision = (1, 1, 1, 0)[self.__diff_index]  # maximum number of vision potions possible
        self.__max_pit_damage = (10, 20, 30, 80)[self.__diff_index]  # maximum damage pits do.
        self.__row_count = (5, 8, 10, 20)[self.__diff_index]  # Total number of rows
        self.__col_count = (5, 8, 10, 20)[self.__diff_index]  # Total number of columns
        self.__difficulty = difficulty  # Difficulty setting.
        self.__empty_rooms = []  # Stores list of empty rooms to be used later for pillar placement
        self.__dungeon = []
        self.__entrance = None
        self.__exit = None
        self.__pillars = ["A", "P", "I", "E"]

    def __set_dungeon(self):
        self.__complete_dungeon = Dungeon(self.__dungeon, self.__difficulty, self.__entrance, self.__exit)

    def __get_rand_coords(self):
        return random.randint(0, self.__row_count - 1), random.randint(0, self.__col_count - 1)

    def __build_2d_room_maze(self):
        """
        Creates a 2D list full of rooms.  Saves it to dungeon.
        :return: None
        """
        for row in range(0, self.__row_count):
            self.__dungeon.append([])
            for col in range(0, self.__col_count):
                self.__dungeon[row].append([])
                new_room = self.__build_room()
                self.__dungeon[row][col] = new_room

    def __build_room(self):
        """
        Creates a room with varied contents based on dungeon difficulty, or completely empty.
        :param varied: bool True for room generation based on difficulty of dungeon, false for an empty room.
        :return: Room, varied contents depending on dungeon difficulty or empty if turned off.
        """
        if not self.__varied:
            return Room()
        total_rooms = self.__row_count * self.__col_count
        random_number = random.randint(0, total_rooms)
        intrigue = random_number / total_rooms
        many_trigger = self.__impassable_chance + self.__many_chance
        hp_trigger = many_trigger + self.__hp_pot_chance  # range of many trigger through hp pot chance
        vision_trigger = hp_trigger + self.__vision_chance  # range of hp trigger through vision trigger
        pit_trigger = vision_trigger + self.__pit_chance
        if intrigue <= self.__impassable_chance:  # Is it less than or equal to impassable chance?  Make no access room!
            new_room = Room(contents="*")
        elif intrigue <= many_trigger:
            new_room = Room(health_potion=random.randint(1, self.__max_hp_pots),
                            vision_potion=random.randint(0, self.__max_vision),
                            pit=random.randint(1, self.__max_pit_damage), contents="M")
        elif intrigue <= hp_trigger:
            new_room = Room(health_potion=random.randint(0, self.__max_hp_pots), contents="H")
        elif intrigue <= vision_trigger:
            new_room = Room(vision_potion=random.randint(0, self.__max_vision), contents="V")
        elif intrigue <= pit_trigger:
            new_room = Room(pit=random.randint(1, self.__max_pit_damage), contents="X")
        else:  # Boring empty room.  The best kind of room.  Could probably put this first to save a lot of O(1)
            new_room = Room()
        return new_room

    def __build_dungeon_path(self, row, col):
        """
        Initial call should be entrance location.  Verifies the dungeon can be traversed from entrance to exit and adds
        any empty rooms' coordinates to the empty_rooms list as a tuple.
        :param row: int indicating current row to traverse
        :param col: int indicating current column to traverse
        :return: True if traversable, able to go from entrance to exit.  False if not.
        """
        found_exit = False
        room = self.__dungeon[row][col]
        if room.is_empty and self.__empty_rooms.count((row, col)) == 0:
            self.__empty_rooms.append((row, col))  # Places to put pillars later
        elif room.exit:  # Check for exit - assume more rooms empty than exit, so checks fewer.
            return True  # Base case.  Escape the recursion!
        else:  # not at exit so try another room:
            room_options = [0, 1, 2, 3]  # Used to choose a random direction to explore.
            while len(room_options) > 0 and not found_exit:  # Will test all options in a room. Change for dead ends up.
                choice = random.choice(room_options)
                room_options.remove(choice)
                # index 0 takes you south, 1 -> east, 2 -> North, 3 -> West from choices.
                inputs = (("south", "north", 1, 0), ("east", "west", 0, 1), ("north", "south", -1, 0),
                          ("west", "east", 0, -1))[choice]
                next_row, next_col = inputs[2] + row, inputs[3] + col  # Coordinates for next room.
                if self.__is_traversable(next_row, next_col):  # Checks if next room is traversable.
                    room.set_door(inputs[0], True)  # Opens up door to next room.
                    self.__dungeon[next_row][next_col].set_door(inputs[1], True)  # Updates next room's doors.
                    found_exit = self.__build_dungeon_path(next_row, next_col)  # Recurse and explore some more!
        return found_exit  # Explored all options.  Back we go.

    def __build_pillars(self):
        """
        Adds pillars to empty rooms along the traversable path of the dungeon.
        :return: None
        """
        pillars = self.__pillars.copy()  # Makes a copy of the pillars since we're going to pop 'em and drop 'em
        empty_rooms = self.__empty_rooms.copy()  # See above.  Pop 'em and drop 'em.
        while pillars:
            current = random.choice(empty_rooms)  # Assumes rooms already entered in semi-random order due to generation
            empty_rooms.remove(current)  # Suspicion is this isn't properly removing the room.
            room = self.__get_room(current)  # Uses coordinates to access room
            room.contents = pillars.pop()  # Sets the pillar to the current room.

    def __is_traversable(self, row, col):
        """
        Verifies location is a valid room for entry.  Helper function for traversal.
        :param row: int between 0 and row_count
        :param col: int between 0 and col_count
        :return: boolean, true if untraversed valid room, false if not.
        """
        return (0 <= row < self.__row_count) and (0 <= col < self.__col_count) and self.__dungeon[row][col].can_enter()

    def __is_valid_room(self, row: int, col: int):
        """
        Checks if room is valid (if the rows and columns are within the range of the 2D list)
        :param row: int
        :param col: int
        :return: True if row and col are both within the grid, else false.
        """
        return (0 <= row < self.__row_count) and (0 <= col < self.__col_count)

    def __get_room(self, coordinates):
        """
        Given a row and column, returns the room at those coordinates
        :param coordinates: list of int, 0 through __row_count-1, 0 through __col_count-1
        :return: room at coordinates
        """
        row, col = coordinates[0], coordinates[1]
        if self.__is_valid_room(row, col):
            return self.__dungeon[row][col]
        else:
            raise ValueError("Coordinates must be a tuple of ints x and y within the range of the dungeon.")

    def get_dungeon(self):
        """
        Returns dungeon and resets to no longer store it.
        :return: Dungeon
        """
        if self.__complete_dungeon:
            complete_dungeon = self.__complete_dungeon
            self.__reset()
            return complete_dungeon
        else:
            raise ValueError("Dungeon is currently empty.  Please build it first.")

    def build_dungeon(self, difficulty="easy", varied=True):
        """
        Main logic for building a maze.
        :return: Dungeon
        """
        self.__reset(difficulty, varied)
        reach_exit = False
        pillar_options = 0
        num_pillars = len(self.__pillars) * 2  # Dungeons with only the pillars will not be generated.
        ent_row = ent_col = exit_row = exit_col = None
        while (not reach_exit) or (pillar_options < num_pillars):  # If can't traverse or spots for pillars, resets.
            self.__empty_rooms = []  # Storage reset if previous generation failed.
            self.__build_2d_room_maze()  # Builds the 2d maze full of random rooms with varied interest.
            # Sets a random location for the exit and entrance.
            ent_row, ent_col = self.__get_rand_coords()
            exit_row, exit_col = self.__get_rand_coords()
            self.__dungeon[ent_row][ent_col].entrance = True  # Clears all items then sets contents to i
            self.__dungeon[exit_row][exit_col].exit = True  # Clears all items then sets contents to O
            reach_exit = self.__build_dungeon_path(ent_row, ent_col)  # Checks if can go from exit to entrance
            pillar_options = len(self.__empty_rooms)  # Verify we have enough empty rooms to put pillars in.
        self.__entrance = (ent_row, ent_col)
        self.__exit = (exit_row, exit_col)
        self.__build_pillars()
        self.__set_dungeon()  # Officially builds the dungeon.
        return self.__complete_dungeon
