"""
Steph's portion~!
Time tracker: 4 hours (with tests & dungeon algorithm )
"""


class Room:
    def __init__(self, health_potion=0, vision_potion=0, pit=0, pillar="", north_door=False, east_door=False,
                 south_door=False, west_door=False, is_exit=False, entrance=False, impassable=False, visited=False):
        """
        Creates a room with passed in parameters.  Defaults provided, so only values need to be provided if not the
        default.  Ex. new_room = Room(vision_potion=1, pit=10, north_door=True) should be valid.
        :param health_potion: integer value 0 or higher representing potions to be found in room
        :param vision_potion: integer value 0 or higher representing potions to be found in room
        :param pit: integer value 0 or higher representing damage dealt upon entry
        :param pillar: string representing APIE pillar or...none at all.
        :param north_door: bool, True means you can go to another room that way, False means no entrada.
        :param east_door: bool, see above
        :param south_door: bool, see above
        :param west_door: bool, see above
        :param is_exit: bool, True if it is the exit to the dungeon.
        :param entrance: bool, True if it is the entrance to the dungeon.
        :param impassable: bool, True if impassable with current dungeon layout.  Used for dungeon building.
        :param visited: bool, True if visited.  Used to know where dungeon building built.
        """
        data = (health_potion, vision_potion, pit, pillar, north_door, east_door, south_door, west_door,
                is_exit, entrance, impassable, visited)  # validation is dependent on tuple being in correct-ish order.
        if self.__is_valid_creation_data(data):
            self.__health_potion = health_potion
            self.__vision_potion = vision_potion
            self.__north_door = north_door
            self.__east_door = east_door
            self.__south_door = south_door
            self.__west_door = west_door
            self.__pillar = pillar
            self.__pit = pit
            self.__exit = is_exit
            self.__entrance = entrance
            self.__impassable = impassable
            self.__visited = visited
        else:
            raise Exception("Value or TypeErrors should have been raised and they weren't.  Sound the alarm!")

    def __str__(self):
        """
        Converts room to string representation.  I'm really proud of my tuple boolean accessors.  Divine inspiration.
        Paladins would be proud.  We agreed you should be able to find health potions and vision potions in the pit.
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
        :param other:
        :return:
        """

    def string_top(self):
        return ("*  *  *", "*  -  *")[self.__north_door]  # Appends *** if not north_door, *-* if north door

    def string_middle(self):
        string = ""
        string += ("*  ", "|  ")[self.__west_door]  # Appends * if not west_door, | if west_door
        if self.__pillar:
            string += self.__pillar
        elif self.__entrance:
            string += "i"  # It's the entrance!
        elif self.__exit:
            string += "O"  # It's the exit!
        elif int(self.__pit > 0) + int(self.__health_potion) + int(self.__vision_potion) >= 2:  # if 2 / 3 are true
            string += "M"  # There be potions in this pit!  Or lots of potions in a treasure chest.
        elif self.__pit:
            string += "X"  # Death awaits ye!
        elif self.__health_potion:
            string += "H"  # Get healthy!
        elif self.__vision_potion:
            string += "V"  # See the world from the comfort of your own home!  JK it's a laptop.
        elif self.__impassable:
            string += "*"  # More rocks here!  Not for human entrance.
        else:
            string += " "
        string += ("  *", "  |")[self.__east_door]  # Appends | if east_door and * if not east_door.
        return string

    def string_bottom(self):
        return ("*  *  *", "*  -  *")[self.__south_door]

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
    def __is_valid_pillar(pillar):
        """
        Verifies if pillar is valid (a string of values "", "A", "P", "I", "E")
        :param pillar: string
        :return: Bool
        :raises: TypeError if pillar is not a string
        :raises: ValueError if pillar is not empty or not A P I E (delicious <3)
        """
        valid_choices = ("", "A", "P", "I", "E")
        if type(pillar) is not str:
            raise TypeError("You must provide a string for the pillar as A P I E or empty")
        else:
            for valid in valid_choices:
                if pillar == valid:
                    return True
            raise ValueError("Pillar must be empty or A P I E")

    def __is_valid_creation_data(self, data):
        """
        Validates all data passed in to create a room is valid for safe creation.
        :param data: tuple of data in this order:
            0 through 3: health_potion, vision_potion, pit - (checks all integers greater than 0)
            4: pillar - string that's either empty ("") or "A" "P" "I" "E"
            5 through 12: north_door, east_door, south_door, west_door, is_exit, entrance, impassable, visited - bool
        :return: True if all data is valid, raises an error in helper functions if not
        """
        valid_nums = valid_rooms = False
        for index in range(0, 3):
            valid_nums = self.__is_number_gt_eq_0(data[index])  # Will error and not finish if not True
        valid_pillar = self.__is_valid_pillar(data[3])
        for index in range(4, len(data)):
            valid_rooms = self.__is_boolean(data[index])
        return valid_nums and valid_pillar and valid_rooms

    def can_enter(self):
        """
        Returns True if can enter.  Not impassable and traversing algorithm hasn't explored it yet.
        :return: bool
        """
        return not self.__impassable and not self.__visited

    def clear_room(self):
        """
        Clears all settings in a room back to nothing.  Not visited, not impassable, no potions, not pits.
        :return:
        """
        self.__health_potion = 0
        self.__vision_potion = 0
        self.__pillar = ""
        self.__pit = 0
        self.__exit = False
        self.__entrance = False
        self.__impassable = False
        self.__visited = False

    @property
    def exit(self):
        """
        Returns if room is the exit.
        :return: bool True if it is, False if it isn't.
        """
        return self.__exit

    @exit.setter
    def exit(self, is_exit):
        """
        Sets exit to a new boolean provided.
        :param is_exit: bool, True if changing the room to being the exit, False if not
        """
        if self.__is_boolean(is_exit):
            self.__exit = is_exit

    @property
    def visited(self):
        return self.__visited

    @visited.setter
    def visited(self, visited):
        """
        Sets visited to a new boolean provided.
        :param visited: bool, True if changing the room to being visited, False if not
        """
        if self.__is_boolean(visited):
            self.__visited = visited

    @property
    def entrance(self):
        return self.__entrance

    @entrance.setter
    def entrance(self, is_entrance):
        """
        Sets whether or not the room is an entrance or not.
        :param is_entrance: bool of whether or not the room is to be set as the entrance
        """
        if self.__is_boolean(is_entrance):
            self.__entrance = is_entrance

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
        return self.__north_door

    @north_door.setter
    def north_door(self, door_exists):
        if self.__is_boolean(door_exists):
            self.__north_door = door_exists

    @property
    def east_door(self):
        return self.__east_door

    @east_door.setter
    def east_door(self, door_exists):
        if self.__is_boolean(door_exists):
            self.__east_door = door_exists

    @property
    def south_door(self):
        return self.__south_door

    @south_door.setter
    def south_door(self, door_exists):
        if self.__is_boolean(door_exists):
            self.__south_door = door_exists

    @property
    def west_door(self):
        return self.__west_door

    @west_door.setter
    def west_door(self, door_exists):
        if self.__is_boolean(door_exists):
            self.__west_door = door_exists

    @property
    def pillar(self):
        return self.__pillar

    @pillar.setter
    def pillar(self, current_pillar):
        if self.__is_valid_pillar(current_pillar):
            self.__pillar = current_pillar
