# Kevin's Time Tracker: 1 hour

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
            self.assertRaises(TypeError)

    def test_init_toString(self):
        """Test for str dunder method for the Adventure class
        """
        hero = Adventurer('Bob')
        expected = f'Name: {hero.name}\nHP: {hero.hitpoints}\nHealth potions: {hero.health_pots}\nVision potions: {hero.vision_pots}\nPillars collected: {hero.pillars}'
        self.assertEqual(expected, hero.__str__())

    def test_set_negative_health(self):
        try:
            hero = Adventurer('Bob')
            hero.hitpoints = -1
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
            