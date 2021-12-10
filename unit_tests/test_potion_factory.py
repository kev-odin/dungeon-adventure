# Kevin's Time Tracker: 1 hour

from potion_factory import PotionFactory
from health_potion import HealthPotion
from vision_potion import VisionPotion
import unittest

class PotionFactoryTest(unittest.TestCase):
    def test_create_health_potion(self):
        test_health = PotionFactory.create_potion("health")
        assert isinstance(test_health, HealthPotion)
    
    def test_create_vision_potion(self):
        test_vision = PotionFactory.create_potion("vision")
        assert isinstance(test_vision, VisionPotion)