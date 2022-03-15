"""
WARNING: Tests will heal if Healable inherits from ABC.  These are for testing while writing.  Use caution
"""

from unittest import TestCase
from app.unit_tests.characters_tests.abstract_classes_tests.healable_mock import HealAbleMock


class TestHealAble(TestCase):
    def setUp(self):
        self._heals_maxed = {"current_hp": 100, "max_hp": 100, "min_heal": 10, "max_heal": 20}
        self._heals_5 = {"current_hp": 95, "max_hp": 100, "min_heal": 10, "max_heal": 20}
        self._heals_min_10 = {"current_hp": 5, "max_hp": 100, "min_heal": 10, "max_heal": 20}
        self._healable = HealAbleMock()

    def test__heal_full(self):
        actual = self._healable.heal(self._heals_maxed)
        self.assertEqual(0, actual, "Should heal 0 when already full health.")

    def test__heal_5(self):
        actual = self._healable.heal(self._heals_5)
        self.assertEqual(5, actual, "Should heal 5 to max health.")

    def test__heal_min_10(self):
        actual = self._healable.heal(self._heals_min_10)
        self.assertGreaterEqual(actual, 10, "Should heal 10 minimum.")