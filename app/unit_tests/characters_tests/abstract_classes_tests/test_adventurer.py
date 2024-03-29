"""
WARNING: Only works when adventurer is not current set to have abstract method use_special
Otherwise the abstract class says nope.
"""


import unittest
from app.unit_tests.characters_tests.abstract_classes_tests.adventurer_mock import AdventurerMock
from app.model.items.health_potion import HealthPotion
from app.model.db.query_helper import QueryHelper


class AdventurerTest(unittest.TestCase):
    def setUp(self, name="Bob", adv_class="Warrior") -> None:
        self.__qh = QueryHelper()
        hero_dict = self.__qh.query("Warrior")
        hero_dict["current_hp"] = hero_dict["max_hp"]
        hero_dict["name"] = name
        if "health_pots" not in hero_dict:  # Checks for new creation of adventurerer or load of adventurer
            hero_dict["health_pots"] = 0
            hero_dict["vision_pots"] = 0
            hero_dict["pillars_collected"] = {
                "A": False,
                "P": False,
                "I": False,
                "E": False
            }
        self.__adv_dict = hero_dict
        self.__hero = AdventurerMock(self.__adv_dict)

    def test_init(self):
        try:
            self.setUp()
            self.assertEqual(True, True)
        except TypeError:
            self.assertEqual(True, False, "Failed to create instance")

    def test_init_name_string(self):
        self.assertEqual("Bob", self.__hero.name)

    def test_init_name_int(self):
        try:
            hero = AdventurerMock(101, "Warrior")
        except TypeError:
            self.assertRaises(TypeError, "Integers are not valid names.")

    def test_init_str(self):
        hero = self.__hero
        expected = f'Name: {hero.name}\n'
        expected += f'HP: {hero.current_hitpoints} / {hero.max_hitpoints}\n'
        expected += f'Health potions: {hero.health_pots}\n'
        expected += f'Vision potions: {hero.vision_pots}\n'
        expected += f'Object Oriented Pillars Collected\n{hero._readable_pillars()}\n'
        self.assertEqual(expected, hero.__str__())

    def test_init_repr(self):
        hero = self.__hero
        expected = f"{hero.name}\n"
        expected += f"{hero.current_hitpoints} / {hero.max_hitpoints}\n"
        expected += f"{hero.health_pots}\n"
        expected += f"{hero.vision_pots}\n"
        expected += f"{hero.pillars_collected}\n"
        self.assertEqual(expected, hero.__repr__())

    def test_set_negative_health(self):
        try:
            hero = self.__hero
            hero.current_hitpoints = -1
        except ValueError:
            self.assertRaises(ValueError)

    def test_set_negative_health_potion(self):
        try:
            hero = self.__hero
            hero.health_pots = -1
        except ValueError:
            self.assertRaises(ValueError)

    def test_set_negative_vision_potion(self):
        try:
            self.__hero.vision_pots = -1
        except ValueError:
            self.assertRaises(ValueError)

    def test_set_health_potions(self):
        self.__hero.health_pots = 1
        self.assertEqual(1, self.__hero.health_pots)

    def test_set_vision_potions(self):
        self.__hero.vision_pots = 1
        self.assertEqual(1, self.__hero.vision_pots, "Adventurer should have 1 vision potion.")

    def test_default_pillars(self):
        self.assertFalse(self.__hero.has_all_pillars(), "Default adventurer should not have any pillars.")

    def test_is_hero_alive_false(self):
        hero = self.__hero
        hero.current_hitpoints = 0
        self.assertFalse(hero.is_alive(), "Current hitpoints were set to 0, should be False.")

    def test_is_hero_alive_true(self):
        hero = self.__hero
        self.assertTrue(hero.is_alive(), "Default hero should be alive")

    def test_is_hero_alive_set_hitpoints(self):
        hero = self.__hero
        hero.current_hitpoints = 1
        self.assertTrue(hero.is_alive(), "Default hero is alive when we set health to 1.")

    def test_hero_collect_potions_correct_length(self):
        mock_potions = (1, 2)
        hero = self.__hero
        hero.health_pots = 0
        hero.vision_pots = 0
        hero.add_potions(mock_potions)
        self.assertEqual(hero.health_pots, 1, "Based on the tuple, there should be 1 health potion")
        self.assertEqual(hero.vision_pots, 2, "Based on the tuple there shoulc be 2 vision potions")

    def test_hero_collect_potions_long_length(self):
        try:
            mock_potions = (1, 1, 1)
            hero = self.__hero
            hero.add_potions(mock_potions)
        except ValueError:
            self.assertRaises(ValueError)

    def test_hero_collect_potions_short_length(self):
        try:
            mock_potions = (1,)
            hero = self.__hero
            hero.add_potions(mock_potions)
        except ValueError:
            self.assertRaises(ValueError)

    def test_hero_collect_potions_correct_length_str(self):
        try:
            mock_potions = ("a", "b")
            hero = self.__hero
            hero.add_potions(mock_potions)
        except TypeError:
            self.assertRaises(TypeError)

    def test_hero_collect_all_pillars(self):
        pillar_list = ["A", "P", "I", "E"]
        for val in pillar_list:
            self.__hero.add_pillar(val)
        self.assertTrue(self.__hero.has_all_pillars())

    def test_hero_collect_pillar_none(self):
        compare = self.__hero.pillars_collected
        self.__hero.add_pillar(None)
        self.assertEqual(compare, self.__hero.pillars_collected)

    def test_hero_collect_pillar_a_true(self):
        pillar_list = ["A", "P", "I", "E"]
        self.__hero.add_pillar(pillar_list[0])
        self.assertTrue(self.__hero.pillars_collected["A"])

    def test_hero_collect_pillar_p_false(self):
        pillar_list = ["A", "P", "I", "E"]
        self.__hero.add_pillar(pillar_list[1])
        self.assertFalse(self.__hero.pillars_collected["A"])

    def test_hero_pit_damage_alive(self):
        mock_pit = 25
        self.__hero.current_hitpoints = 26
        always_hits = True
        self.__hero.take_damage(mock_pit, always_hits)
        self.assertEqual(1, self.__hero.current_hitpoints, "1 health point should be left")

    def test_hero_pit_damage_dead(self):
        mock_pit = 25
        self.__hero.current_hitpoints = 25
        always_hits = True
        self.__hero.take_damage(mock_pit, always_hits)
        self.assertEqual(0, self.__hero.current_hitpoints, "0 health points should be left")

    def test_hero_pit_damage_dead_boolean(self):
        mock_pit = 25
        self.__hero.current_hitpoints = 25
        always_hits = True
        self.__hero.take_damage(mock_pit, always_hits)
        self.assertFalse(self.__hero.is_alive(), "Boolean should evaluate to False")

    def test_hero_pit_damage_greater_than_current(self):
        mock_pit = 30
        self.__hero.current_hitpoints = 25
        self.__hero.take_damage(mock_pit, True)
        self.assertEqual(0, self.__hero.current_hitpoints, "0 health points should be left")

    def test_hero_potion_has_health_potion(self):
        self.__hero.health_pots = 1
        self.__hero.has_health_potion()
        self.assertEqual(0, self.__hero.health_pots, "Adventurer should decrement from health potion inventory, should be 0.")

    def test_hero_potion_has_health_potion_zero(self):
        self.__hero.health_pots = 0
        self.__hero.has_health_potion()
        self.assertEqual(0, self.__hero.health_pots, "Adventurer should have 0 health potions.")

    def test_hero_potion_has_vision_potion(self):
        self.__hero.vision_pots = 1
        self.__hero.has_vision_potion()
        self.assertEqual(0, self.__hero.vision_pots, "Adventurer should decrement from vision potion inventory, should be 0.")

    def test_hero_potion_has_vision_potion_zero(self):
        self.__hero.vision_pots = 0
        self.__hero.has_health_potion()
        self.assertEqual(0, self.__hero.vision_pots, "Adventurer should have 0 vision potions.")

    def test_hero_potion_has_health_potion_true(self):
        self.__hero.health_pots = 1
        self.assertTrue(self.__hero.has_health_potion())

    def test_hero_potion_has_health_potion_false(self):
        self.__hero.health_pots = 0
        self.assertFalse(self.__hero.has_health_potion())

    def test_hero_potion_has_vision_potion_true(self):
        self.__hero.vision_pots = 1
        self.assertTrue(self.__hero.has_vision_potion())

    def test_hero_potion_has_vision_potion_false(self):
        self.__hero.vision_pots = 0
        self.assertFalse(self.__hero.has_vision_potion())

    def test_hero_heal_potion(self):
        mock_potion = HealthPotion(random=False)
        mock_potion.heal_amount = 25
        self.__hero.current_hitpoints = 1
        self.__hero.heal_adventurer(mock_potion)
        self.assertEqual(26, self.__hero.current_hitpoints, "Adventurer should have 26 hitpoints after healing.")

    def test_hero_heal_potion_over(self):
        mock_potion = HealthPotion(random=False)
        mock_potion.heal_amount = 250
        self.__hero.current_hitpoints = 1
        self.__hero.heal_adventurer(mock_potion)
        self.assertEqual(self.__hero.max_hitpoints, self.__hero.current_hitpoints, "Adventurer should have the same as max hit points.")

    def test_hero_pillar_a_active(self):
        # Double all health potions collected
        hero = self.__hero
        hero.health_pots = 0
        hero.vision_pots = 0
        hero.add_pillar("A")
        potion_collect = (1, 2)
        hero.add_potions(potion_collect)
        self.assertEqual(hero.health_pots, 2)
        self.assertEqual(hero.vision_pots, 2)

    def test_hero_pillar_p_active(self):
        # Double all vision potions collected
        hero = self.__hero
        hero.health_pots = 0
        hero.vision_pots = 0
        hero.add_pillar("P")
        potion_collect = (1, 2)
        hero.add_potions(potion_collect)
        self.assertEqual(hero.health_pots, 1)
        self.assertEqual(hero.vision_pots, 4)

    def test_hero_pillar_i_active(self):
        # Reduce pit damage
        hero = self.__hero
        hero.max_hitpoints = 100
        hero.current_hitpoints = 100
        hero.add_pillar("I")
        mock_pit_damage = 100
        expected = 50
        hero.take_damage(mock_pit_damage, True)
        self.assertEqual(expected, hero.current_hitpoints)

    def test_hero_pillar_e_active(self):
        # Increases healing hitpoints
        hero = self.__hero
        mock_potion = HealthPotion(random=False)
        mock_potion.heal_amount = 15
        hero.max_hitpoints = 60
        hero.current_hitpoints = 30
        hero.add_pillar("E")
        hero.heal_adventurer(mock_potion)
        self.assertEqual(60, hero.current_hitpoints)

    def test_hero_pillar_all_active(self):
        # Increases healing hitpoints
        hero = self.__hero
        mock_potion = HealthPotion(random=False)
        pillar_list = ["A", "P", "I", "E"]
        for val in pillar_list:
            hero.add_pillar(val)

        mock_potion.heal_amount = 15
        hero.max_hitpoints = 60
        hero.current_hitpoints = 30
        hero.add_pillar("E")
        hero.heal_adventurer(mock_potion)
        self.assertEqual(60, hero.current_hitpoints)
        self.assertEqual(75, hero.max_hitpoints)
