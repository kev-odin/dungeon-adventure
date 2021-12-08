from potion_factory import PotionFactory
import unittest

class PotionFactoryTest(unittest.TestCase):
    def test_create_health_potion(self):
        test_health = PotionFactory.create_potion("health")
        self.assertEqual(test_health.name, "Health Potion")
    
    def test_create_vision_potion(self):
        test_vision = PotionFactory.create_potion("vision")
        self.assertEqual(test_vision.name, "Vision Potion")
