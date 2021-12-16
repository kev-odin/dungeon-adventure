"""
Time used: 34 hours: main + map + test
xingguo
"""


class Map:
    def __init__(self, rows, cols):
        self.__visited_array = []
        self.__rows = rows
        self.__cols = cols
        self.__create_visited_room_array()

    def __room_in_bound(self, row, col):
        if 0 <= row < self.__rows and 0 <= col < self.__cols:
            return True
        else:
            return False

    def __create_visited_room_array(self):
        for row in range(0, self.__rows):
            self.__visited_array.append([])
            for col in range(0, self.__cols):
                self.__visited_array[row].append([])
                self.__visited_array[row][col] = False

    def use_vision_potion(self, row, col):
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if self.__room_in_bound(i, j):
                    self.set_visited_room(i, j)  # we set the adjacent room's visibility as True

    def set_visited_room(self, row, col):
        self.__visited_array[row][col] = True  # adv_curr_map.set_visited_room(i,j) in main function

    def visited_array(self):
        return self.__visited_array

    def get_rows(self):
        return self.__rows

    def set_rows(self, new_rows):
        self.__rows = new_rows

    def get_cols(self):
        return self.__cols

    def set_cols(self, new_cols):
        self.__cols = new_cols