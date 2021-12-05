"""
Steph's Time Tracker~!
10 hours to working properly with no error checking or fun.
"""

import random
from collections.abc import Iterable, Iterator
from room_factory import RoomFactory


class Dungeon(Iterable):
    class DungeonIterator(Iterator):
        def __init__(self, dungeon: list, row: int, col: int, row_count: int, col_count: int, access_only=False):
            self.__collection = dungeon
            self.__access_only = access_only
            self.__position = row * col_count + col
            self.__row = row
            self.__col = col
            self.__row_count = row_count
            self.__col_count = col_count

        def __next__(self):
            try:
                current_room = self.__collection[self.__row][self.__col]
                self.__increment()
            except IndexError:
                raise StopIteration()
            return current_room

        def __increment(self):
            if not self.__access_only:
                self.__col += 1
                if self.__col >= self.__col_count:
                    self.__col = 0
                    self.__row += 1

    def __init__(self, row_count=5, col_count=5, pillars=["A", "P", "I", "E"], hp_pot_chance=0.1,
                 vision_chance=0.05, many_chance=0.05, pit_chance=0.1):
        """
        Welcome to the dungeon!  Allows for hardcoded difficulty to be adjusted in the event we want to add different
        difficulty settings as an extra credit feature (ex. increase pit chance and damage)
        :param row_count: int between 0 and stack overflow
        :param col_count: int between 0 and stack overflow
        :param pillars: list of strings, though current room coding will error if not A P I E due to hardcoding.
        """
        if len(pillars) + 2 < (row_count * col_count * (pit_chance + hp_pot_chance + vision_chance +
                               many_chance)):  # If not, very unlikely maze will successfully generate
            self.__dungeon = []
            self.__row_count = row_count
            self.__col_count = col_count
            self.__empty_rooms = []  # Stores list of empty rooms to be used later for pillar placement
            self.__pillars = pillars  # To be popped into rooms
            self.__entrance = None  # Will be stored as a row, col tuple at maze building.
            self.__exit = None  # Will be stored as a row, col tuple when building maze.
            self.__build_maze()  # Sets entrance and exit.
            self.__add_pillars()
            self.__adventurer_loc = self.__entrance
        else:
            raise ValueError("row_count * col_count * (impassable_chance + pit_chance + hp_pot_chance + vision_chance"
                             " + many_chance) must be greater than len(pillars) + 2.")

    def __str__(self):
        string = string_top = string_middle = string_bottom = ""
        for row in range(0, self.__row_count):
            for col in range(0, self.__col_count):
                room = self.__dungeon[row][col]
                string_top += room.string_top()
                string_middle += room.string_middle()
                string_bottom += room.string_bottom()
            string += string_top + "\n" + string_middle + "\n" + string_bottom + "\n"
            string_top = string_middle = string_bottom = ""
        return string

    def __iter__(self):
        return self.DungeonIterator(self.__dungeon, 0, 0, self.__row_count, self.__col_count)

    def __create_2d_room_maze(self):
        """

        :return: None
        """
        rf = RoomFactory()
        for row in range(0, self.__row_count):
            self.__dungeon.append([])
            for col in range(0, self.__col_count):
                self.__dungeon[row].append([])
                new_room = rf.create_room(self.__row_count * self.__col_count)
                self.__dungeon[row][col] = new_room

    def __add_pillars(self):
        pillars = self.__pillars.copy()
        empty_rooms = self.__empty_rooms.copy()
        while pillars:
            current = random.choice(empty_rooms)  # Assumes rooms already entered in semi-random order due to generation
            empty_rooms.remove(current)  # Suspicion is this isn't properly removing the room.
            room = self.get_room(current)
            room.contents = pillars.pop()
        self.__empty_rooms = empty_rooms.copy()

    def __build_maze(self):
        """
        Builds the maze.  Sets member entrance and exit to tuple coordinates.  Creates list of
        :return: None
        """
        reach_exit = False
        pillar_options = 0
        num_pillars = len(self.__pillars) * 2  # Dungeons with only the pillars will not be generated.
        ent_row = ent_col = exit_row = exit_col = None
        while (not reach_exit) or (pillar_options < num_pillars):  # If can't traverse or spots for pillars, resets.
            self.__empty_rooms = []  # Storage
            self.__create_2d_room_maze()  # Builds the 2d maze full of random rooms with varied interest.
            ent_row, ent_col = random.randint(0, self.__row_count-1), random.randint(0, self.__col_count-1)
            exit_row, exit_col = random.randint(0, self.__row_count-1), random.randint(0, self.__col_count-1)
            self.__dungeon[ent_row][ent_col].entrance = True  # Clears all items then sets contents to i
            self.__dungeon[exit_row][exit_col].exit = True  # Clears all items then sets contents to O
            reach_exit = self.__traverse(ent_row, ent_col)  # Checks if can go from exit to entrance
            pillar_options = len(self.__empty_rooms)
        self.__entrance = (ent_row, ent_col)
        self.__exit = (exit_row, exit_col)

    # initial call if you know entrance is 0,0 would be traverse(0, 0)
    def __traverse(self, row, col):
        found_exit = False
        if self.__is_valid_room(row, col):
            room = self.__dungeon[row][col]
            if room.is_empty and self.__empty_rooms.count((row, col)) == 0:
                self.__empty_rooms.append((row, col))  # Places to put pillars later
            elif room.exit:  # Check for exit - assume more rooms empty than exit, so checks fewer.
                return True
            # not at exit so try another room:
            else:
                room_options = [0, 1, 2, 3]
                while len(room_options) > 0 and not found_exit:  # Will test all options in a room.
                    choice = random.choice(room_options)
                    room_options.remove(choice)
                    # index 0 takes you south, 1 -> east, 2 -> North, 3 -> West from choices.
                    inputs = (("south", "north", 1, 0), ("east", "west", 0, 1), ("north", "south", -1, 0),
                              ("west", "east", 0, -1))[choice]
                    next_row, next_col = inputs[2] + row, inputs[3] + col
                    if self.__is_traversable(next_row, next_col):
                        room.set_door(inputs[0], True)
                        self.__dungeon[next_row][next_col].set_door(inputs[1], True)  # next room
                        found_exit = self.__traverse(next_row, next_col)
        return found_exit

    def __is_traversable(self, row, col):
        """
        Verifies location is a valid room for entry.  Helper function for traversal.
        :param row: int between 0 and row_count
        :param col: int between 0 and col_count
        :return: boolean, true if untraversed valid room, false if not.
        """
        return (0 <= row < self.__row_count) and (0 <= col < self.__col_count) and self.__dungeon[row][col].can_enter()

    def __is_valid_room(self, row, col):
        return (0 <= row < self.__row_count) and (0 <= col < self.__col_count)

    def set_health_potion(self, row, col, num):
        """
        Sets the health potion quantity in a specific room to a specific value, such as setting to 0 when an adventurer
        collects the health potions.
        :param row: int to identify target row
        :param col: int to identify target column
        :param num: int to change the current health potions in a room to
        :return:
        """
        self.__dungeon[row][col].health_potion = num

    def set_vision_potion(self, row, col, num):
        """
        Sets the vision potion quantity in a specific room to a specific value, such as 0 after collecting.
        :param row: int to identify target row
        :param col: int to identify target column
        :param num: int to change the current vision potions in a room to
        :return:
        """
        self.__dungeon[row][col].vision_potion = num

    def get_room(self, coordinates):
        """
        Given a row and column, returns the room at those coordinates
        :param coordinates: list of int, 0 through __row_count-1, 0 through __col_count-1
        :return: room at coordinates
        """
        row = coordinates[0]
        col = coordinates[1]
        if self.__is_valid_room(row, col):
            return self.__dungeon[row][col]
        else:
            raise ValueError("Coordinates must be a tuple of ints x and y within the range of the dungeon.")

    @property
    def entrance(self):
        return self.__entrance

    @property
    def pillars(self):
        return self.__pillars

    @property
    def dungeon(self):
        return self.__dungeon

    def move_adventurer(self, direction: str):
        current_room = self.__dungeon[self.__adventurer_loc[0]][self.__adventurer_loc[1]]
        if current_room.door(direction):
            coord_dict = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}
            adjust_coords = coord_dict[direction]
            new_row = self.__adventurer_loc[0] + adjust_coords[0]
            new_col = self.__adventurer_loc[1] + adjust_coords[1]
        else:
            raise ValueError("Value must be north, east, south, or west, and there must be a door in that direction.")
        if self.__is_valid_room(new_row, new_col):
            self.__adventurer_loc = (new_row, new_col)
            return self.get_room(new_row, new_col)
        else:
            raise ValueError("There's no room that way!  Check the map!")
