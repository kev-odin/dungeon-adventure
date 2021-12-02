"""
Steph Time Tracker:
30 minutes, 15 to write this, 15 to test
"""

from collections.abc import Iterator


class DungeonIterator(Iterator):
    def __init__(self, dungeon, row: int, col: int, row_count: int, col_count: int, access_only=False) -> None:
        self._collection = dungeon
        self._access_only = access_only
        self._position = row * col_count + col
        self._row = row
        self._col = col
        self._row_count = row_count
        self._col_count = col_count

    def __next__(self):
        try:
            current_room = self._collection[self._row][self._col]
            self.__increment()
        except IndexError:
            raise StopIteration()
        return current_room

    def __increment(self):
        if not self._access_only:
            self._col += 1
            if self._col >= self._col_count:
                self._col = 0
                self._row += 1

        if self._access_only:  ### TODO Write iteration code for only accessible areas.
            pass

