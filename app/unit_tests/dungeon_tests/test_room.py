import unittest
from app.model.dungeon.room import Room
from app.model.dungeon.dungeon_builder import DungeonBuilder


class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        db = DungeonBuilder()
        self._ogre = db._build_monster(True)

    def test_init_default_str(self):
        test = Room()
        expected = f"*  *  *\n*     *\n*  *  *\n"
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

    def test_can_enter(self):
        test = Room(contents="*")
        expected = False
        self.assertEqual(expected, test.can_enter(), "Should not be able to enter impassable room.")

    def test_can_enter_visited(self):
        test = Room()
        test.set_door("north", True)
        expected = False
        self.assertEqual(expected, test.can_enter(), "Should not be able to enter already entered room with door.")

    def test_init_default_is_exit(self):
        test = Room()
        expected = False
        self.assertEqual(expected, test.exit, "Should not be an exit by default.")

    def test_init_default_is_visited(self):
        test = Room()
        expected = False
        self.assertEqual(expected, test.visited, "Should be visited by default.")

    def test_is_visited_with_door_change(self):
        test = Room()
        expected = True
        test.set_door("east", True)
        self.assertEqual(expected, test.visited, "Should be visited if door exists.")

    def test_is_eq(self):
        test = Room()
        expected = True
        check = test == test
        self.assertEqual(expected, check, "Room should equal itself.  Check __eq__ and strings.")

    def test_is_not_eq(self):
        test1 = Room()
        test2 = Room(contents="i")
        expected = False
        check = test1 == test2
        self.assertEqual(expected, check, "Empty room should not equal an entrance.")

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

    def test_entrance_setter_changed_contents(self):
        test = Room(monster=10, contents="X")
        test.entrance = True
        self.assertEqual("i", test.contents, "Contents should have been updated to 'i'")

    def test_entrance_setter_cleared_room(self):
        test = Room(monster=self._ogre, contents="X")
        test.entrance = True
        self.assertEqual(None, test.monster, "Monster should be None")

    def test_exit_setter_valid(self):
        test = Room()
        expected = True
        test.exit = expected
        self.assertEqual(expected, test.exit, "Check exit setter.")

    def test_exit_setter_string(self):
        test = Room()
        try:
            test.exit = "O"
            self.assertEqual(True, False, "TypeError expected for string setter with exit")
        except TypeError:
            self.assertEqual(True, True)

    def test_exit_setter_changed_contents(self):
        test = Room(monster=20, contents="X")
        test.exit = True
        self.assertEqual("O", test.contents, "Contents once set exit should be 'O'")

    def test_exit_setter_cleared_monster(self):
        test = Room(monster=self._ogre, contents="X")
        test.exit = True
        self.assertEqual(None, test.monster, "Contents once set exit should be 'O'")

    def test_partial_init_string(self):
        test = Room(health_potion=2, monster=10, contents="M")
        self.assertEqual("*  *  *\n*  M  *\n*  *  *\n", test.__str__(), "Check string for multiples and north doors")

    def test_partial_init_hp(self):
        test = Room(health_potion=2, monster=10, contents="M")
        self.assertEqual(2, test.health_potion, "Check init for partial variables with health potions")

    def test_partial_init_pit_damage(self):
        test = Room(health_potion=2, monster=self._ogre, contents="M")
        self.assertEqual(self._ogre, test.monster, "Check init for partial variables. Monster should exist.")

    def test_init_then_set_north_door(self):
        test = Room(health_potion=2, monster=10, contents="M")
        test.north_door = True
        self.assertEqual(True, test.north_door, "Check init for partial variables.  north door should be True.")

    def test_monster_getter(self):
        test = Room(health_potion=2, monster=self._ogre, contents="M")
        self.assertEqual(self._ogre, test.monster, "Check monster getter")

    def test_set_doors(self):
        test = Room()
        test.set_door("north", True)
        test.set_door("south", True)
        test.set_door("east", True)
        test.set_door("west", True)
        self.assertEqual(True, test.get_door("north"), "Check door inits or getters north")
        self.assertEqual(True, test.get_door("south"), "Check door inits or getters south")
        self.assertEqual(True, test.get_door("east"), "Check door inits or getters east")
        self.assertEqual(True, test.get_door("west"), "Check door inits or getters west")

    def test_create_doors_strings(self):
        test = Room()
        test.set_door("north", True)
        test.set_door("south", True)
        test.set_door("east", True)
        test.set_door("west", True)
        self.assertEqual("*  -  *\n|     |\n*  -  *\n", test.__str__(), "Check string for opening doors")

    def test_partial_init_potions(self):
        test = Room(health_potion=1, vision_potion=2, contents="M")
        self.assertEqual(False, test.get_door("north"), "Check door inits or getters north")  # Juuuust in case.
        self.assertEqual(False, test.get_door("south"), "Check door inits or getters south")
        self.assertEqual(False, test.get_door("east"), "Check door inits or getters east")
        self.assertEqual(False, test.get_door("west"), "Check door inits or getters west")
        self.assertEqual(2, test.vision_potion, "Check init for vision potions")
        self.assertEqual(1, test.health_potion, "Check init for health potions")

    def test_partial_init_potions_multiple_string(self):
        test = Room(health_potion=1, vision_potion=2, contents="M")
        self.assertEqual("*  *  *\n*  M  *\n*  *  *\n", test.__str__(), "Check string for multiple potions")

    def test_init_pit_string(self):
        test = Room(monster=self._ogre, contents="X")
        self.assertEqual("*  *  *\n*  X  *\n*  *  *\n", test.__str__(), "Check string for pit")

    def test_hp_string(self):
        test = Room(health_potion=1, contents="H")
        self.assertEqual("*  *  *\n*  H  *\n*  *  *\n", test.__str__(), "Check string for health potions")

    def test_vision_potion_string(self):
        test = Room(vision_potion=1, contents="V")
        self.assertEqual("*  *  *\n*  V  *\n*  *  *\n", test.__str__(), "Check string for vision potions")

    def test_exit_string(self):
        test = Room(contents="O")
        self.assertEqual("*  *  *\n*  O  *\n*  *  *\n", test.__str__(), "Check string for exit")

    def test_entrance_string(self):
        test = Room(contents="i")
        self.assertEqual("*  *  *\n*  i  *\n*  *  *\n", test.__str__(), "Check string for exit")

    def test_clear_room(self):
        test = Room(contents="i")
        test.clear_room()
        empty_room = Room()
        self.assertEqual(f"{empty_room}", f"{test}", "Check if room is clearing properly.")

    def test_remove_HP_potions_contents(self):
        test = Room(health_potion=1)
        test.health_potion = 0
        self.assertEqual(" ", test.contents, "Room contents should be open after removing potion.")

    def test_remove_HP_potions(self):
        test = Room(health_potion=1)
        test.health_potion = 0
        self.assertEqual(0, test.health_potion, "Health potions should be nothing.")

    def test_remove_vision_potions(self):
        test = Room(vision_potion=1)
        test.vision_potion = 0
        self.assertEqual(" ", test.contents, "Room contents should be clear after removing potion.")

    def test_remove_hp_potion_still_pit(self):
        test = Room(health_potion=1, monster=10)
        test.health_potion = 0
        self.assertEqual("X", test.contents, "Room should have a pit still.")

    def test_remove_vision_potion_still_pit(self):
        test = Room(vision_potion=1, monster=10)
        test.vision_potion = 0
        self.assertEqual("X", test.contents, "Room should have a pit still.")

    def test_remove_vision_potion_still_hp_and_pit(self):
        test = Room(health_potion=1, vision_potion=1, monster=10)
        test.vision_potion = 0
        self.assertEqual("M", test.contents, "Should still have multiple - HP potion and pit, after removing vision")

    def test_remove_hp_potion_still_vision_and_pit(self):
        test = Room(health_potion=1, vision_potion=1, monster=10)
        test.health_potion = 0
        self.assertEqual("M", test.contents, "Should still have multiple - HP potion and pit, after removing vision")

    def test_get_door_invalid_key(self):
        test = Room()
        test.set_door("east", True)
        try:
            test.get_door("Joy")
            self.assertEqual(True, False, "Expected KeyError with invalid key")
        except KeyError:
            self.assertEqual(True, True)

    def test_set_door_invalid_key(self):
        test = Room()
        try:
            test.set_door(0, True)
            self.assertEqual(True, False, "Expected KeyError with invalid key")
        except KeyError:
            self.assertEqual(True, True)

    def test_json_dict(self):
        test = Room(monster=self._ogre, contents="X")
        self.assertEqual({'health': 0, 'vision': 0, 'monster': {'attack_speed': 2,
             'current_hp': 200,
             'heal_chance': 0.1,
             'hit_chance': 0.6,
             'max_dmg': 60,
             'max_heal': 60,
             'max_hp': 200,
             'min_dmg': 30,
             'min_heal': 30,
             'name': 'Ogre'}, 'north': False, 'east': False, 'south': False,
                          'west': False, 'contents': 'X'}, test.json_dict(), "Verify dict converstion successful")

    def test_doors(self):
            test = Room()
            test.set_door("east", True)
            expected = {"east": True,'north': False, "south": False, "west": False }
            self.assertDictEqual(expected, test.doors, "Check that doors dict presented as expected")