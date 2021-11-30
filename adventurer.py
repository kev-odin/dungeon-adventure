# Kevin's Time Tracker: 1 hour

class Adventurer:
    """Adventurer that traverses through the maze. Picks up potions, falls into pits, and must complete the maze to win.
    """

    def __init__(self):
        self.name = None
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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value

    @property
    def hitpoints(self):
        return self.__hitpoints

    @hitpoints.setter
    def hitpoints(self, value):
        if isinstance(value, int):
            self.__hitpoints = value

    @property
    def health_pots(self):
        return self.__health_pots

    @health_pots.setter
    def health_pots(self, value):
        if isinstance(value, int):
            self.__health_pots = value

    @property
    def vision_pots(self):
        return self.__vision_pots

    @vision_pots.setter
    def vision_pots(self, value):
        if isinstance(value, int):
            self.__vision_pots = value

    def __str__(self):
        player_stats = f'{self.name}\n{self.hitpoints}\n{self.health_pots}\n{self.vision_pots}\n{self.pillars}'
        return player_stats
