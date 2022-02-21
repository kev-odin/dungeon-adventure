from app.model.dungeon.dungeon_builder import DungeonBuilder
from app.view.dungeon_crawler import DungeonCrawler
from app.view.dungeon_adventure_GUI import dungeon_adventure_GUI

# TODO: https://www.youtube.com/watch?v=ihtIcGkTFBU
# Controller methods are accessed by the view because we are passing the reference to Controller.

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
        """Builds tKinter frames for the user.
        """
        self.__view.setup(self)
        self.__view.start_main_loop()

    def game_start(self):
        """Switches over to the DungeonCrawler view after the dungeon has been created.
        """
        self.window_destroy()
        adv = self.__model.adventurer
        dc = DungeonCrawler()
        self.__view = dc
        self.game_setup()

    def window_destroy(self):
        print(f"DEBUG-Destroyed by Controller! {self}")
        self.__view.destruct()
    
    def user_settings(self):
        return self.__view.send_settings()

    def user_settings_to_model(self):
        """Function that grabs user settings from the view and pass to controller.
        Controller passes the settings to the model.
        """
        entry = self.user_settings()
        self.create_adventurer(entry["name"], entry["class_name"])
        self.create_dungeon(entry["difficulty"])
        print(f"DEBUG-SDungeon created successfully.")
        self.game_start()

    def create_adventurer(self, name: str, class_name: str):
        try:
            self.__model.build_adventurer(name, class_name)
        except ValueError:
            return f"An error occurred.  Please verify {class_name} and {name} are valid options."

    def create_dungeon(self, difficulty: str):
        try:
            self.__model.build_dungeon(difficulty)
        except ValueError:
            return f"An error occurred.  Please verify {difficulty} is a valid option."

    def adventurer(self):
        print("Hey I have been called.")
        return self.__model.adventurer.name

    def still_playing(self):
        return self.__model.adventurer.is_alive()

    def adventurer_hp(self):
        return self.__model.adventurer.current_hitpoints

if __name__ == "__main__":
    db = DungeonBuilder()
    gv = dungeon_adventure_GUI()
    gc = GameController(db, gv)
    gc.game_setup()
    test = "Hi"

    # dc = DungeonCrawler()
    # gc = GameController(db, dc)
    # gc.game_setup()
