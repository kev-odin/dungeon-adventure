"""
Time used: 34 hours: main + map + test
xingguo
"""


class Map:
    """
        Map class to create a 2D array list to store the rooms traveled.
        adjust the boolean flag of each room if adventurer traveled or used vision potion on it.
    """
    def __init__(self, map_dict):
        """
        Map class that contains rows and columns to create a list of list
        :param rows: rows of the 2d array
        :type rows: int
        :param cols: columns of the 2d array
        :type cols: int
        """
        keys = {"visited_array", "rows", "cols"}
        for key in keys:
            if key not in map_dict:
                raise KeyError(f"{key} is missing from map dictionary.  Please check map creation in dungeon builder.")
        self.__map_dict = map_dict

    def __room_in_bound(self, row, col):
        """
        method to check if the room is within range
       :param row: row of the current room
        :type row: int
        :param col: column of the current room
        :type col: int
        :return: True if the room is within bounds of the array
                False if it is not
        """
        if 0 <= row < self.__map_dict["rows"] and 0 <= col < self.__map_dict["cols"]:
            return True
        else:
            return False

    def use_vision_potion(self, row, col):
        """
        method to find the adjacent rooms
        :param row: row of the current room
        :type row: int
        :param col: column of the current room
        :type col: int
        """
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if self.__room_in_bound(i, j):
                    self.set_visited_room(i, j)  # we set the adjacent room's visibility as True

    def set_visited_room(self, row, col):
        """
        method to set the visited rooms' bool flag to True
        :param row: row of the current room
        :type row: int
        :param col: column of the current room
        :type col: int
        """
        self.__map_dict["visited_array"][row][col] = True  # adv_curr_map.set_visited_room(i,j) in main function

    def visited_array(self):
        """
        getter method to return the visited array
        :return:visited array
        """
        return self.__map_dict["visited_array"]

    def get_rows(self):
        """
        getter method to return the rows
        :return: rows
        """
        return self.__map_dict["rows"]

    def set_rows(self, new_rows):
        """
        setter method to set the new row number
        :param new_rows: new number to set the row
        """
        self.__map_dict["rows"] = new_rows

    def get_cols(self):
        """
        getter method to return the columns
        :return: columns
        """
        return self.__map_dict["cols"]

    def set_cols(self, new_cols):
        """
        setter method to set the new column number
        :param new_cols: new number to set the column
        """
        self.__map_dict["cols"] = new_cols

    @property
    def map_dict(self):
        return self.__map_dict
