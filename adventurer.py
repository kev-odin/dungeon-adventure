# Kevin's Time Tracker: 1.5 hours

class Adventurer:
    """Adventurer that traverses through the maze. Picks up potions, falls into pits, and
    must complete the maze with all OOP pillars (APIE) collected to win.
    """

    def __init__(self, name = None):
        self.name = name
        self.dev_powers = False
        self.hitpoints = 75
        self.health_pots = 0
        self.vision_pots = 0
        self.pillars = {
            'A' : False,
            'P' : False,
            'I' : False,
            'E' : False
        }
        self.dev_abilities = {
            'fullmap' : 'something that allows visions',
            'tank' : 'unlimited health',
            'alchemist' : 'unlimited potions'
        }

    def __is_alive(self):
        return self.hitpoints > 0

    def __str__(self):
        player_stats = f'{self.name}\n{self.hitpoints}\n{self.health_pots}\n{self.vision_pots}\n{self.pillars}'
        return player_stats

    @property
    def name(self):
        """Getter for name property

        :return: name of adventurer
        :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for the name property

        :param value: name provided by user
        :type value: str
        """
        if isinstance(value, str):
            self.__name = value

    @property
    def hitpoints(self):
        """Getter for hitpoints property

        :return: health remaining of adventurer
        :rtype: int
        """
        return self.__hitpoints

    @hitpoints.setter
    def hitpoints(self, value):
        """Setter for the hitpoints property

        :param value: damage incurred from pits
        :type value: int
        """
        if isinstance(value, int):
            self.__hitpoints = value

    @property
    def health_pots(self):
        """Getter for health potion property

        :return: number of health potions for adventurer
        :rtype: int
        """
        return self.__health_pots

    @health_pots.setter
    def health_pots(self, value):
        """Setter for the health potion property

        :param value: number of potions found in the room
        :type value: int
        """
        if isinstance(value, int):
            self.__health_pots = value

    @property
    def vision_pots(self):
        """Getter for vision pots property

        :return: number of vision potions for adventurer
        :rtype: int
        """
        return self.__vision_pots

    @vision_pots.setter
    def vision_pots(self, value):
        """Setter for the health pots property

        :param value: number of potions found in the room
        :type value: int
        """
        if isinstance(value, int):
            self.__vision_pots = value
