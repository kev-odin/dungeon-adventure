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

    def frame_setup(self):
        """Builds tKinter frames for the user.
        """
        self.__view.setup(self)
        self.__view.start_main_loop()

    def game_start(self):
        """Switches over to the DungeonCrawler view after the dungeon has been created.
        """
        self.window_destroy()
        dc = DungeonCrawler()
        self.__view = dc
        self.frame_setup()

    def window_destroy(self):
        print(f"DEBUG - Destroyed by Controller! {self}")
        self.__view.destruct()

    def set_model(self):
        """Function that grabs user settings from the view and pass to controller.
        Controller passes the settings to the model.
        """
        entry = self.__view.send_settings()
        dungeon = self.create_dungeon(str(entry["difficulty"]).lower())
        adv = self.create_adventurer(entry["name"], entry["class_name"])
        print(f"DEBUG - Dungeon created successfully. Passing off to DungeonCrawler")
        model = (dungeon, adv)
        x= 0
        self.game_start()

    def set_move(self, move):
        """Function that updates moves from the view (NSWE) and passes those instructions to the
        model
        """
        move_dict = {"n": "north", "w": "west", "s": "south", "e": "east"}
        try:
            print(f"DEBUG - Moving Adventurer {move_dict[move]}")
            self.__model.move_adventurer(move_dict[move])
        except KeyError:
            return f"An error occured. Please verify the {move} is a valid option."


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

    def update_adv_info(self):
        hero_name = self.__model.adventurer.name
        hero_hp = self.__model.adventurer.current_hitpoints
        hero_max_hp = self.__model.adventurer.max_hitpoints
        self.__view.set_adventurer_info(hero_name, hero_hp, hero_max_hp)

    def update_dungeon_display(self):
        print("DEBUG - Retrieving the hero position")

        adv_telemetry = self.__model.map
        self.__view.set_dungeon_display(adv_telemetry)

    def update_adv_bag(self):
        print("DEBUG - Pressing the Bag Button")
        pillars = self.__model.adventurer.pillars_collected
        health_pots = self.__model.adventurer.health_pots
        vision_pots = self.__model.adventurer.vision_pots

        bag = {
            "pillars": pillars,
            "health": health_pots,
            "vision": vision_pots
        }

        self.__view.set_bag_display(bag)

    def update_adv_map(self):
        print("DEBUG - Pressing the Map Button")
        
    def still_playing(self):
        print(self.__model.adventurer.is_alive())
        return self.__model.adventurer.is_alive()

if __name__ == "__main__":
    db = DungeonBuilder()
    gv = dungeon_adventure_GUI()
    gc = GameController(db, gv)
    gc.frame_setup()

    # dc = DungeonCrawler()
    # gc = GameController(db, dc)
    # gc.game_setup()
