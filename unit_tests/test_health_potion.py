# Kevin's Time Tracker: 2 hours

from health_potion import HealthPotion
import unittest

class HealthPotionTest(unittest.TestCase):
    def test_basic_potion(self):
        test = HealthPotion(random=False)
        self.assertEqual(test.name, "Common Health Potion")

    def test_basic_potion_health(self):
        test = HealthPotion(random=False)
        self.assertEqual(test.heal_amount, 0)

    def test_basic_potion_string(self):
        test = HealthPotion(random=False)
        expected = f"Item: {test.name}\n"
        plural = "s" if test.heal_amount != 1 else ""
        expected += f"Effect: Restores {test.heal_amount} hitpoint{plural}."
        self.assertEqual(expected, test.__str__())
    
    def test_basic_potion_heal_amount(self):
        test = HealthPotion(random=False)
        expected = 0
        self.assertEqual(expected, test.heal_amount)

    def test_basic_potion_action(self):
        test = HealthPotion(random=False)
        expected = 0
        self.assertEqual(expected, test.action())

    def test_basic_potion_set_heal_int(self):
        test = HealthPotion(random=False)
        test.heal_amount = 10
        expected = 10
        self.assertEqual(expected, test.heal_amount)

    def test_basic_potion_set_heal_int_string(self):
        test = HealthPotion(random=False)
        test.heal_amount = 10
        expected = f"Item: {test.name}\n"
        expected += f"Effect: Restores {test.heal_amount} hitpoints."
        self.assertEqual(expected, test.__str__())

    def test_basic_potion_set_heal_string(self):
        try:
            test = HealthPotion(random=False)
            test.heal_amount = "10"
        except TypeError:
            self.assertRaises(TypeError)
