import json
from datetime import datetime
from app.model.db.query_helper import QueryHelper

class SaveManager:
    """
    Saves the game!  Loads the game!  Games the game.
    """
    @staticmethod
    def save(dungeon_dict: dict, adventurer_dict: dict):
        save_dict = {}
        current_time = str(datetime.now())
        save_dict["timestamp"] = current_time
        save_dict["hero_name"] = adventurer_dict["name"]
        save_dict["class"] = adventurer_dict["adv_class"]
        save_dict["difficulty"] = dungeon_dict["difficulty"]
        save_dict["current_hp"] = adventurer_dict["current_hp"]
        save_dict["max_hp"] = adventurer_dict["max_hp"]
        json_adventurer = json.dumps(adventurer_dict)
        json_dungeon = json.dumps(dungeon_dict)
        save_dict["dungeon"] = json_dungeon
        save_dict["adventurer"] = json_adventurer
        qh = QueryHelper()
        try:
            qh.save_game(save_dict)
            return True
        except BaseException:
            return False



    def load(self):
        pass


