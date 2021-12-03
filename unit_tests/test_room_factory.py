import unittest
from room_factory import RoomFactory


class TestRoomFactory(unittest.TestCase):
    def test_create_a_room(self):
        rf = RoomFactory()
        room1 = rf.create_room(1)
        room2 = rf.create_room(1)
        room1.clear_room()
        room2.clear_room()
        self.assertEqual(room1, room2, "Cleared rooms created from dungeon expected to be equal.")

if __name__ == '__main__':
    unittest.main()
