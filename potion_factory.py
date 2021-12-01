from health_potion import HealthPotion
from vision_potion import VisionPotion

class PotionFactory:

    @staticmethod
    def create_potion(name, *args):
        """
        Creates a potion based on name of provided and args.
        :param name:
        :param args:
        :return: Shape
        """
        if name == "health_pot":
            return HealthPotion()
        elif name == "vision_pot":
            return VisionPotion()
        else:
            raise ValueError(f"{name} is not a valid potion.")
