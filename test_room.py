import unittest
from room import Room


class TestRoom(unittest.TestCase):
    def test_init_default_str(self):
        test = Room()
        expected = f"***\n* *\n***\n"
        self.assertEqual(expected, test.__str__(), "Check your to string method.")

    def test_init_default_health_potions(self):
        test = Room()
        expected = 0
        self.assertEqual(expected, test.health_potion, "Check health potion property.  Default should be 0.")

    def test_init_default_vision_potions(self):
        test = Room()
        expected = 0
        self.assertEqual(expected, test.vision_potion, "Check vision potion property.  Default should be 0.")

    def test_init_default_entrance(self):
        test = Room()
        expected = False
        self.assertEqual(expected, test.entrance, "Should not be an entrance by default")

    def test_init_default_can_enter(self):
        test = Room()
        expected = True
        self.assertEqual(expected, test.can_enter(), "Should be able to enter a room by default.")

    def test_init_default_is_exit(self):
        test = Room()
        expected = False
        self.assertEqual(expected, test.exit, "Should not be an exit by default.")

    def test_init_default_is_visited(self):
        test = Room()
        expected = False
        self.assertEqual(expected, test.visited, "Should be visited by default.")

    def test_setter_health_potion_2(self):
        test = Room()
        expected = 2
        test.health_potion = expected
        self.assertEqual(expected, test.health_potion, "Check health potion setter.")

    def test_setter_vision_potion_2(self):
        test = Room()
        expected = 2
        test.vision_potion = expected
        self.assertEqual(expected, test.vision_potion, "Check vision potion setter.")

    def test_setter_health_potion_string(self):
        test = Room()
        try:
            test.health_potion = "2"
            self.assertEqual(True, False, "Error should be raised when fed string.")
        except TypeError:
            self.assertEqual(True, True)

    def test_setter_vision_potion_string(self):
        test = Room()
        try:
            test.vision_potion = "2"
            self.assertEqual(True, False, "Error should be raised when fed string.")
        except TypeError:
            self.assertEqual(True, True)

    def test_setter_health_potion_negative(self):
        test = Room()
        try:
            test.health_potion = -2
            self.assertEqual(True, False, "Error should be raised when fed string.")
        except ValueError:
            self.assertEqual(True, True)

    def test_setter_vision_potion_negative(self):
        test = Room()
        try:
            test.vision_potion = -1
            self.assertEqual(True, False, "Error should be raised when fed string.")
        except ValueError:
            self.assertEqual(True, True)

    def test_entrance_setter_valid(self):
        test = Room()
        expected = True
        test.entrance = expected
        self.assertEqual(expected, test.entrance, "Check entrance setter.")

    def test_entrance_setter_int(self):
        test = Room()
        try:
            test.entrance = 1
            self.assertEqual(True, False, "TypeError expected for int setter with entrance")
        except TypeError:
            self.assertEqual(True, True)

    def test_exit_setter_valid(self):
        test = Room()
        expected = True
        test.exit = expected
        self.assertEqual(expected, test.exit, "Check exit setter.")

    def test_exit_setter_string(self):
        test = Room()
        try:
            test.exit = "True"
            self.assertEqual(True, False, "TypeError expected for string setter with exit")
        except TypeError:
            self.assertEqual(True, True)

    def test_partial_init_string(self):
        test = Room(health_potion=2, pit=10, north_door=True)
        self.assertEqual("*-*\n*M*\n***\n", test.__str__(), "Check string for multiples and north doors")

    def test_partial_init_hp(self):
        test = Room(health_potion=2, pit=10, north_door=True)
        self.assertEqual(2, test.health_potion, "Check init for partial variables with health potions")

    def test_partial_init_pit_damage(self):
        test = Room(health_potion=2, pit=10, north_door=True)
        self.assertEqual(10, test.pit_damage, "Check init for partial variables.  Pit should do 10 damage")

    def test_partial_init_north_door(self):
        test = Room(health_potion=2, pit=10, north_door=True)
        self.assertEqual(True, test.north_door, "Check init for partial variables.  north door should be True.")

    def test_partial_init_doors(self):
        test = Room(north_door=True, south_door=True, east_door=True, west_door=True)
        self.assertEqual(True, test.north_door, "Check door inits or getters north")
        self.assertEqual(True, test.south_door, "Check door inits or getters south")
        self.assertEqual(True, test.east_door, "Check door inits or getters east")
        self.assertEqual(True, test.west_door, "Check door inits or getters west")

    def test_partial_init_doors_strings(self):
        test = Room(north_door=True, south_door=True, east_door=True, west_door=True)
        self.assertEqual("*-*\n| |\n*-*\n", test.__str__(), "Check string for opening doors")

    def test_partial_init_potions(self):
        test = Room(vision_potion=2, health_potion=1)
        self.assertEqual(False, test.north_door, "Check door inits or getters north")  # Juuuust in case.
        self.assertEqual(False, test.south_door, "Check door inits or getters south")
        self.assertEqual(False, test.east_door, "Check door inits or getters east")
        self.assertEqual(False, test.west_door, "Check door inits or getters west")
        self.assertEqual(2, test.vision_potion, "Check init for vision potions")
        self.assertEqual(1, test.health_potion, "Check init for health potions")

    def test_partial_init_potions_multiple_string(self):
        test = Room(vision_potion=2, health_potion=1)
        self.assertEqual("***\n*M*\n***\n", test.__str__(), "Check string for multiple potions")

    def test_partial_init_pillar_A(self):
        test = Room(pillar="A")
        self.assertEqual("A", test.pillar, "Something went wrong with pillar init")
        self.assertEqual("***\n*A*\n***\n", test.__str__(), "Check string for pillar")

    def test_pillar_validity_P(self):
        test = Room(pillar="P")
        self.assertEqual("P", test.pillar, "Something went wrong with pillar init")
        self.assertEqual("***\n*P*\n***\n", test.__str__(), "Check string for pillar")

    def test_pillar_validity_I(self):
        test = Room(pillar="I")
        self.assertEqual("I", test.pillar, "Something went wrong with pillar init")
        self.assertEqual("***\n*I*\n***\n", test.__str__(), "Check string for pillar")

    def test_pillar_validity_E(self):
        test = Room(pillar="E")
        self.assertEqual("E", test.pillar, "Something went wrong with pillar init")
        self.assertEqual("***\n*E*\n***\n", test.__str__(), "Check string for pillar")

    def test_pillar_validity_value_error(self):
        try:
            test = Room(pillar="Frank")
            self.assertEqual(True, False, "Value error expected in pillar validation")
        except ValueError:
            self.assertEqual(True, True)

    def test_pillar_validity_type_error(self):
        try:
            test = Room(pillar=1)
            self.assertEqual(True, False, "Type error expected in pillar validation")
        except TypeError:
            self.assertEqual(True, True)

    def test_init_pit_to_string(self):
        try:
            test = Room(pit="2")
            self.assertEqual(True, False, "Type error expected in pit validation")
        except TypeError:
            self.assertEqual(True, True)

    def test_init_pit_to_float(self):
        try:
            test = Room(pit=2.0)
            self.assertEqual(True, False, "Type error expected in pit validation")
        except TypeError:
            self.assertEqual(True, True)

    def test_init_pit_string(self):
        test = Room(pit=10)
        self.assertEqual("***\n*X*\n***\n", test.__str__(), "Check string for pit")

    def test_hp_string(self):
        test = Room(health_potion=1)
        self.assertEqual("***\n*H*\n***\n", test.__str__(), "Check string for health potions")

    def test_vision_potion_string(self):
        test = Room(vision_potion=1)
        self.assertEqual("***\n*V*\n***\n", test.__str__(), "Check string for vision potions")

    def test_exit_string(self):
        test = Room(is_exit=True)
        self.assertEqual("***\n*O*\n***\n", test.__str__(), "Check string for exit")

    def test_entrance_string(self):
        test = Room(entrance=True)
        self.assertEqual("***\n*i*\n***\n", test.__str__(), "Check string for exit")


if __name__ == '__main__':
    unittest.main()
