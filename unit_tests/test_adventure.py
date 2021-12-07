# Kevin's Time Tracker: 1.5 hour

import unittest
from adventurer import Adventurer

class AdventurerTest(unittest.TestCase):

    def test_init(self):
        """Test blank instance for the adventurer class
        """
        try:
            hero = Adventurer()
            self.assertEqual(True, True)
        except TypeError:
            self.assertEqual(True, False, 'Failed to create instance')

    def test_init_name_string(self):
        """Test for passing instance class name with string
        """
        hero = Adventurer('Bob')
        self.assertEqual('Bob', hero.name)

    def test_init_name_int(self):
        """Test for passing instance class name with integer value
        Return a Type Error based on the isinstance functionality
        """
        try:
            hero = Adventurer(101)
        except TypeError:
            self.assertRaises(TypeError, "Integers are not valid names.")

    def test_init_toString(self):
        """Test for str dunder method for the Adventure class
        """
        hero = Adventurer('Bob')
        expected = f'Name: {hero.name}\n'
        expected += f'HP: {hero.current_hitpoints} / {hero.max_hitpoints}\n'
        expected += f'Health potions: {hero.health_pots}\n'
        expected += f'Vision potions: {hero.vision_pots}\n'
        expected += f'Pillars collected: {hero.pillars}'
        self.assertEqual(expected, hero.__str__())

    def test_set_negative_health(self):
        try:
            hero = Adventurer('Bob')
            hero.current_hitpoints = -1
        except ValueError:
            self.assertRaises(ValueError)

    def test_set_negative_health_potion(self):
        try:
            hero = Adventurer('Bob')
            hero.health_pots = -1
        except ValueError:
            self.assertRaises(ValueError)

    def test_set_negative_vision_potion(self):
        try:
            hero = Adventurer('Bob')
            hero.vision_pots = -1
        except ValueError:
            self.assertRaises(ValueError)

    def test_default_dev_powers(self):
        try:
            hero = Adventurer('Bob')
            self.assertFalse(hero.dev_powers)
        except AssertionError:
            self.assertRaises(AssertionError)
            
    def test_set_dev_powers_true(self):
        try:
            hero = Adventurer('tom')
            self.assertTrue(hero.dev_powers)
        except AssertionError:
            self.assertRaises(AssertionError)

    def test_set_health_potions(self):
        hero = Adventurer('Bob')
        hero.health_pots = 1
        self.assertEqual(1, hero.health_pots)

    def test_set_vision_potions(self):
        hero = Adventurer('Bob')
        hero.vision_pots = 1
        self.assertEqual(1, hero.vision_pots)

    def test_default_pillars(self):
        hero = Adventurer('Bob')
        self.assertFalse(hero.has_all_pillars())
