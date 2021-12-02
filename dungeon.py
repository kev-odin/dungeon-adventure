"""
Steph's Time Tracker~!
4 hours to working properly with no error checking or fun.
"""

import random
from room import Room


class Dungeon:
    def __init__(self, row_count, col_count, impassable_chance=0.05, pillars=["A", "P", "I", "E"], hp_pot_chance=0.1,
                 vision_chance=0.05, many_chance=0.05, pit_chance=0.1, max_hp_pots=2, max_vision=1, max_pit_damage=20):
        """
        Welcome to the dungeon!  Allows for hardcoded difficulty to be adjusted in the event we want to add different
        difficulty settings as an extra credit feature (ex. increase pit chance and damage)
        :param row_count:
        :param col_count:
        :param impassable_chance:
        :param pillars:
        :param hp_pot_chance:
        :param vision_chance:
        :param many_chance:
        :param pit_chance:
        :param max_hp_pots:
        :param max_vision:
        :param max_pit_damage:
        """
        if len(pillars) + 2 < (row_count * col_count * (impassable_chance + pit_chance + hp_pot_chance + vision_chance +
                               many_chance)):  # If not, very unlikely maze will successfully generate
            self.__dungeon = []
            self.__row_count = row_count
            self.__col_count = col_count
            self.__empty_rooms = []  # Stores list of empty rooms to be used later for pillar placement
            self.__pillars = pillars  # To be popped into rooms
            self.__impassable_chance = impassable_chance  # 5% of rooms will be impassable
            self.__hp_pot_chance = hp_pot_chance  # max number of potions vs. max damage pits do
            self.__vision_chance = vision_chance
            self.__many_chance = many_chance  # It is vital to fall in a pit and find potions on bodies of unfortunates.
            self.__pit_chance = pit_chance
            self.__max_hp_pots = max_hp_pots
            self.__max_vision = max_vision
            self.__pit_pain = max_pit_damage  # max number of damage a pit can do.
            self.__build_maze()
        else:
            raise ValueError("Rows * Columns  / 2 must be greater than len(pillars) + 2.")

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

    def create_room(self):
        return self.__create_room()
    def __create_room(self):
        """
        Generates rooms to be input to the maze that are either impassable, pits and potions, potions, pits, or boring.
        :return: room
        """
        total_rooms = self.__row_count * self.__col_count
        random_number = random.randint(0, total_rooms)
        intrigue = random_number / total_rooms
        many_trigger = self.__impassable_chance + self.__many_chance  # range of impassable through many
        hp_trigger = many_trigger + self.__hp_pot_chance  # range of many trigger through hp pot chance
        vision_trigger = hp_trigger + self.__vision_chance  # range of hp trigger through vision trigger
        pit_trigger = vision_trigger + self.__pit_chance
        if intrigue <= self.__impassable_chance:
            new_room = Room(impassable=True)
        elif intrigue <= many_trigger:
            new_room = Room(health_potion=random.randint(0, self.__max_hp_pots),
                            vision_potion=random.randint(0, self.__max_vision),
                            pit=random.randint(0, self.__pit_pain))
        elif intrigue <= hp_trigger:
            new_room = Room(health_potion=random.randint(0, self.__max_hp_pots))
        elif intrigue <= vision_trigger:
            new_room = Room(vision_potion=random.randint(0, self.__max_vision))
        elif intrigue <= pit_trigger:
            new_room = Room(pit=random.randint(1, self.__pit_pain))
        else:  # Boring empty room.
            new_room = Room()
        return new_room

    def __create_2d_room_maze(self):
        """

        :return: None
        """
        for row in range(0, self.__row_count):
            self.__dungeon.append([])
            for col in range(0, self.__col_count):
                self.__dungeon[row].append([])
                new_room = self.__create_room()
                self.__dungeon[row][col] = new_room

    def __add_pillars(self):
        pillars_left = len(self.__pillars)
        pillars = self.__copy_of_list(self.__pillars)
        while pillars_left > 0:
            current = random.choice(self.__empty_rooms)
            self.__empty_rooms.remove(current)
            current.pillar = pillars.pop()
            pillars_left -= 1

    @staticmethod
    def __copy_of_list(copied):
        copy = []
        for datum in copied:
            copy.append(datum)
        return copy

    @staticmethod
    def __check_if_empty_room(a_room):
        return not a_room.exit and not a_room.pillar and not a_room.entrance and not a_room.health_potion \
               and not a_room.vision_potion and not a_room.pit_damage

    def __build_maze(self):
        reach_exit = False
        pillar_options = 0
        num_pillars = len(self.__pillars)
        while (not reach_exit) or (pillar_options < num_pillars):  # If can't traverse or spots for pillars, resets.
            self.__create_2d_room_maze()
            ent_row, ent_col = random.randint(0, self.__row_count-1), random.randint(0, self.__col_count-1)
            exit_row, exit_col = random.randint(0, self.__row_count-1), random.randint(0, self.__col_count-1)
            entrance = self.__dungeon[ent_row][ent_col]
            entrance.clear_room()
            entrance.entrance = True
            exit_room = self.__dungeon[exit_row][exit_col]
            exit_room.clear_room()
            exit_room.exit = True
            reach_exit = self.__traverse(ent_row, ent_col)
            pillar_options = len(self.__empty_rooms)
        self.__add_pillars()

    def print_maze(self):
        # print(self.__maze)
        for row in range(0, self.__row_count):
            print("row ", row)
            for col in range(0, self.__col_count):
                print(self.__dungeon[row][col].__str__())
            print()

    def set_health_potion(self, row, col, num):
        self.__dungeon[row][col].health_potion = num

    def __try_a_room(self, row, col):
        room = self.__dungeon[row][col]
        if self.__is_valid_room(row + 1, col):
            room.south_door = True
            next_room = self.__dungeon[row + 1][col]
            next_room.north_door = True
        found_exit = self.__traverse(row + 1, col)  # south
        if not found_exit:
            if self.__is_valid_room(row, col + 1):
                room.east_door = True
                next_room = self.__dungeon[row][col + 1]
                next_room.west_door = True
            found_exit = self.__traverse(row, col + 1)  # east
        if not found_exit:
            if self.__is_valid_room(row - 1, col):
                room.north_door = True
                next_room = self.__dungeon[row - 1][col]
                next_room.south_door = True
            found_exit = self.__traverse(row - 1, col)  # north
        if not found_exit:
            if self.__is_valid_room(row, col - 1):
                room.west_door = True
                next_room = self.__dungeon[row][col - 1]
                next_room.east_door = True
            found_exit = self.__traverse(row, col - 1)  # west

    # initial call if you know entrance is 0,0 would be traverse(0, 0)
    def __traverse(self, row, col):
        found_exit = False
        if self.__is_valid_room(row, col):
            room = self.__dungeon[row][col]
            if self.__check_if_empty_room(room):
                self.__empty_rooms.append(room)  # Places to put pillars later
            room.visited = True  # No coming back here!
            # check for exit
            if room.exit:
                return True
            # not at exit so try another room: south, east, north, west
            else:
                room_options = [1, 2, 3, 4]
                random.choice(room_options)
                if self.__is_valid_room(row + 1, col):
                    room.south_door = True
                    next_room = self.__dungeon[row + 1][col]
                    next_room.north_door = True
                found_exit = self.__traverse(row + 1, col)  # south
                if not found_exit:
                    if self.__is_valid_room(row, col + 1):
                        room.east_door = True
                        next_room = self.__dungeon[row][col + 1]
                        next_room.west_door = True
                    found_exit = self.__traverse(row, col + 1)  # east
                if not found_exit:
                    if self.__is_valid_room(row - 1, col):
                        room.north_door = True
                        next_room = self.__dungeon[row - 1][col]
                        next_room.south_door = True
                    found_exit = self.__traverse(row - 1, col)  # north
                if not found_exit:
                    if self.__is_valid_room(row, col - 1):
                        room.west_door = True
                        next_room = self.__dungeon[row][col - 1]
                        next_room.east_door = True
                    found_exit = self.__traverse(row, col - 1)  # west
        return found_exit

    def __is_valid_room(self, row, col):
        return (0 <= row < self.__row_count) and (col >= 0) and (col < self.__col_count) \
               and self.__dungeon[row][col].can_enter()
