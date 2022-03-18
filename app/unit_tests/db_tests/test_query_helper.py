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
        self.assertEqual(['name', 'max_hp', 'attack_speed', 'hit_chance', 'min_dmg', 'max_dmg', 'heal_chance', 'min_heal',
                          'max_heal'], keys, "Verify keys loaded properly in query values.")

    def test__build_dictionary(self):
        expected = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
        result = self.qh._build_dictionary((0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
        self.assertDictEqual(expected, result, "Dictionaries should match after built.")

    def test_query_saves(self):
        result = self.qh.query_saves()
        expected = [{'timestamp': '2022-03-01 23:20:08.356245', 'hero_name': 'Pineapple', 'class': 'Priestess', 'difficulty': 'Easy', 'current_hp': 75, 'max_hp': 75},
                    {'timestamp': '2022-03-02 20:44:43.084837', 'hero_name': 'Kevin', 'class': 'Warrior', 'difficulty': 'Easy', 'current_hp': 125, 'max_hp': 125},
                    {'timestamp': '2022-03-02 20:46:12.675624', 'hero_name': 'Xingguo the Knower of Things', 'class': 'Thief', 'difficulty': 'Easy', 'current_hp': 75, 'max_hp': 75}]
        for item in expected:
            if item not in result:
                self.fail(f"{item} is missing from database save query")
        self.assertTrue(True, "Everything loaded properly so why is this showing?!")

    def test_query_saves_with_timestamp(self):
        timestamp = "2022-03-01 23:20:08.356245"
        game = self.qh.query_saves(timestamp)
        print(game)
        expected = {'dungeon': '{"dungeon": [[{"health": 0, "vision": 0, "monster": null, "north": false, "east": false, "south": false, "west": false, "contents": " "}, {"health": 0, "vision": 0, "monster": null, "north": false, "east": false, "south": false, "west": false, "contents": " "}, {"health": 0, "vision": 0, "monster": {"name": "Ogre", "max_hp": 200, "attack_speed": 2, "hit_chance": 0.6, "min_dmg": 30, "max_dmg": 60, "heal_chance": 0.1, "min_heal": 30, "max_heal": 60, "current_hp": 200}, "north": false, "east": true, "south": false, "west": false, "contents": "E"}, {"health": 0, "vision": 0, "monster": null, "north": false, "east": true, "south": true, "west": true, "contents": "i"}, {"health": 0, "vision": 0, "monster": null, "north": false, "east": false, "south": false, "west": true, "contents": "O"}], [{"health": 0, "vision": 0, "monster": null, "north": false, "east": false, "south": false, "west": false, "contents": " "}, {"health": 0, "vision": 0, "monster": null, "north": false, "east": false, "south": false, "west": false, "contents": " "}, {"health": 0, "vision": 0, "monster": null, "north": false, "east": true, "south": false, "west": false, "contents": " "}, {"health": 1, "vision": 0, "monster": null, "north": true, "east": true, "south": true, "west": true, "contents": "H"}, {"health": 0, "vision": 0, "monster": null, "north": false, "east": false, "south": false, "west": true, "contents": " "}], [{"health": 2, "vision": 0, "monster": null, "north": false, "east": false, "south": false, "west": false, "contents": "H"}, {"health": 0, "vision": 0, "monster": {"name": "Ogre", "max_hp": 200, "attack_speed": 2, "hit_chance": 0.6, "min_dmg": 30, "max_dmg": 60, "heal_chance": 0.1, "min_heal": 30, "max_heal": 60, "current_hp": 200}, "north": false, "east": true, "south": false, "west": false, "contents": "I"}, {"health": 2, "vision": 0, "monster": null, "north": false, "east": true, "south": true, "west": true, "contents": "H"}, {"health": 1, "vision": 0, "monster": null, "north": true, "east": true, "south": false, "west": true, "contents": "H"}, {"health": 0, "vision": 0, "monster": null, "north": false, "east": false, "south": false, "west": true, "contents": " "}], [{"health": 0, "vision": 0, "monster": null, "north": false, "east": false, "south": false, "west": false, "contents": " "}, {"health": 0, "vision": 0, "monster": {"name": "Ogre", "max_hp": 200, "attack_speed": 2, "hit_chance": 0.6, "min_dmg": 30, "max_dmg": 60, "heal_chance": 0.1, "min_heal": 30, "max_heal": 60, "current_hp": 200}, "north": false, "east": true, "south": false, "west": false, "contents": "A"}, {"health": 1, "vision": 0, "monster": {"name": "Gremlin", "max_hp": 70, "attack_speed": 5, "hit_chance": 0.8, "min_dmg": 15, "max_dmg": 30, "heal_chance": 0.4, "min_heal": 20, "max_heal": 40, "current_hp": 70}, "north": true, "east": true, "south": true, "west": true, "contents": "M"}, {"health": 0, "vision": 0, "monster": {"name": "Ogre", "max_hp": 200, "attack_speed": 2, "hit_chance": 0.6, "min_dmg": 30, "max_dmg": 60, "heal_chance": 0.1, "min_heal": 30, "max_heal": 60, "current_hp": 200}, "north": false, "east": false, "south": false, "west": true, "contents": "P"}, {"health": 0, "vision": 0, "monster": null, "north": false, "east": false, "south": false, "west": false, "contents": " "}], [{"health": 0, "vision": 0, "monster": null, "north": false, "east": false, "south": false, "west": false, "contents": " "}, {"health": 0, "vision": 2, "monster": null, "north": false, "east": false, "south": false, "west": false, "contents": "V"}, {"health": 0, "vision": 0, "monster": null, "north": true, "east": false, "south": false, "west": false, "contents": " "}, {"health": 0, "vision": 0, "monster": {"name": "Skeleton", "max_hp": 100, "attack_speed": 3, "hit_chance": 0.8, "min_dmg": 30, "max_dmg": 50, "heal_chance": 0.3, "min_heal": 30, "max_heal": 50, "current_hp": 100}, "north": false, "east": false, "south": false, "west": false, "contents": "X"}, {"health": 1, "vision": 0, "monster": null, "north": false, "east": false, "south": false, "west": false, "contents": "H"}]], "difficulty": "Easy", "rows": 5, "cols": 5, "pillars": ["A", "P", "I", "E"], "entrance": [0, 3], "exit": [0, 4], "adventurer_location": [0, 3]}',
                    'adventurer': '{"adv_class": "Priestess", "max_hp": 75, "attack_speed": 5, "hit_chance": 0.7, "min_dmg": 25, "max_dmg": 45, "block_chance": 0.3, "special": "Heal", "current_hp": 75, "name": "Pineapple", "max_heal": 75, "min_heal": 18, "health_pots": 0, "vision_pots": 0, "pillars_collected": {"A": false, "P": false, "I": false, "E": false}}',
                    'map': '{"rows": 5, "cols": 5, "visited_array": [[false, false, false, true, false], [false, false, false, false, false], [false, false, false, false, false], [false, false, false, false, false], [false, false, false, false, false]]}'}
        self.assertDictEqual(game, expected, "The queried save is incorrect.  Check it provided a dictionary correctly and correct data..")