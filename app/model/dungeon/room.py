"""
WARNING: Pillars are currently hard-coded in string validation for contents.  To allow flexible pillars, we need
to modify this.

Contents key:
        " ": empty
        "A", "P", "I", "E": one of the pillars and an Ogre
        "i": in, entrance
        "O": out, exit
        "*": Impassable
        "H": HP potion
        "V": Vision potion
        "X": Monster
        "M": Multiple potions or a potion + a monster.
"""

from app.model.characters.monster import Monster


class Room:
    def __init__(self, health_potion=0, vision_potion=0, monster=None, contents=" ", room_dict=None):
        """
        Creates a room with passed in parameters.  Defaults provided, so only values need to be provided if not the
        default.  Ex. new_room = Room(vision_potion=1, monster = Monster, north_door=True) should be valid.
        :param health_potion: integer value 0 or higher representing potions to be found in room
        :param vision_potion: integer value 0 or higher representing potions to be found in room
        :param monster: Monster object or None, combat begins upon entry
        """
        if room_dict is None:
            if self.__is_valid_creation_data(health_potion, vision_potion, monster, contents):
                self.__room_dict = {"health": health_potion, "vision": vision_potion, "monster": monster,
                                   "north": False, "east": False, "south": False, "west": False,
                                    "contents": contents}
            else:
                raise Exception("Value or TypeErrors should have been raised and they weren't.  Sound the alarm!")
        else:
            keys = ("health", "vision", "monster", "north", "east", "south", "west", "contents")
            for key in keys:
                if key not in room_dict:
                    raise KeyError(f"Room dictionary is missing vital value {key}")
            self.__room_dict = room_dict

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

    def __repr__(self):
        """
        Representation of a room for debugging purposes.
        :return: str representing room.
        """

        rep = f"Health Potion: {self.room_dict['health']}, Vision Potion: {self.room_dict['vision']}, "
        rep += f"Monster: {self.monster.name}, " if self.monster is not None else f"Monster: None, "
        rep += f"Contents: {self.contents}, Doors: "
        keys = ["north", "east", "south", "west"]
        for key in keys:
            if self.room_dict[key] == True:
                rep += key
        return rep

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

    def __is_valid_creation_data(self, health_potion: int, vision_potion: int, monster, contents: str) -> bool:
        """
        Validates all data passed in to create a room is valid for safe creation.
        :param health_potion: int
        :return: True if all data is valid, raises an error in helper functions if not
        """
        data = (health_potion, vision_potion)
        valid_nums = False
        for index in range(0, len(data)):
            valid_nums = self.__is_number_gt_eq_0(data[index])  # Will error and not finish if not True
        valid_contents = self.__is_valid_contents(contents)
        return valid_nums and valid_contents

    def __update_room_contents(self):
        """
        Checks and updated the contents of the current room after a change has been made to potions.
        :return: Returns True if changed through this method.  Returns False if not so potions can be updated.
        """
        if self.contents in {"A", "P", "I", "E"}:
            return False
        elif bool(self.room_dict["vision"]) + bool(self.room_dict["health"]) + bool(self.room_dict["monster"]) >= 2:
            self.contents = "M"
            return True
        elif self.room_dict["monster"] and (not self.room_dict["vision"] and not self.room_dict["health"]):
            self.contents = "X"
            return True
        elif not self.room_dict["monster"] and not self.room_dict["vision"] and not self.room_dict["health"]:
            self.contents = " "
            return True
        else:
            return False

    def string_top(self):
        """
        Creates top portion of the room's string including doors.
        :return: string representing top of room.
        """
        return ("*  *  *", "*  -  *")[self.room_dict["north"]]  # Appends *** if not north_door, *-* if north door

    def string_middle(self):
        """
        Creates middle portion of the room's string including contents and doors east or west.
        :return: string representing middle and contents of room.
        """
        string = ""
        string += ("*  ", "|  ")[self.room_dict["west"]]  # Appends * if not west_door, | if west_door
        string += self.contents
        string += ("  *", "  |")[self.room_dict["east"]]  # Appends | if east_door and * if not east_door.
        return string

    def string_bottom(self):
        """
        Creates bottom of string including contents and doors south.
        :return: string representing bottom of room
        """
        return ("*  *  *", "*  -  *")[self.room_dict["south"]]

    def can_enter(self):
        """
        Returns True if can enter.  Not impassable and not visited.
        :return: bool
        """
        return self.contents != "*" and not self.visited

    def clear_room(self):
        """
        Clears all settings in a room back to nothing.  Not visited, not impassable, no potions, not monsters.
        :return:
        """
        self.room_dict["health"] = 0
        self.room_dict["vision"] = 0
        self.contents = " "
        self.room_dict["monster"] = None

    @property
    def exit(self):
        """
        Returns if room is the exit.
        :return: bool True if it is, False if it isn't.
        """
        return self.contents == "O"

    @exit.setter
    def exit(self, is_exit: bool):
        """
        Sets exit to a new boolean provided.
        :param is_exit: bool, True if changing the room to being the exit, False if not
        """
        if self.__is_boolean(is_exit) and is_exit:
            self.clear_room()
            self.contents = "O"
        elif not is_exit:
            self.contents = " "

    @property
    def entrance(self):
        """
        Returns if current room is the entrance.
        :return: bool, True if it is the entrance, False if not
        """
        return self.contents == "i"

    @entrance.setter
    def entrance(self, is_entrance: bool):
        """
        Sets whether or not the room is an entrance or not.
        :param is_entrance: bool of whether or not the room is to be set as the entrance
        """
        if self.__is_boolean(is_entrance) and is_entrance:
            self.clear_room()
            self.contents = "i"
        elif not is_entrance:
            self.contents = " "

    @property
    def health_potion(self):
        """
        Returns current quantity of health_potions in the room as int
        :return: int of current number of health_potions.
        """
        return self.__room_dict["health"]

    @health_potion.setter
    def health_potion(self, num_pots):
        """
        Sets health_potion quantity in room to a specific number.
        :param num_pots: integer >= 0
        """
        if self.__is_number_gt_eq_0(num_pots):
            self.room_dict["health"] = num_pots
            updated = self.__update_room_contents()
            if not updated:
                self.contents = "H"


    @property
    def vision_potion(self):
        """
        Getter for current number of vision potions in a room.
        :return: int for current quantity of vision_potions
        """
        return self.room_dict["vision"]

    @vision_potion.setter
    def vision_potion(self, num_pots):
        """
        Sets vision_potion quantity in room to a specific number.
        :param num_pots: integer >= 0
        """
        if self.__is_number_gt_eq_0(num_pots):
            self.room_dict["vision"] = num_pots
            updated = self.__update_room_contents()
            if not updated:
                self.contents = "V"

    def get_door(self, direction):
        """
        Given a direction, returns a boolean for if the door exists.
        :param direction: string either 'north', 'east', 'west', or 'south'
        :return: bool, True for if there is a door, False for if there isn't
        """
        try:
            return self.__room_dict[direction]
        except KeyError:
            raise KeyError(f"{direction} is not a valid key!  Must be 'north', east', west', or 'south' as a string.")

    def set_door(self, direction, door_exists):
        """
        Given a direction and a boolean, sets the door in that direction to match the boolean.
        :param direction: string either 'north', 'east', 'west', or 'south'
        :param door_exists: bool of whether door exists or not (True for yes, False for no)
        :raises KeyError: if direction isn't a valid door
        :raises TypeError: if door_exists is not a boolean
        :return: None
        """
        if self.__is_boolean(door_exists):
            try:
                self.room_dict[direction]  # Verifies is valid direction.  I'm sure there's a better way to do this.
                self.room_dict[direction] = door_exists
            except KeyError:
                raise KeyError(f"{direction} is not a valid key!  Most be north, east, west, south as a string.")

    @property
    def is_empty(self):
        """
        Returns bool if room is empty or not.  True if it is, False if it isn't.
        :return: bool
        """
        return self.contents == " "

    @property
    def contents(self):
        """
        Returns current contents of a room as a string.
        :return: str
        """
        return self.__room_dict["contents"]

    @contents.setter
    def contents(self, data: str):
        """
        Setter for contents if contents are valid.
        :param data: str " ", "A", "P", "I", "E", "i", "O", "*", "H", "V", "X", "M"
        """
        if self.__is_valid_contents(data):
            self.__room_dict["contents"] = data

    @property
    def monster(self):
        """
        Returns monster in the room.
        :return: Monster, None if no Monster
        """
        return self.room_dict["monster"]

    @monster.setter
    def monster(self, monster_obj: Monster):
        self.room_dict["monster"] = monster_obj
        self.__update_room_contents()

    @property
    def visited(self):
        """
        Checks if any of the rooms were visited during creation of the dungeon / traversal.
        :return: bool, True if any doors exist
        """
        return self.room_dict["north"] or self.room_dict["east"] or self.room_dict["south"] or self.room_dict["west"]

    @property
    def room_dict(self):
        return self.__room_dict

    @property
    def doors(self):
        """
        Returns dictionary for "east", "west", "north", and "south" doors with matching bool (True if door in that
        direction, false otherwise).
        :return: dict representing directions and whether there's a door there.
        """
        doors_dict = {}
        keys = {"east", "west", "north", "south"}
        for key in keys:
            doors_dict[key] = self.__room_dict[key]
        return doors_dict

    def json_dict(self):
        """
        :return: dictionary in json friendly format with objects within dict converted to json friendly dicts.
        """
        temp = self.room_dict.copy()
        if self.monster:
            temp["monster"] = self.monster.char_dict
        return temp
