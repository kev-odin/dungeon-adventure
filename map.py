class Map:
    def __init__(self, row, col):
        self.__visited_array = []
        self.create_visited_room_array()
        self._row = row
        self._col = col

    def create_visited_room_array(self):
        for row in range(0, 20):
            self.__visited_array.append([])
            for col in range(0, 20):
                self.__visited_array[row].append([])
                self.__visited_array[row][col] = False

    def set_visited_room(self, row, col):
        self.__visited_array[row][col] = True

    def visited_array(self):
        return self.__visited_array
