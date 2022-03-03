import unittest
from app.model.dungeon.map import Map


class TestMap(unittest.TestCase):
    def setUp(self, rows=5, cols=5) -> None:
        dungeon = {"rows": rows, "cols": cols}
        visited_array = []
        for row in range(dungeon["rows"]):
            visited_array.append([])
            for col in range(dungeon["cols"]):
                visited_array[row].append([])
                visited_array[row][col] = False
        map_dict = {"rows": dungeon["rows"], "cols": dungeon["cols"], "visited_array": visited_array}
        self.__map = Map(map_dict)

    def test_init(self):
        try:
            self.setUp()
            self.assertEqual(True, True)
        except TypeError:
            self.assertEqual(True, False, "Failed to create instance")

    def test_init_rows_cols(self):
        expected_rows = 5
        expected_cols = 6
        self.setUp(expected_rows, expected_cols)
        mock_map = self.__map
        self.assertEqual(expected_rows, mock_map.get_rows())
        self.assertEqual(expected_cols, mock_map.get_cols())

    def test_init_rows_cols_str(self):
        try:
            self.setUp("a", "b")
            map = self.__map
        except TypeError:
            self.assertRaises(TypeError, "Strings are not valid row and column numbers.")

    def test_init_rows_cols_missing_args(self):
        try:
            map = Map(1)
        except TypeError:
            self.assertRaises(TypeError, "Missing args for the constructor.")

    def test_init_rows_cols_extra_args(self):
        try:
            map = Map(5,6,7)
        except TypeError:
            self.assertRaises(TypeError, "extra args than expected for the constructor.")

    def test_get_rows(self):
        self.setUp(5, 6)
        map = self.__map
        self.assertEqual(5, map.get_rows())

    def test_get_cols(self):
        self.setUp(5, 6)
        map = self.__map
        self.assertEqual(6, map.get_cols())

    def test_set_rows(self):
        self.setUp(5, 6)
        map = self.__map
        map.set_rows(6)
        self.assertEqual(6, map.get_rows())

    def test_set_cols(self):
        self.setUp(5, 6)
        map = self.__map
        map.set_cols(5)
        self.assertEqual(5, map.get_cols())

    def test_create_visited_room_array(self):
        self.setUp(20, 20)
        map_to_be_compared = self.__map
        mock_array = []
        for row in range(0, 20):
            mock_array.append([])
            for col in range(0, 20):
                mock_array[row].append([])
                mock_array[row][col] = False
        self.assertEqual(mock_array, map_to_be_compared.visited_array())

    def test_set_visited_room(self):
        self.setUp(5, 6)
        mock_map = self.__map
        mock_map.set_visited_room(0, 0)
        self.assertTrue(mock_map.visited_array()[0][0], "room at the top left corner should be true")

    def test_visited_array(self):
        self.setUp(20, 20)
        map_to_be_compared = self.__map
        mock_array = []
        for row in range(0, 20):
            mock_array.append([])
            for col in range(0, 20):
                mock_array[row].append([])
                mock_array[row][col] = False
        mock_array[5][5]= True
        map_to_be_compared.set_visited_room(5, 5)
        self.assertEqual(mock_array, map_to_be_compared.visited_array(), "They should be equal.")
