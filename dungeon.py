"""
Time Tracker~!
17 hours
"""

from collections.abc import Iterable, Iterator


class Dungeon(Iterable):
    class DungeonIterator(Iterator):
        """
        Iterates through dungeon.  Returns every room, whether accessible or not.
        """
        def __init__(self, dungeon: list, col_count: int):
            self.__collection = dungeon
            self.__row = 0
            self.__col = 0
            self.__col_count = col_count

        def __next__(self):
            """
            Checks if has next room, stops iteration if not.  Else returns room.
            :return:
            """
            try:
                current_room = self.__collection[self.__row][self.__col]
                self.__col += 1
                if self.__col >= self.__col_count:
                    self.__col = 0
                    self.__row += 1
            except IndexError:
                raise StopIteration()
            return current_room

    def __init__(self, dungeon=[], difficulty="easy", ent=(0, 0), ex=(3, 3)):
        """
        Welcome to the dungeon!  Allows for hardcoded difficulty to be adjusted in the event we want to add different
        difficulty settings as an extra credit feature (ex. increase pit chance and damage)
        :param row_count: int between 0 and stack overflow
        :param col_count: int between 0 and stack overflow
        :param pillars: list of strings, though current room coding will error if not A P I E due to hardcoding.
        """
        pillars = ["A", "P", "I", "E"]
        diff_index = {"easy": 0, "medium": 1, "hard": 2, "inhumane": 3}
        if diff_index.get(difficulty) >= 0:
            self.__diff_index = diff_index[difficulty]
            self.__row_count = (5, 8, 10, 20)[self.__diff_index]
            self.__col_count = (5, 8, 10, 20)[self.__diff_index]
            self.__dungeon = dungeon  # Created from dungeon_builder
            self.__pillars = pillars  # To be popped into rooms, currently hard-coded.
            self.__entrance = ent  # Will be stored as a row, col tuple at maze building.
            self.__exit = ex  # Will be stored as a row, col tuple when building maze.
            self.__adventurer_loc = self.__entrance  # Adventurer starts at the entrance.

        else:
            raise ValueError("row_count * col_count * (impassable_chance + pit_chance + hp_pot_chance + vision_chance"
                             " + many_chance) must be greater than len(pillars) + 2.")

    def __str__(self):
        """
        Builds string representing all rooms in the dungeon.
        [" ", "A", "P", "I", "E", "i", "O", "*", "H", "V", "X", "M"] are contents of room matching directions.
        M can be pit and potions or just multiple potions.
        :return: string
        """
        string = string_top = string_middle = string_bottom = ""
        for row in range(0, self.__row_count):
            for col in range(0, self.__col_count):
                room = self.__dungeon[row][col]
                string_top += room.string_top()
                string_middle += room.string_middle()
                string_bottom += room.string_bottom()
            string += string_top + "\n" + string_middle + "\n" + string_bottom + "\n"  # New lines at the end of row.
            string_top = string_middle = string_bottom = ""  # Reset strings for building next row.
        return string

    def __iter__(self):
        """
        Iterates through dungeon collection, visiting every portion of the dungeon.
        :return: DungeonIterator
        """
        return self.DungeonIterator(self.__dungeon, self.__col_count)

    def __eq__(self, other):
        """
        Dungeons are equal if their strings are identical.  Used for testing.
        :param other: Another dungeon.
        :return: True if dungeons strings are identical.  False if not.
        """
        return self.__str__() == other.__str__()

    def __is_valid_room(self, row: int, col: int):
        """
        Checks if room is valid (if the rows and columns are within the range of the 2D list)
        :param row: int
        :param col: int
        :return: True if row and col are both within the grid, else false.
        """
        return (0 <= row < self.__row_count) and (0 <= col < self.__col_count)

    def get_room(self, coordinates):
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

    @property
    def entrance(self):
        """
        Gets coordinates of entrance as a tuple of ints.  Ex. (0, 0)
        :return: tuple pair of ints
        """
        return self.__entrance

    @property
    def exit(self):
        """
        Gets coordinates of exit as tuple of ints.  Ex. (0, 0)
        :return: tuple pair of ints.
        """
        return self.__exit

    @property
    def pillars(self):
        """
        Returns list of strings of all pillars within dungeon.
        :return: list of strings
        """
        return self.__pillars

    @property
    def dungeon(self):
        """
        Returns two dimensional python list representing the entire dungeon.  Each coordinate contains a room.
        :return: dungeon as two dimensional list.
        """
        return self.__dungeon

    @property
    def adventurer_loc(self):
        """
        Getter for adventurer's current location as a tuple of ints, row, col (x, y).
        :return: tuple of ints
        """
        return self.__adventurer_loc

    @property
    def pit_damage(self):
        """
        Gets pit damage adventurer should receive in their current room.
        :return: int of damage
        """
        room = self.get_room(self.__adventurer_loc)
        return room.pit_damage

    def move_adventurer(self, direction: str):
        """
        Moves the adventurer in the indicated direction as long as they are able.
        :param direction: str either "north", "east", "west", or "south"
        :return:
        """
        current_room = self.__dungeon[self.__adventurer_loc[0]][self.__adventurer_loc[1]]
        if current_room.get_door(direction):
            coord_dict = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}
            adjust_coords = coord_dict[direction]
            new_row, new_col = self.__adventurer_loc[0] + adjust_coords[0], self.__adventurer_loc[1] + adjust_coords[1]
        else:
            raise ValueError("Value must be north, east, south, or west, and there must be a door in that direction.")
        if self.__is_valid_room(new_row, new_col):
            self.__adventurer_loc = (new_row, new_col)
            new_room = self.get_room((new_row, new_col))
            return new_room
        else:
            raise ValueError("There's no room that way!  Check the map!")

    def collect_potions(self):
        """
        Collections all potions in adventurer's location.  Returns as tuple of ints, HP then vision.
        :return: tuple of ints, HP then vision.
        """
        room = self.get_room(self.__adventurer_loc)
        pots = (room.health_potion, room.vision_potion)
        room.health_potion = 0
        room.vision_potion = 0
        return pots

    def collect_pillars(self):
        """
        Removes pillar from the room and returns it if a pillar exists in the room.
        :return: str pillar, else None
        """
        room = self.get_room(self.__adventurer_loc)
        pillar = None
        if self.__pillars.count(room.contents) > 0:
            pillar = room.contents
            room.contents = " "  # Since rooms with pillars are otherwise empty, no other updating necessary.
        return pillar
