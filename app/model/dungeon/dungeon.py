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

    def __init__(self, dungeon_dict: dict):
        """
        Welcome to the dungeon!  Allows for hardcoded difficulty to be adjusted in the event we want to add different
        difficulty settings as an extra credit feature (ex. increase pit chance and damage)
        :param dungeon: list of lists containing room objects.  Init empty if not built through dungeon builder.
        :param difficulty: difficulty index for challenge level as string "easy", "medium", "hard", "inhumane"
        :param ent: tuple of ints indicating coordinates in matrix for entrance (row, column)
        :param ex: tuple of ints indicating coordinates in matrix for exit (row, column)
        """
        if not dungeon_dict:
            self.__dungeon_dict = None
        else:
            keys = {"dungeon", "difficulty", "rows", "cols", "pillars", "entrance", "exit",
                        "adventurer_location"}
            for key in keys:
                if key not in dungeon_dict:
                    assert KeyError(f"{key} is missing from dungeon dictionary.")
            self.__dungeon_dict = dungeon_dict

    def __str__(self):
        """
        Builds string representing all rooms in the dungeon.
        [" ", "A", "P", "I", "E", "i", "O", "*", "H", "V", "X", "M"] are contents of room matching directions.
        M can be pit and potions or just multiple potions.
        :return: string
        """
        return self.get_visible_dungeon_string()  # When feeding none, automatically prints whole maze

    def __iter__(self):
        """
        Iterates through dungeon collection, visiting every portion of the dungeon.
        :return: DungeonIterator
        """
        return self.DungeonIterator(self.dungeon_dict["dungeon"], self.dungeon_dict["cols"])

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
        return (0 <= row < self.dungeon_dict["rows"]) and (0 <= col < self.dungeon_dict["cols"])

    def get_room(self, coordinates):
        """
        Given a row and column, returns the room at those coordinates
        :param coordinates: list of int, 0 through total_rows-1, 0 through total_columns-1
        :return: room at coordinates
        """
        row, col = coordinates[0], coordinates[1]
        if self.__is_valid_room(row, col):
            return self.dungeon[row][col]
        else:
            raise ValueError(f"Coordinates must be tuple of ints.  Max row: {self.total_rows}, "
                             f"max col: {self.total_columns}.")

    @property
    def total_rows(self):
        """
        Returns total number of rows as an int.  Returns none if dungeon not built through dungeon builder.
        :return: int
        """
        return self.dungeon_dict["rows"]

    @property
    def total_columns(self):
        """
        Returns total number of columns as an int.  Returns none if dungeon not built through dungeon builder.
        :return: int
        """
        return self.dungeon_dict["cols"]

    @property
    def entrance(self):
        """
        Gets coordinates of entrance as a tuple of ints.  Ex. (0, 0)  Returns none if dungeon not built through
        dungeon builder.
        :return: tuple pair of ints
        """
        return self.dungeon_dict["entrance"]

    @property
    def exit(self):
        """
        Gets coordinates of exit as tuple of ints.  Ex. (0, 0) Returns none if dungeon not built through dungeon builder
        :return: tuple pair of ints.
        """
        return self.dungeon_dict["exit"]

    @property
    def pillars(self):
        """
        Returns list of strings of all pillars within dungeon.
        :return: list of strings
        """
        return self.dungeon_dict["pillars"]

    @property
    def dungeon(self):
        """
        Returns two dimensional python list representing the entire dungeon.  Each coordinate contains a room.
        :return: dungeon as two dimensional list.
        """
        return self.dungeon_dict["dungeon"]

    @property
    def adventurer_loc(self):
        """
        Getter for adventurer's current location as a tuple of ints, row, col (x, y).
        :return: tuple of ints
        """
        return self.dungeon_dict["adventurer_location"]

    @adventurer_loc.setter
    def adventurer_loc(self, coords):
        self.__dungeon_dict["adventurer_location"] = coords

    @property
    def monster(self):
        """
        Gets monster if one is in the room with adventurer.
        :return: Monster.  None if no monster in the room with adventurer.
        """
        room = self.get_room(self.adventurer_loc)
        return room.monster

    def move_adventurer(self, direction: str):
        """
        Moves the adventurer in the indicated direction as long as they are able.
        :param direction: str either "north", "east", "west", or "south"
        :return:
        """
        current_room = self.dungeon[self.adventurer_loc[0]][self.adventurer_loc[1]]
        if current_room.get_door(direction):
            coord_dict = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}
            adjust_coords = coord_dict[direction]
            new_row, new_col = self.adventurer_loc[0] + adjust_coords[0], self.adventurer_loc[1] + adjust_coords[1]
        else:
            raise ValueError("Value must be north, east, south, or west, and there must be a door in that direction.")
        if self.__is_valid_room(new_row, new_col):
            self.adventurer_loc = (new_row, new_col)
            new_room = self.get_room((new_row, new_col))
            return new_room
        else:
            raise ValueError("There's no room that way!  Check the map!")

    def collect_potions(self):
        """
        Collections all potions in adventurer's location.  Returns as tuple of ints, HP then vision.
        :return: tuple of ints, HP then vision.
        """
        room = self.get_room(self.adventurer_loc)
        pots = (room.health_potion, room.vision_potion)
        if room.health_potion or room.vision_potion:
            room.health_potion = 0
            room.vision_potion = 0
        return pots

    def collect_pillars(self):
        """
        Removes pillar from the room and returns it if a pillar exists in the room.
        :return: str pillar, else None
        """
        room = self.get_room(self.adventurer_loc)
        pillar = None
        if self.pillars.count(room.contents) > 0:
            pillar = room.contents
            room.contents = " "  # Since rooms with pillars are otherwise empty, no other updating necessary.
        return pillar

    def get_visible_dungeon_string(self, bool_list=None):
        """
        Returns string of visible rooms.  Provide None for bool_list to return everything!  TODO error checking.
        :param bool_list: 2d list of boolean values for what is currently visible in the may. True if yes, False if no.
        :return: String of visible rooms.  If bool_list is None, returns the whole dungeon.
        """
        string = string_top = string_middle = string_bottom = ""
        for row in range(0, self.total_rows):
            for col in range(0, self.total_columns):
                if bool_list is None or bool_list[row][col]:  # If visible or no bool_list (for __str__ method)
                    room = self.dungeon[row][col]
                    string_top += room.string_top()
                    room_middle_string = room.string_middle()
                    if (row, col) == self.adventurer_loc:  # replaces middle to @ if adv loc.
                        room_middle_string = room_middle_string[:1] + "@" + room_middle_string[2:]
                    string_middle += room_middle_string

                    string_bottom += room.string_bottom()
                else:  # If not visible, prints nooooothingness instead.
                    empty = "       "
                    string_top += empty
                    string_middle += empty
                    string_bottom += empty
            string += string_top + "\n" + string_middle + "\n" + string_bottom + "\n"  # New lines at the end of row.
            string_top = string_middle = string_bottom = ""  # Reset strings for building next row.
        return string

    @property
    def dungeon_dict(self):
        return self.__dungeon_dict

    @property
    def json_dict(self):
        temp = self.__dungeon_dict.copy()
        room_array = []
        for row in range(self.dungeon_dict["rows"]):
            room_array.append([])
            for col in range(self.dungeon_dict["cols"]):
                room_array[row].append([])
                current_room = self.get_room((row, col))
                room_array[row][col] = current_room.json_dict()
        temp["dungeon"] = room_array
        return temp

