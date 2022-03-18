import sqlite3
import os.path


class QueryHelper:
    def __init__(self):
        """
        Query Helper assists with all your dungeon querying needs from monsters to difficulty settings to classes!
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._db_path = os.path.join(base_dir, "app.db")
        self._con = None
        self._cur = None

    def _select_query(self, sql_select_query, value=None):
        """
        If there's a value, queries for a specific value within the
        :param sql_select_query: valid SELECT query for sqlite including valid table name.
        :param value: Optional, specific value within a table that's being searched for.
        :return: Records and matching table column names for specific search if applicable (value only search)
        """
        self._connect()
        keys = []
        if value:
            self._cur.execute(sql_select_query, (value,))
            col_names = self._cur.description
            for row in col_names:
                keys.append(row[0])
        else:
            self._cur.execute(sql_select_query)
        records = self._cur.fetchall()
        self._disconnect()
        return records, keys

    @staticmethod
    def _build_dictionary(keys: tuple, records: tuple):
        """
        Builds a dictionary from given keys to matching records.
        :param keys: tuple representing keys / column names in database table
        :param records: values inside the database column for a single row.
        :return: Dictionary of key-value pairs.
        """
        record_dict = {}
        for i, value in enumerate(records):
            record_dict[keys[i]] = value
        return record_dict

    def _connect(self):
        """
        Connects to database and sets cursor.
        """
        self._con = sqlite3.connect(self._db_path)
        self._cur = self._con.cursor()

    def _disconnect(self):
        """
        Disconnects from database.
        """
        self._con.close()
        self._con = None
        self._cur = None

    @property
    def cursor(self):
        return self._cur

    @property
    def console(self):
        return self._con

    def query(self, target: str):
        """
        Queries the dng_diff table, returning a dictionary.
        :param target: must be a string in the 'difficulty' column of dng_diff table, name in classes table,
            or name in monsters table.  'easy', 'medium', 'hard', 'inhumane'.  'Ogre', 'Gremlin', 'Skeleton', or
            'Thief', 'Priestess', 'Warrior'.
        :return: dict of values for defaults queried, with keys as table names and values as value.
        """
        sql_select_query = ("""SELECT difficulty FROM dng_diff""", """SELECT name FROM monsters""",
                            """SELECT adv_class FROM classes""")
        diff_options = self._select_query(sql_select_query[0])
        monster_options = self._select_query(sql_select_query[1])
        class_options = self._select_query(sql_select_query[2])
        if target in str(diff_options[0]):
            sql_select_query = """SELECT * FROM dng_diff where difficulty = ?"""
        elif target in str(monster_options[0]):
            sql_select_query = """SELECT * FROM monsters where name = ?"""
        elif target in str(class_options[0]):
            sql_select_query = """SELECT * FROM classes where adv_class = ?"""
        else:
            raise KeyError(f"{target} is not a valid query.")
        values, keys = self._select_query(sql_select_query, target)
        return self._build_dictionary(keys, values[0])

    def save_game(self, save_data: dict):
        """
        Saves game in saves table with save_data.  Varifies keys required in dict.
        :param save_data: dict, timestamp - str, hero_name - str, class - str, difficulty - str, current_hp - int,
            max_hp - int, dungeon - json string, adventurerer - json string, save_data - json string.
        """
        keys = {"timestamp", "hero_name","class", "difficulty", "current_hp", "max_hp", "dungeon", "adventurer", "map"}
        for key in keys:
            if key not in save_data:
                assert KeyError(f"Missing key {key} from save dictionary.")
        self._connect()
        sql_insert = """INSERT INTO saves VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        self._cur.execute(sql_insert, (save_data["timestamp"], save_data["hero_name"], save_data["class"],
                                       save_data["difficulty"], save_data["current_hp"], save_data["max_hp"],
                                       save_data["dungeon"], save_data["adventurer"], save_data["map"]))
        self._con.commit()
        self._disconnect()

    def query_saves(self, time=None):
        if time is None:
            sql_select_query = """SELECT timestamp, hero_name, class, difficulty, current_hp, max_hp FROM saves"""
            records, keys = self._select_query(sql_select_query)
            keys = ("timestamp", "hero_name", "class", "difficulty", "current_hp", "max_hp")
            collection = []
            for record in records:
                collection.append(self._build_dictionary(keys, record))
            return collection
        else:
            sql_select_query="""SELECT dungeon, adventurer, map FROM saves WHERE timestamp = ?"""
            records, keys = self._select_query(sql_select_query, time)
            keys = ("dungeon", "adventurer", "map")
            dict = self._build_dictionary(keys, records[0])
            return dict

