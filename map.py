class Map:
    def __init__(self):
        self.__visited_array = []
        self.create_visited_room_array()

    def create_visited_room_array(self):
        for row in range(0, 20): # how to find out the size,change in the future  5x5;8x8;10x10
            self.__visited_array.append([])
            for col in range(0, 20):
                self.__visited_array[row].append([])
                self.__visited_array[row][col] = False

    def set_visited_room(self, row, col):
        self.__visited_array[row][col] = True

    def use_vision_potion(self):
        pass

    def visited_array(self):
        return self.__visited_array
    # maintain a 2D array to reveal the fog of war on the dungeon