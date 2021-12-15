import unittest
from map import Map


class TestMap(unittest.TestCase):

    def test_init(self):
        try:
            map = Map(5,5)
            self.assertEqual(True, True)
        except TypeError:
            self.assertEqual(True, False, "Failed to create instance")

    def test_init_rows_cols(self):
        mock_map = Map(5,6)
        expected_rows = 5
        expected_cols = 6
        self.assertEqual(expected_rows, mock_map.get_rows())
        self.assertEqual(expected_cols, mock_map.get_cols())

    def test_init_rows_cols_str(self):
        try:
            map = Map("a","b")
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
        map = Map(5,6)
        self.assertEqual(5, map.get_rows())

    def test_get_cols(self):
        map = Map(5,6)
        self.assertEqual(6, map.get_cols())

    def test_set_rows(self):
        map = Map(5,6)
        map.set_rows(6)
        self.assertEqual(6, map.get_rows())

    def test_set_cols(self):
        map = Map(5,6)
        map.set_cols(5)
        self.assertEqual(5, map.get_cols())

    def test_create_visited_room_array(self):
        map1 = Map(20, 20)

        mock_array = []
        for row in range(0, 20):
            mock_array.append([])
            for col in range(0, 20):
                mock_array[row].append([])
                mock_array[row][col] = False
        self.assertEqual(mock_array, map1.visited_array())

    def test_set_visited_room(self):
        map = Map(5, 6)
        map.set_visited_room(0, 0)
        self.assertTrue(map.visited_array()[0][0], "room at the top left corner should be true")

    def test_visited_array(self):
        map1 = Map(20, 20)
        mock_array = []
        for row in range(0, 20):
            mock_array.append([])
            for col in range(0, 20):
                mock_array[row].append([])
                mock_array[row][col] = False
        mock_array[5][5]= True
        map1.set_visited_room(5, 5)
        self.assertEqual(mock_array, map1.visited_array(), "They should be equal.")
