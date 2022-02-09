# Kevin's Time Tracker: 1 hours

from model.items.health_potion import HealthPotion
from model.items.vision_potion import VisionPotion

class PotionFactory:
    """Basic factory pattern to provide two types of potion objects.
    """

    @staticmethod
    def create_potion(name):
        """
        Creates a potion based on provided name.
        :param name: str - Provide the name of the potion; "health", "vision"
        :return: Health or Vision potion based on the string passed
        :raises ValueError: When a potion name is not provided as an option
        """
        valid_potions = "health or vision"
        try:
            if name == "health":
                return HealthPotion()
            elif name == "vision":
                return VisionPotion()
            else:
                raise ValueError
        except ValueError:
            print(f"{name} is not a valid potion option: {valid_potions}")
        except TypeError:
            print(f"You must pass in a valid option: {valid_potions}")
