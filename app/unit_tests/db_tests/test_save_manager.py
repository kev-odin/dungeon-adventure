from unittest import TestCase
from app.model.db.save_manager import SaveManager
from app.model.dungeon.dungeon_builder import DungeonBuilder


class TestSaveManager(TestCase):
    def setUp(self) -> None:
        db = DungeonBuilder()
        self._dungeon = db.build_dungeon("Easy")
        self._adventurer = db.build_adventurer("Pineapple", "Priestess")
        self._map = db.map.map_dict
        self._sm = SaveManager()

    def test_save(self):
        dungeon_dict = self._dungeon.json_dict
        adv_dict = self._adventurer.char_dict
        map_dict = self._map
        saved = SaveManager.save(dungeon_dict, adv_dict, map_dict)
        self.assertTrue(saved, "Didn't save - returned an error!")

    def test_get_saved_games(self):
        result = SaveManager.get_saved_games()
        expected = [{'timestamp': '2022-03-01 23:20:08.356245', 'hero_name': 'Pineapple', 'class': 'Priestess',
                     'difficulty': 'Easy', 'current_hp': 75, 'max_hp': 75},
                    {'timestamp': '2022-03-02 20:44:43.084837', 'hero_name': 'Kevin', 'class': 'Warrior',
                     'difficulty': 'Easy', 'current_hp': 125, 'max_hp': 125},
                    {'timestamp': '2022-03-02 20:46:12.675624', 'hero_name': 'Xingguo the Knower of Things',
                     'class': 'Thief', 'difficulty': 'Easy', 'current_hp': 75, 'max_hp': 75}]
        for item in expected:
            if item not in result:
                self.fail(f"{item} is missing from database save query")
        self.assertTrue(True, "Everything loaded properly so why is this showing?!")

    def test_load(self):
        timestamp = "2022-03-01 23:20:08.356245"
        result = SaveManager.load(timestamp)
        expected= {'dungeon': {'dungeon': [[{'health': 0, 'vision': 0, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': False, 'contents': ' '}, {'health': 0, 'vision': 0, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': False, 'contents': ' '}, {'health': 0, 'vision': 0, 'monster': {'name': 'Ogre', 'max_hp': 200, 'attack_speed': 2, 'hit_chance': 0.6, 'min_dmg': 30, 'max_dmg': 60, 'heal_chance': 0.1, 'min_heal': 30, 'max_heal': 60, 'current_hp': 200}, 'north': False, 'east': True, 'south': False, 'west': False, 'contents': 'E'}, {'health': 0, 'vision': 0, 'monster': None, 'north': False, 'east': True, 'south': True, 'west': True, 'contents': 'i'}, {'health': 0, 'vision': 0, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': True, 'contents': 'O'}], [{'health': 0, 'vision': 0, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': False, 'contents': ' '}, {'health': 0, 'vision': 0, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': False, 'contents': ' '}, {'health': 0, 'vision': 0, 'monster': None, 'north': False, 'east': True, 'south': False, 'west': False, 'contents': ' '}, {'health': 1, 'vision': 0, 'monster': None, 'north': True, 'east': True, 'south': True, 'west': True, 'contents': 'H'}, {'health': 0, 'vision': 0, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': True, 'contents': ' '}], [{'health': 2, 'vision': 0, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': False, 'contents': 'H'}, {'health': 0, 'vision': 0, 'monster': {'name': 'Ogre', 'max_hp': 200, 'attack_speed': 2, 'hit_chance': 0.6, 'min_dmg': 30, 'max_dmg': 60, 'heal_chance': 0.1, 'min_heal': 30, 'max_heal': 60, 'current_hp': 200}, 'north': False, 'east': True, 'south': False, 'west': False, 'contents': 'I'}, {'health': 2, 'vision': 0, 'monster': None, 'north': False, 'east': True, 'south': True, 'west': True, 'contents': 'H'}, {'health': 1, 'vision': 0, 'monster': None, 'north': True, 'east': True, 'south': False, 'west': True, 'contents': 'H'}, {'health': 0, 'vision': 0, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': True, 'contents': ' '}], [{'health': 0, 'vision': 0, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': False, 'contents': ' '}, {'health': 0, 'vision': 0, 'monster': {'name': 'Ogre', 'max_hp': 200, 'attack_speed': 2, 'hit_chance': 0.6, 'min_dmg': 30, 'max_dmg': 60, 'heal_chance': 0.1, 'min_heal': 30, 'max_heal': 60, 'current_hp': 200}, 'north': False, 'east': True, 'south': False, 'west': False, 'contents': 'A'}, {'health': 1, 'vision': 0, 'monster': {'name': 'Gremlin', 'max_hp': 70, 'attack_speed': 5, 'hit_chance': 0.8, 'min_dmg': 15, 'max_dmg': 30, 'heal_chance': 0.4, 'min_heal': 20, 'max_heal': 40, 'current_hp': 70}, 'north': True, 'east': True, 'south': True, 'west': True, 'contents': 'M'}, {'health': 0, 'vision': 0, 'monster': {'name': 'Ogre', 'max_hp': 200, 'attack_speed': 2, 'hit_chance': 0.6, 'min_dmg': 30, 'max_dmg': 60, 'heal_chance': 0.1, 'min_heal': 30, 'max_heal': 60, 'current_hp': 200}, 'north': False, 'east': False, 'south': False, 'west': True, 'contents': 'P'}, {'health': 0, 'vision': 0, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': False, 'contents': ' '}], [{'health': 0, 'vision': 0, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': False, 'contents': ' '}, {'health': 0, 'vision': 2, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': False, 'contents': 'V'}, {'health': 0, 'vision': 0, 'monster': None, 'north': True, 'east': False, 'south': False, 'west': False, 'contents': ' '}, {'health': 0, 'vision': 0, 'monster': {'name': 'Skeleton', 'max_hp': 100, 'attack_speed': 3, 'hit_chance': 0.8, 'min_dmg': 30, 'max_dmg': 50, 'heal_chance': 0.3, 'min_heal': 30, 'max_heal': 50, 'current_hp': 100}, 'north': False, 'east': False, 'south': False, 'west': False, 'contents': 'X'}, {'health': 1, 'vision': 0, 'monster': None, 'north': False, 'east': False, 'south': False, 'west': False, 'contents': 'H'}]], 'difficulty': 'Easy', 'rows': 5, 'cols': 5, 'pillars': ['A', 'P', 'I', 'E'], 'entrance': [0, 3], 'exit': [0, 4], 'adventurer_location': [0, 3]}, 'adventurer': {'adv_class': 'Priestess', 'max_hp': 75, 'attack_speed': 5, 'hit_chance': 0.7, 'min_dmg': 25, 'max_dmg': 45, 'block_chance': 0.3, 'special': 'Heal', 'current_hp': 75, 'name': 'Pineapple', 'max_heal': 75, 'min_heal': 18, 'health_pots': 0, 'vision_pots': 0, 'pillars_collected': {'A': False, 'P': False, 'I': False, 'E': False}}, 'map': {'rows': 5, 'cols': 5, 'visited_array': [[False, False, False, True, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]}}
        self.assertDictEqual(expected, result, "Verify results converted to dictionary properly.")

