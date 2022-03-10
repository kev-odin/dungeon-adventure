"""
Modified simple builder pattern to allow difficulty settings and single location configuration for rooms and dungeons.
Didn't seem necessary to include the layers of abstraction for a director or multiple builders when I just wanted to put
all my creation stuff in one spot.

Also builds map and adventurer.  All your needs met in one place!
"""
from app.model.dungeon.dungeon import Dungeon
from app.model.dungeon.room import Room
from app.model.dungeon.map import Map
from app.model.characters.priestess import Priestess
from app.model.characters.warrior import Warrior
from app.model.characters.thief import Thief
from app.model.characters.monster import Monster
from app.model.db.query_helper import QueryHelper

import random


class DungeonBuilder:
    def __init__(self, difficulty="Easy", varied=True):  # This seems like bad practice to have variables unnecessarily.
        self.__reset(difficulty, varied)

    def __reset(self, difficulty="Easy", varied=True):
        """
        Clears dungeon builder to prep it for building another dungeon.  Resets prior to build and on init.
        :param difficulty: string, "Easy", "Medium", "Hard", "Inhumane" are defaults.
        :param varied: bool, True for rooms being randomly generated contents, false for not.
        :return:
        """
        diff_options = {"Easy", "Medium", "Hard", "Inhumane"}
        if difficulty in diff_options:
            self.__qh = QueryHelper()
            self.__settings = self.__qh.query(difficulty)
        else:
            raise ValueError("difficulty must be Easy, Medium, Hard, or Inhumane")
        self.__complete_dungeon = self.__complete_map = self.__complete_adventurer = None
        self.__varied = varied
        self.__adventurer_dict = None
        self.__empty_rooms = []  # Stores list of empty rooms to be used later for pillar placement
        self.__dungeon = []
        self.__entrance = None  # Stores entrance as a tuple of int coordinates
        self.__exit = None  # Stored as a tuple of int coordinates
        self.__pillars = ["A", "P", "I", "E"]

    def __set_dungeon(self):
        """
        Passes dungeon over to dungeon and all settings then stores it as a complete_dungeon.
        :return: None
        """
        dungeon_dict = {"dungeon": self.__dungeon, "difficulty": self.__settings["difficulty"],
                        "rows": self.__settings["row"], "cols": self.__settings["col"],
                        "pillars": self.__pillars, "entrance": self.__entrance, "exit": self.__exit,
                        "adventurer_location": self.__entrance}
        self.__complete_dungeon = Dungeon(dungeon_dict)

    def __set_map(self):
        """
        Sets a map as part of the build dungeon routine.  Sets visited rooms to the entrance location.
        Visited rooms are set to True (the entrance), unvisited set to False (all other locations).
        :return: None
        """
        dungeon = self.__complete_dungeon.dungeon_dict
        visited_array = []
        for row in range(dungeon["rows"]):
            visited_array.append([])
            for col in range(dungeon["cols"]):
                visited_array[row].append([])
                visited_array[row][col] = False
        map_dict = {"rows": dungeon["rows"], "cols": dungeon["cols"], "visited_array": visited_array}
        self.__complete_map = Map(map_dict)
        self.__complete_map.set_visited_room(self.__entrance[0], self.__entrance[1])

    def __set_adventurer(self):
        """
        Based on class of adventurerer, sets self.__complete_adventurerer to match the completed class object.
        """
        adv_class = self.__adventurer_dict["adv_class"]
        if adv_class == "Warrior":
            self.__complete_adventurer = Warrior(self.__adventurer_dict)
        elif adv_class == "Priestess":
            self.__adventurer_dict["max_heal"] = self.__adventurer_dict["max_hp"]
            self.__adventurer_dict["min_heal"] = self.__adventurer_dict["max_hp"] // 4
            self.__complete_adventurer = Priestess(self.__adventurer_dict)
        elif adv_class == "Thief":
            self.__complete_adventurer = Thief(self.__adventurer_dict)

    def __get_rand_coords(self):
        return random.randint(0, self.__settings["row"] - 1), random.randint(0, self.__settings["col"] - 1)

    def __build_2d_room_maze(self):
        """
        Creates a 2D list full of rooms.  Saves it to dungeon.
        :return: None
        """
        for row in range(0, self.__settings["row"]):
            self.__dungeon.append([])
            for col in range(0, self.__settings["col"]):
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
        total_rooms = self.__settings["row"] * self.__settings["col"]
        random_number = random.randint(0, total_rooms)
        intrigue = random_number / total_rooms
        many_trigger = self.__settings["impassable_chance"] + self.__settings["many_chance"]
        hp_trigger = many_trigger + self.__settings["hp_chance"]  # range of many trigger through hp pot chance
        vision_trigger = hp_trigger + self.__settings["vp_chance"]  # range of hp trigger through vision trigger
        monster_trigger = vision_trigger + self.__settings["monster_chance"]
        if intrigue > monster_trigger:  # Boring empty room.  The best kind of room.  First for efficiency.
            new_room = Room()
        elif intrigue <= self.__settings["impassable_chance"]:  # Is it less than or equal to impassable chance?  Make no access room!
            new_room = Room(contents="*")
        elif intrigue <= many_trigger:  # A room of many things.
            new_room = Room(health_potion=random.randint(1, self.__settings["max_hp_pots"]),
                            vision_potion=random.randint(0, self.__settings["max_vp"]),
                            monster=self._build_monster(), contents="M")
        elif intrigue <= hp_trigger:  # A room of health pots.
            new_room = Room(health_potion=random.randint(1, self.__settings["max_hp_pots"]), contents="H")
        elif intrigue <= vision_trigger:  # A room of vision potion.
            new_room = Room(vision_potion=random.randint(1, self.__settings["max_vp"]), contents="V")
        else:  # intrigue <= pit_trigger: A room of pit.
            new_room = Room(monster=self._build_monster(), contents="X")
        return new_room

    def _build_monster(self, pillar_room=False):
        """
        Builds a monster.  If pillar room, builds Ogre, otherwise random between Gremlin and Skeleton.
        Method is for lazy testing only!
        :param pillar_room: bool, True if currently a pillar room.
        :return: Monster
        """
        if pillar_room:
            choice = "Ogre"  # Hardcoded, not my favorite, but works!
        else:
            choice = random.choice(("Gremlin", "Skeleton"))
        monster_dict = self.__qh.query(choice)
        monster_dict["current_hp"] = monster_dict["max_hp"]
        return Monster(monster_dict)

    def __build_dungeon_path(self, row: int, col: int):
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
            boss = True
            room.monster = self._build_monster(boss)

    def __is_traversable(self, row: int, col: int):
        """
        Verifies location is a valid room for entry.  Helper function for traversal.
        :param row: int between 0 and self.__settings["row"]
        :param col: int between 0 and self.__settings["col"]
        :return: boolean, true if untraversed valid room, false if not.
        """
        return self.__is_valid_room(row, col) and self.__dungeon[row][col].can_enter()

    def __is_valid_room(self, row: int, col: int):
        """
        Checks if room is valid (if the rows and columns are within the range of the 2D list)
        :param row: int
        :param col: int
        :return: True if row and col are both within the grid, else false.
        """
        return (0 <= row < self.__settings["row"]) and (0 <= col < self.__settings["col"])

    def __get_room(self, coordinates):
        """
        Given a row and column, returns the room at those coordinates
        :param coordinates: list of int, 0 through self.__settings["row"]-1, 0 through self.__settings["col"]-1
        :return: room at coordinates
        """
        row, col = coordinates[0], coordinates[1]
        if self.__is_valid_room(row, col):
            return self.__dungeon[row][col]
        else:
            raise ValueError("Coordinates must be a tuple of ints x and y within the range of the dungeon.")

    def build_dungeon(self, difficulty="Easy", varied=True):
        """
        Main logic for building a dungeon.  Returns the dungeon after it is built.  Defaults to 5x5 easy dungeon.
        :param difficulty: str, "easu", "medium", "hard" or "inhumane".  Defaults to easy for test dungeons.
        :param varied: bool, defaults to True.  If True, rooms are generated randomly.  If False, generate empty.
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
        self.__set_dungeon()  # Officially builds the dungeon and saves it!  Perhaps shouldn't save it.
        self.__set_map()  # Officially builds the related map!
        return self.__complete_dungeon

    def build_adventurer(self, name: str, adv_class: str):
        """Helper method for character creation. Difficulty and name are checked,
                based on those values, create an adventurer with modified base values.
                :param: name: str if found in cheat_code dictionary, modification applied to adventurer
                :param: adv_class: class that is available within the db for a adventurer class.
                """

        adv_dict = self.__qh.query(adv_class)
        adv_dict["current_hp"] = adv_dict["max_hp"]
        adv_dict["name"] = name

        expected_keys = ["name", "adv_class", "current_hp", "max_hp", "attack_speed", "hit_chance", "min_dmg", "max_dmg",
                         "block_chance", "special"]
        for key in expected_keys:
            if key not in adv_dict:
                raise KeyError(f"Expected {key} in adventurer dictionary.")

        self.__adventurer_dict = adv_dict
        self.__set_adventurer()
        return self.__complete_adventurer

    @property
    def adventurer(self):
        """
        Getter property for adventurer
        :return: adventurer created during build adventurer
        :raises RuntimeError if attempting to access adventurer without building it first.
        """
        if self.__complete_adventurer:
            return self.__complete_adventurer
        else:
            raise RuntimeError("Must build an adventurerer before accessing them..")

    @property
    def map(self):
        """
        Getter property for map.
        :return: map created during dungeon builder.
        :raises RuntimeError if attempting to access map without building it first.
        """
        if self.__complete_map:
            return self.__complete_map
        else:
            raise RuntimeError("Must build a dungeon before accessing the map for a dungeon.")
