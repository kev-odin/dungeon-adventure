class Map:
    def __init__(self, row, col):
        self.__visited_array = []
        self.__row = row
        self.__col = col
        self.create_visited_room_array()

    def create_visited_room_array(self):
        for row in range(0, 20):
            self.__visited_array.append([])
            for col in range(0, 20):
                self.__visited_array[row].append([])
                self.__visited_array[row][col] = False

    def set_visited_room(self, row, col):
        self.__visited_array[row][col] = True # adv_curr_map.set_visited_room(i,j) in main function

    def visited_array(self):
        return self.__visited_array
