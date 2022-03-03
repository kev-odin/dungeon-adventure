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

    # def test_load(self):
    #     self.fail()
