from potion import Potion

class HealthPotion(Potion):
    def __init__(self):
        self.name = 'health_pot'

    def __str__(self):
        return f'{self.name}'

    def action(self):
        pass

    def random(self):
        pass

    @property
    def name(self):
        return self.name
