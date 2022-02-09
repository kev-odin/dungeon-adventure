# Kevin's Time Tracker: 1.5 hours

from model.items.potion_factory import PotionFactory
from model.items.health_potion import HealthPotion
from model.items.vision_potion import VisionPotion
import unittest

class PotionFactoryTest(unittest.TestCase):
    def test_create_health_potion(self):
        test_health = PotionFactory.create_potion("health")
        self.assertIsInstance(test_health, HealthPotion)
    
    def test_create_vision_potion(self):
        test_vision = PotionFactory.create_potion("vision")
        self.assertIsInstance(test_vision, VisionPotion)

    def test_create_blank_potion(self):
        try:
            test_blank = PotionFactory.create_potion()
        except TypeError:
            self.assertRaises(TypeError)
    
    def test_create_invalid_potion(self):
        try:
            test_invalid = PotionFactory.create_potion("super")
        except ValueError:
            self.assertRaises(ValueError)

    def test_create_numerous_potions(self):
        multiple = ("health", "vision")
        try:
            test_numerous = PotionFactory.create_potion(multiple)
        except TypeError:
            self.assertRaises(TypeError)