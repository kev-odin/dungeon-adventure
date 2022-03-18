import json
from datetime import datetime
from app.model.db.query_helper import QueryHelper

class SaveManager:
    """
    Saves the game!  Loads the game!  Games the game.
    """
    @staticmethod
    def save(dungeon_dict: dict, adventurer_dict: dict, map_dict: dict):
        """
        Sets up dictionary to send to queryhelper to save the game.
        :param dungeon_dict: dict representing dungeon with every object inside stored as a dict.
        :param adventurer_dict: dict representing the adventurer.  Just basic char_dict
        :param map_dict: dict representing the map.
        :return: True if no errors occurred while attempting to save.  False if an error occurred and save failed.
        """
        save_dict = {}
        current_time = str(datetime.now())
        save_dict["timestamp"] = current_time  # How we will query for saves to load.
        save_dict["hero_name"] = adventurer_dict["name"]
        save_dict["class"] = adventurer_dict["adv_class"]
        save_dict["difficulty"] = dungeon_dict["difficulty"]
        save_dict["current_hp"] = adventurer_dict["current_hp"]
        save_dict["max_hp"] = adventurer_dict["max_hp"]
        json_adventurer = json.dumps(adventurer_dict)  # Stores as json string for text field in DB
        json_dungeon = json.dumps(dungeon_dict)
        json_map = json.dumps(map_dict)
        save_dict["dungeon"] = json_dungeon
        save_dict["adventurer"] = json_adventurer
        save_dict["map"] = json_map
        qh = QueryHelper()
        try:
            qh.save_game(save_dict)
            return True
        except BaseException:  # Literally anything happened that shouldn't have.
            return False

    @staticmethod
    def get_saved_games():
        """
        Returns a sorted list (by timestamp) of dictionaries of all saved games with "timestamp", "hero_name",
        "class", "difficulty", "current_hp", "max_hp".
        May be just an unnecessary level of complexity since it does literally all the query helper does.
        :return: list of dicts in chronological order.  Oldest saves at the end.
        """
        qh = QueryHelper()
        saves = qh.query_saves()
        return saves

    @staticmethod
    def load(timestamp: str):
        """
        Selects and loads a game based on its timestamp.  Returns the dungeon, adventurerer, and map objects.
        :param timestamp: str matching datetime in saves db.
        :return: tuple (dungeon, adventurerer, map) of dictionaries
        """
        qh = QueryHelper()
        game = qh.query_saves(timestamp)
        game["dungeon"], game["adventurer"], game["map"] = json.loads(game["dungeon"]), json.loads(game["adventurer"]), json.loads(game["map"])
        return game




