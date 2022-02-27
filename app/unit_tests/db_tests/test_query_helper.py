from unittest import TestCase
from app.model.db.query_helper import QueryHelper


class TestQueryHelper(TestCase):
    def setUp(self) -> None:
        self.qh = QueryHelper()

    def test_query(self):
        try:
            self.setUp()
            self.assertEqual(True, True, "Shouldn't see this, things worked!")
        except:  # Way too vague.
            self.assertEqual(True, False, "Something went terribly wrong.  Cannot init QueryHelper.")

    def test__connect(self):
        self.qh._connect()
        if self.qh.cursor:
            self.assertEqual(True, True, "Cursor doesn't exist, failed to connect to DB!")
        else:
            self.fail("Failed to initiate cursor with connection.")

    def test__disconnect(self):
        self.qh._connect()
        self.qh._disconnect()
        if not self.qh.console:
            self.assertEqual(True, True, "Cursor and console disconnected successfully.")
        else:
            self.fail()

    def test__select_query_dng_diff(self):
        sql_select_query = """SELECT difficulty FROM dng_diff"""
        diff_options = self.qh._select_query(sql_select_query)
        self.assertEqual(([('Easy',), ('Medium',), ('Hard',), ('Inhumane',)], []), diff_options)

    def test__select_query_value(self):
        sql_select_query = """SELECT * FROM monsters where name = ?"""
        values, keys = self.qh._select_query(sql_select_query, "Ogre")
        self.assertEqual([('Ogre', 200, 2, 0.6, 30, 60, 0.1, 30, 60)], values, "Check values displayed properly.")
        self.assertEqual(['name', 'hp', 'attack_speed', 'hit_chance', 'min_dmg', 'max_dmg', 'heal_chance', 'min_heal',
                          'max_heal'], keys, "Verify keys loaded properly in query values.")

    def test__build_dictionary(self):
        expected = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
        result = self.qh._build_dictionary((0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
        self.assertDictEqual(expected, result, "Dictionaries should match after built.")
