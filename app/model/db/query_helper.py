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

    def query(self, target: str):
        """
        Queries the dng_diff table, returning a dictionary.
        :param target: must be a string in the 'difficulty' column of dng_diff table, name in classes table,
            or name in monsters table.  'easy', 'medium', 'hard', 'inhumane'.  'Ogre', 'Gremlin', 'Skeleton', or
            'Thief', 'Priestess', 'Warrior'.
        :return: dict of values for defaults queried, with keys as table names and values as value.
        """
        sql_select_query = ("""SELECT difficulty FROM dng_diff""", """SELECT name FROM monsters""",
                            """SELECT name FROM classes""")
        diff_options = self._select_query(sql_select_query[0])
        monster_options = self._select_query(sql_select_query[1])
        class_options = self._select_query(sql_select_query[2])
        if target in str(diff_options[0]):
            sql_select_query = """SELECT * FROM dng_diff where difficulty = ?"""
        elif target in str(monster_options[0]):
            sql_select_query = """SELECT * FROM monsters where name = ?"""
        elif target in str(class_options[0]):
            sql_select_query = """SELECT * FROM classes where name = ?"""
        else:
            raise KeyError(f"{target} is not a valid query.")
        values, keys = self._select_query(sql_select_query, target)
        return self._build_dictionary(keys, values[0])

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
