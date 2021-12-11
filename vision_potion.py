# Kevin's Time Tracker: 2 hours
# We can still figure out how a vision potion can be implemented with this. Or scrap it.

from potion import Potion

class VisionPotion(Potion):
    """Vision potion that an adventurer can use to reveal surrounding rooms.
    """
    def __init__(self):
        self.__name = "Vision Potion"
        self.__rooms_revealed = 8

    def __str__(self):
        return f"Item: {self.name}\nEffect: {self.rooms_revealed} adjacent rooms revealed."

    def action(self):
        return self.rooms_revealed

    @property
    def name(self):
        """Simple getter for the name property.

        :return: Name of potion
        :rtype: str
        """
        return self.__name

    @property
    def rooms_revealed(self):
        """Simple getter for the room revealed property.

        :return: Number of rooms revealed after using a potion.
        :rtype: int
        """
        return self.__rooms_revealed

    @rooms_revealed.setter
    def rooms_revealed(self, value):
        """Simple setter that sets the rooms revealed.

        :param value: Number of rooms revealed by vision potion
        :type value: int
        :raises TypeError: For values that are not the correct type
        """
        if isinstance(value, int):
            self.__rooms_revealed = value
        else:
            raise TypeError("Value passed into method was not an integer value.")
