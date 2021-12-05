"""
Steph's portion~!
Time tracker: 5 hours (with tests & dungeon algorithm )
"""


class Room:
    def __init__(self, health_potion=0, vision_potion=0, pit=0, contents=" "):
        """
        Creates a room with passed in parameters.  Defaults provided, so only values need to be provided if not the
        default.  Ex. new_room = Room(vision_potion=1, pit=10, north_door=True) should be valid.
        :param health_potion: integer value 0 or higher representing potions to be found in room
        :param vision_potion: integer value 0 or higher representing potions to be found in room
        :param pit: integer value 0 or higher representing damage dealt upon entry
        """
        if self.__is_valid_creation_data(health_potion, vision_potion, pit, contents):
            self.__health_potion = health_potion
            self.__vision_potion = vision_potion
            self.__doors = {"north": False, "east": False, "south": False, "west": False}
            self.__pit = pit
            self.__contents = contents
        else:
            raise Exception("Value or TypeErrors should have been raised and they weren't.  Sound the alarm!")

    def __str__(self):
        """
        Converts room to string representation.  I'm really proud of my tuple boolean accessors.
        :return: string
        """
        string = ""
        string += self.string_top() + "\n"  # Appends *** if not north_door, *-* if north door
        string += self.string_middle() + "\n"  # Gets the middle of the string and adds a new line for individual room.
        string += self.string_bottom() + "\n"
        return string

    def __eq__(self, other):
        """
        For testing purposes.  Compares the strings of the two rooms.
        :param other: another room
        :return: bool, True if the strings match, false if they don't.
        """
        return f"{self}" == f"{other}"

    @staticmethod
    def __is_number_gt_eq_0(num):
        """
        Verifies num is an integer and greater than or equal to 0.
        :param num: integer greater than or eq to 0
        :return: True if it is, raises error otherwise
        :raise: TypeError if not an integer
        :raise: ValueError if less than 0
        """
        if type(num) is not int:
            raise TypeError("You must provide an integer greater than or equal to 0")
        elif num < 0:
            raise ValueError("You must provide an integer greater than or equal to 0.")
        else:
            return True

    @staticmethod
    def __is_boolean(boolean):
        """
        Verifies boolean type is bool.  Raises error if not.  Helper function for creation validation.
        :param boolean: expected to be a bool
        :return: True if bool
        :raises: TypeError if boolean is not bool
        """
        if type(boolean) is not bool:
            raise TypeError("You must provide a boolean.")
        return True

    @staticmethod
    def __is_valid_contents(contents):
        """
        Verifies if pillar is valid (a string of values "", "A", "P", "I", "E")
        :param contents: string
        :return: Bool
        :raises: TypeError if contents is not a string
        :raises: ValueError if contents is not empty or not A P I E (delicious <3) or
                 "i", "O", "*", "H", "V", "X", "M", " "
        """
        valid_choices = [" ", "A", "P", "I", "E", "i", "O", "*", "H", "V", "X", "M"]
        if type(contents) is not str:
            raise TypeError('You must provide a string " ", "A", "P", "I", "E", "i", "O", "*", "H", "V", "X", "M"')
        else:
            try:
                valid_choices.index(contents)
                return True
            except ValueError:
                print(f'{ValueError} Contents must be " ", "A", "P", "I", "E", "i", "O", "*", "H", "V", "X", "M"')

    def __is_valid_creation_data(self, health_potion: int, vision_potion: int, pit: int, contents: str) -> bool:
        """
        Validates all data passed in to create a room is valid for safe creation.
        :param health_potion: int
        :return: True if all data is valid, raises an error in helper functions if not
        """
        data = (health_potion, vision_potion, pit)
        valid_nums = False
        for index in range(0, 3):
            valid_nums = self.__is_number_gt_eq_0(data[index])  # Will error and not finish if not True
        valid_contents = self.__is_valid_contents(contents)
        return valid_nums and valid_contents

    def string_top(self):
        return ("*  *  *", "*  -  *")[self.__doors["north"]]  # Appends *** if not north_door, *-* if north door

    def string_middle(self):
        string = ""
        string += ("*  ", "|  ")[self.__doors["west"]]  # Appends * if not west_door, | if west_door
        string += self.__contents
        string += ("  *", "  |")[self.__doors["east"]]  # Appends | if east_door and * if not east_door.
        return string

    def string_bottom(self):
        return ("*  *  *", "*  -  *")[self.__doors["south"]]

    def can_enter(self):
        """
        Returns True if can enter.  Not impassable and not visited.
        :return: bool
        """
        return self.__contents != "*" and not self.visited

    def clear_room(self):
        """
        Clears all settings in a room back to nothing.  Not visited, not impassable, no potions, not pits.
        :return:
        """
        self.__health_potion = 0
        self.__vision_potion = 0
        self.__contents = " "
        self.__pit = 0

    @property
    def exit(self):
        """
        Returns if room is the exit.
        :return: bool True if it is, False if it isn't.
        """
        return self.__contents == "O"

    @exit.setter
    def exit(self, is_exit: bool):
        """
        Sets exit to a new boolean provided.
        :param is_exit: bool, True if changing the room to being the exit, False if not
        """
        if self.__is_boolean(is_exit) and is_exit:
            self.clear_room()
            self.__contents = "O"
        elif not is_exit:
            self.__contents = " "

    @property
    def entrance(self):
        return self.__contents == "i"

    @entrance.setter
    def entrance(self, is_entrance: bool):
        """
        Sets whether or not the room is an entrance or not.
        :param is_entrance: bool of whether or not the room is to be set as the entrance
        """
        if self.__is_boolean(is_entrance) and is_entrance:
            self.clear_room()
            self.__contents = "i"
        elif not is_entrance:
            self.__contents = " "

    @property
    def health_potion(self):
        return self.__health_potion

    @health_potion.setter
    def health_potion(self, num_pots):
        """
        Sets health_potion quantity in room to a specific number.
        :param num_pots: integer >= 0
        """
        if self.__is_number_gt_eq_0(num_pots):
            self.__health_potion = num_pots

    @property
    def vision_potion(self):
        return self.__vision_potion

    @vision_potion.setter
    def vision_potion(self, num_pots):
        """
        Sets vision_potion quantity in room to a specific number.
        :param num_pots: integer >= 0
        """
        if self.__is_number_gt_eq_0(num_pots):
            self.__vision_potion = num_pots

    @property
    def pit_damage(self):
        return self.__pit

    @property
    def north_door(self):
        return self.__doors["north"]

    @north_door.setter
    def north_door(self, door_exists):
        if self.__is_boolean(door_exists):
            self.__doors["north"] = door_exists

    @property
    def east_door(self):
        return self.__doors["east"]

    @east_door.setter
    def east_door(self, door_exists):
        if self.__is_boolean(door_exists):
            self.__doors["east"] = door_exists

    @property
    def south_door(self):
        return self.__doors["south"]

    @south_door.setter
    def south_door(self, door_exists):
        if self.__is_boolean(door_exists):
            self.__doors["south"] = door_exists

    @property
    def west_door(self):
        return self.__doors["west"]

    @west_door.setter
    def west_door(self, door_exists):
        if self.__is_boolean(door_exists):
            self.__doors["west"] = door_exists

    @property
    def is_empty(self):
        return self.__contents == " "

    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, data: str):
        self.__contents = data

    @property
    def visited(self):
        return self.__doors["north"] or self.__doors["east"] or self.__doors["south"] or self.__doors["west"]
