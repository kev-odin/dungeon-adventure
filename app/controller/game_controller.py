from app.model.dungeon.dungeon_builder import DungeonBuilder
from app.view.dungeon_crawler import DungeonCrawler
from app.view.dungeon_adventure_GUI import dungeon_adventure_GUI

# TODO: https://www.youtube.com/watch?v=ihtIcGkTFBU
# Controller methods are accessed by the view because we are passing the reference to Controller.
# 

# From here everything you need from the dungeon and adventurer can be accessed via dungeon builder.
# Depending on how you want to receive information, may translate it into a different format.
# The idea is that the view has no idea who it is talking to or what, and aside from function calls,
# keep non-visual code out of the view as much as possible.  Logic goes in the controller.
# The controller can talk to as many things as its specific view needs it to, be it adventurers, potions, etc.
# The view only cares about what it's showing.
# The controller cares about manipulating data from the model so the view can see it and manipulating
# data from the view so that model can process it.
# Onclick listeners will usually listen for an event then pull the data in those fields in the view out.
# Hope this helps!  I'm not familiar enough with TKinter to go into too many specific examples!
# I should go read your code, ahaha.

class GameController:
    def __init__(self, model, view):
        self.__model = model                            # Model
        self.__view = view                              # View

    def game_setup(self):
        self.__view.setup(self)
        self.__view.start_main_loop()

    def window_destroy(self):
        print(f"Destroyed by Controller! {self}")
        self.__view.destruct()
    
    def print_settings(self):
        print(self.__view.send_settings())

    def create_adventurer(self, name: str, class_name: str):  # Or however you want to pass this.
        try:
            self.__model.build_adventurer(name, class_name)  # If not like this, translate it to look like this
        except ValueError:
            # How you want to display the error to the view / player.  Suggest dropdowns for things that aren't
            # flexible.
            return f"An error occurred.  Please verify {class_name} and {name} are valid options."

    def create_dungeon(self, difficulty: str):
        try:
            self.__view()
            self.__model.build_dungeon(difficulty)  # If not like this, translate it to look like this
        except ValueError:
            # How you want to display the error to the view / player.
            return f"An error occurred.  Please verify {difficulty} is a valid option."

    def adventurer(self):
        return self.__model.adventurer.name

    def still_playing(self):  # Whatever that is, this will probably be a check after the user tries to do something
        return self.__model.adventurer.is_alive()

    # def move_adventurer(self, movement):
    #     return self.__model.move_adventurer(move[movement])

    # def show_adventurer(self):
    #     self.__dungeon_view.adventurer_info(self.adventurer())

if __name__ == "__main__":
    db = DungeonBuilder()
    gv = dungeon_adventure_GUI()
    gc = GameController(db, gv)
    gc.game_setup()
    gc.print_settings()
    # dc = DungeonCrawler()
    # gc = GameController(db, dc)
    # gc.game_setup()
