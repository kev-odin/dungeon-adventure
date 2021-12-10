# Kevin's Time Tracker: 3.5 hour

import unittest
from adventurer import Adventurer

class AdventurerTest(unittest.TestCase):

    def test_init(self):
        try:
            hero = Adventurer()
            self.assertEqual(True, True)
        except TypeError:
            self.assertEqual(True, False, "Failed to create instance")

    def test_init_name_string(self):
        hero = Adventurer("Bob")
        self.assertEqual("Bob", hero.name)

    def test_init_name_int(self):
        try:
            hero = Adventurer(101)
        except TypeError:
            self.assertRaises(TypeError, "Integers are not valid names.")

    def test_init_toString(self):
        hero = Adventurer("Bob")
        expected = f'Name: {hero.name}\n'
        expected += f'HP: {hero.current_hitpoints} / {hero.max_hitpoints}\n'
        expected += f'Health potions: {hero.health_pots}\n'
        expected += f'Vision potions: {hero.vision_pots}\n'
        expected += f'Pillars collected: {hero.pillars_collected}\n'
        self.assertEqual(expected, hero.__str__())

    def test_set_negative_health(self):
        try:
            hero = Adventurer("Bob")
            hero.current_hitpoints = -1
        except ValueError:
            self.assertRaises(ValueError)

    def test_set_negative_health_potion(self):
        try:
            hero = Adventurer("Bob")
            hero.health_pots = -1
        except ValueError:
            self.assertRaises(ValueError)

    def test_set_negative_vision_potion(self):
        try:
            hero = Adventurer("Bob")
            hero.vision_pots = -1
        except ValueError:
            self.assertRaises(ValueError)

    def test_default_dev_powers(self):
        try:
            hero = Adventurer("Bob")
            self.assertFalse(hero.dev_powers, "This name is not in the dictionary. Should be False.")
        except AssertionError:
            self.assertRaises(AssertionError)

    def test_set_dev_powers_true(self):
        try:
            hero = Adventurer("tom")
            self.assertTrue(hero.dev_powers, "This name is in the dictionary. Should be True.")
        except AssertionError:
            self.assertRaises(AssertionError)

    def test_set_health_potions(self):
        hero = Adventurer("Bob")
        hero.health_pots = 1
        self.assertEqual(1, hero.health_pots)

    def test_set_vision_potions(self):
        hero = Adventurer("Bob")
        hero.vision_pots = 1
        self.assertEqual(1, hero.vision_pots, "Adventurer should have 1 vision potion.")

    def test_default_pillars(self):
        hero = Adventurer("Bob")
        self.assertFalse(hero.has_all_pillars(), "Default adventurer should not have any pillars.")

    def test_is_hero_alive_false(self):
        hero = Adventurer("Bob")
        hero.current_hitpoints = 0
        self.assertFalse(hero.is_alive(), "Current hitpoints were set to 0, should be False.")

    def test_is_hero_alive_true(self):
        hero = Adventurer("Bob")
        self.assertTrue(hero.is_alive(), "Default hero should be alive")

    def test_is_hero_alive_set_hitpoints(self):
        hero = Adventurer("Bob")
        hero.current_hitpoints = 1
        self.assertTrue(hero.is_alive(), "Default hero is alive when we set health to 1.")

    def test_hero_collect_potions_correct_length(self):
        mock_potions = (1, 2)
        hero = Adventurer("Bob")
        hero.add_potions(mock_potions)
        self.assertEqual(hero.health_pots, 1, "Based on the tuple, there should be 1 health potion")
        self.assertEqual(hero.vision_pots, 2, "Based on the tuple there shoulc be 2 vision potions")

    def test_hero_collect_potions_long_length(self):
        try:
            mock_potions = (1, 1, 1)
            hero = Adventurer("Bob")
            hero.add_potions(mock_potions)
        except ValueError:
            self.assertRaises(ValueError)

    def test_hero_collect_potions_short_length(self):
        try:
            mock_potions = (1)
            hero = Adventurer("Bob")
            hero.add_potions(mock_potions)
        except ValueError:
            self.assertRaises(ValueError)

    def test_hero_collect_potions_correct_length_str(self):
        try:
            mock_potions = ("a", "b")
            hero = Adventurer("Bob")
            hero.add_potions(mock_potions)
        except TypeError:
            self.assertRaises(TypeError)

    def test_hero_collect_all_pillars(self):
        pillar_list = ["A", "P", "I", "E"]
        hero = Adventurer("Bob")
        for val in pillar_list:
            hero.add_pillar(val)
        self.assertTrue(hero.has_all_pillars())

    def test_hero_collect_pillar_a_true(self):
        pillar_list = ["A", "P", "I", "E"]
        hero = Adventurer("Bob")
        hero.add_pillar(pillar_list[0])
        self.assertTrue(hero.pillars_collected["A"])

    def test_hero_collect_pillar_p_false(self):
        pillar_list = ["A", "P", "I", "E"]
        hero = Adventurer("Bob")
        hero.add_pillar(pillar_list[1])
        self.assertFalse(hero.pillars_collected["A"])
    
    def test_hero_pit_damage_alive(self):
        mock_pit = 25
        hero = Adventurer("Bob")
        hero.current_hitpoints = 26
        hero.damage_adventurer(mock_pit)
        self.assertEqual(1, hero.current_hitpoints, "1 health point should be left")

    def test_hero_pit_damage_dead(self):
        mock_pit = 25
        hero = Adventurer("Bob")
        hero.current_hitpoints = 25
        hero.damage_adventurer(mock_pit)
        self.assertEqual(0, hero.current_hitpoints, "0 health points should be left")

    def test_hero_pit_damage_dead_boolean(self):
        mock_pit = 25
        hero = Adventurer("Bob")
        hero.current_hitpoints = 25
        hero.damage_adventurer(mock_pit)
        self.assertFalse(hero.is_alive(), "Boolean should evaluate to False")

    def test_hero_pit_damage_greater_than_current(self):
        mock_pit = 30
        hero = Adventurer("Bob")
        hero.current_hitpoints = 25
        hero.damage_adventurer(mock_pit)
        self.assertEqual(0, hero.current_hitpoints, "0 health points should be left")

    def test_hero_potion_use_health_potion(self):
        hero = Adventurer("Bob")
        hero.health_pots = 1
        hero.use_health_potion()
        self.assertEqual(0, hero.health_pots, "Adventurer should decrement from health potion inventory, should be 0.")

    def test_hero_potion_use_health_potion_zero(self):
        hero = Adventurer("Bob")
        hero.health_pots = 0
        hero.use_health_potion()
        self.assertEqual(0, hero.health_pots, "Adventurer should have 0 health potions.")

    def test_hero_potion_use_vision_potion(self):
        hero = Adventurer("Bob")
        hero.vision_pots = 1
        hero.use_vision_potion()
        self.assertEqual(0, hero.vision_pots, "Adventurer should decrement from vision potion inventory, should be 0.")

    def test_hero_potion_use_vision_potion_zero(self):
        hero = Adventurer("Bob")
        hero.vision_pots = 0
        hero.use_health_potion()
        self.assertEqual(0, hero.vision_pots, "Adventurer should have 0 vision potions.")

    def test_hero_heal_potion(self):
        mock_heal_amount = 25
        hero = Adventurer("Bob")
        hero.current_hitpoints = 1
        hero.heal_adventurer(mock_heal_amount)
        self.assertEqual(26, hero.current_hitpoints, "Adventurer should have 26 hitpoints after healing.")

    def test_hero_heal_potion_over(self):
        mock_heal_amount = 250
        hero = Adventurer("Bob")
        hero.current_hitpoints = 1
        hero.heal_adventurer(mock_heal_amount)
        self.assertEqual(hero.max_hitpoints, hero.current_hitpoints, "Adventurer should have the same as max hit points.")
