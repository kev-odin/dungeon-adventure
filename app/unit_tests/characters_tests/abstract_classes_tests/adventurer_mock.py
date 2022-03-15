from app.model.characters.adventurer import Adventurer


class AdventurerMock(Adventurer):
    def __init__(self, adv_dict):
        super(AdventurerMock, self).__init__(adv_dict)

    def use_special(self):
        pass
