from app.model.characters.adventurer import Adventurer


class Warrior(Adventurer):
    def __init__(self, adv_dict):
        super().__init__(adv_dict)

    def use_special(self):
        accuracy, min_dmg, max_dmg = 0.4, 75, 175
        # Hardcoded isn't my favorite, but making a separate table didn't feel right.
        return self.attack(accuracy, min_dmg, max_dmg)
