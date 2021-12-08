# Kevin's Time Tracker: 1 hours

from health_potion import HealthPotion
from vision_potion import VisionPotion

class PotionFactory:
    """Basic factory pattern to provide two types of potions that can be used
    by the adventurer object.
    """

    @staticmethod
    def create_potion(name):
        """
        Creates a potion based on provided name.
        :param name: str - Provide the name of the potion; "health", "vision"
        :return: Health or Vision potion based on the string passed
        :raises ValueError: When a potion name is not provided as an option
        """
        if name == "health":
            return HealthPotion()
        elif name == "vision":
            return VisionPotion()
        else:
            raise ValueError(f"{name} is not a valid potion.")
