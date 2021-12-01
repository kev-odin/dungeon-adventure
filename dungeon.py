"""
Steph's Time Tracker~!
2 hours
"""

import random
from room import Room


class Dungeon:

    def __init__(self, row_count, col_count):
        self.__maze = []
        self.__rowCount = row_count
        self.__colCount = col_count
        self.__accessible_rooms = []
        total_rooms = row_count * col_count

        for row in range(0, self.__rowCount):
            self.__maze.append([])
            for col in range(0, self.__colCount):
                self.__maze[row].append([])
                random_number = random.randint(0, total_rooms)
                if random_number/total_rooms < 0.1:  # 10% of rooms will be impassable.  NO HARDCODE BEFORE SHARING.
                    new_room = Room(impassable=True)
                else:
                    new_room = Room()
                self.__maze[row][col] = new_room

            # self.__maze.append([Room() for c in range(0, self.__colCount)])
        self.build_maze()

    def build_maze(self):
        # make some rooms impassible
        # rand gen chance a room is impassable
        # set entrance and exit
        entrance = self.__maze[0][0]
        entrance.entrance, entrance.__impassable = True, False
        exit_room = self.__maze[1][1]
        exit_room.exit, exit_room.__impassable = True, False
        collected_pillars = ["", "", "", ""]
        curr_row, curr_col = 0, 0
        # while collected_pillars.sort() != ["A", "E", "I", "P"] and self.__maze[curr_row][curr_col] != exit:
        # self.traverse(curr_row, curr_col)
        # place pillars after entrance/exit
        a_pillar_room = self.__maze[2][1]  # Set to random place on traversed room later
        p_pillar_room = self.__maze[3][2]
        i_pillar_room = self.__maze[1][0]
        e_pillar_room = self.__maze[2][2]
        a_pillar_room.pillar, a_pillar_room.__impassable = "A", False
        p_pillar_room.pillar, p_pillar_room.__impassable = "P", False
        i_pillar_room.pillar, i_pillar_room.__impassable = "I", False
        e_pillar_room.pillar, e_pillar_room.__impassable = "E", False

    """
        #place potions and pits
        for row in range(0, self.__rowCount):
            for col in range(0, self.__colCount):
                #check for entrance/exit and impassible
                #generate a random value
                current = self.__maze[row][col]
                if not current.exit and not current.entrance and not current.pillar:
                    number = random.randint(1, 100)
                    if number >= 10:
                        self.__maze[row][col].health_potion += 1
    """

    def print_maze(self):
        # print(self.__maze)
        for row in range(0, self.__rowCount):
            print("row ", row)
            for col in range(0, self.__colCount):
                print(self.__maze[row][col].__str__())
            print()

    def set_health_potion(self, row, col):
        self.__maze[row][col].health_potion += 1

    # WARNING: Work in progress ;-)
    # initial call if you know entrance is 0,0 would be traverse(0, 0)
    def traverse(self, row, col):
        found_exit = False
        if self.is_valid_room(row, col):
            room = self.__maze[row][col]
            room.visited = True
            # check for exit
            if room.exit:
                return True
            # not at exit so try another room: south, east, north, west
            else:
                if self.is_valid_room(row + 1, col):
                    room.south_door = True
                    next_room = self.__maze[row + 1][col]
                    next_room.north_door = True
                found_exit = self.traverse(row + 1, col)  # south
                if not found_exit:
                    if self.is_valid_room(row, col + 1):
                        room.east_door = True
                        next_room = self.__maze[row][col + 1]
                        next_room.west_door = True
                    found_exit = self.traverse(row, col + 1)  # east
                if not found_exit:
                    if self.is_valid_room(row - 1, col):
                        room.north_door = True
                        next_room = self.__maze[row-1][col]
                        next_room.south_door = True
                    found_exit = self.traverse(row - 1, col)  # north
                if not found_exit:
                    if self.is_valid_room(row, col - 1):
                        room.west_door = True
                        next_room = self.__maze[row][col - 1]
                        next_room.east_door = True
                    found_exit = self.traverse(row, col - 1)  # west
                # if we did not reach the exit from this room we need mark it as visited to
                # avoid going into the room again
                # if not found_exit:
                    # self.__maze[row][col].visited = True
        # else:  # tried to move into a room that is not valid
        #    return False
        return found_exit

    def is_valid_room(self, row, col):
        return (0 <= row < self.__rowCount) and (col >= 0) and (col < self.__colCount) and self.__maze[row][col].can_enter()


dungeon = Dungeon(5, 5)
# dungeon.set_health_potion(0, 0)
if dungeon.traverse(0, 0):
    print("whoo hoo, we reached the exit")
else:
    print("exit not reachable")
dungeon.print_maze()

