from app.model.dungeon.dungeon_builder import DungeonBuilder
from app.model.items.potion_factory import PotionFactory
from app.view.dungeon_crawler import DungeonCrawler, DungeonBrawler
from app.view.dungeon_adventure_GUI import dungeon_adventure_GUI

# TODO: https://www.youtube.com/watch?v=ihtIcGkTFBU
# TODO: Update adventurer bag when entering a room - Done
# TODO: Update view with room contents - Done
# TODO: Room Dungeon Canvas 
# TODO: Dungeon Map Canvas
# TODO: DungeonBrawler

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
        """Controller for Dungeon Adventure. Main purpose to pass data from view to set changes
        to the model. And update changes from the model to the view.

        :param model: Initial model is DungeonBuilder which will later change to Dungeon, Map, and Adventurer
        :type model: Python Dictionary
        :param view: Views include Initial Dungeon set-up, DungeonCrawler - traversal, DungeonBrawler - combat
        :type view: Single view from any of the previous parameters
        """
        self.__model = model                            # Model
        self.__view = view                              # View

    def frame_setup(self):
        """Builds tKinter frames for the user based on the current view.
        """
        self.__view.setup(self)
        self.__view.start_main_loop()

    def game_start(self):
        """Switches over to the DungeonCrawler view after the dungeon has been created.
        """
        self.window_destroy()
        crawl = DungeonCrawler()
        # brawl = DungeonBrawler()
        self.__view = crawl
        self.frame_setup()

    def window_destroy(self):
        """Specific call from controller to close the current view to user.
        """
        print(f"DEBUG - Destroyed by Controller! {self}")
        self.__view.destruct()

    def set_model(self):
        """Function that grabs user settings from the view and pass to controller.
        Controller passes the settings to the model. Creates the model model dictionary for
        organization.
        """
        entry = self.__view.send_settings()
        dungeon = self.create_dungeon(entry["difficulty"])
        hero = self.create_adventurer(entry["name"], entry["class_name"])
        dungeon_map = self.__model.map

        print(f"DEBUG - Dungeon created successfully. Passing off to DungeonCrawler")
        
        self.__model = {
            "dungeon"   : dungeon,
            "map"       : dungeon_map,
            "hero"      : hero
        }
        
        self.game_start()

    def set_move(self, move):
        """Function that updates moves from the view (NSWE) and passes those instructions to the
        model. When a monster is encountered, then the DungeonBrawler view will be activated
        """
        move_dict = {"n": "north", "w": "west", "s": "south", "e": "east"}
        try:
            print(f"DEBUG - Moving Adventurer {move_dict[move]}")
            new_room = self.__model["dungeon"].move_adventurer(move_dict[move])
            print(f"{new_room}")
            moving = self.__model["dungeon"].get_visible_dungeon_string() # Just for easy debug
            print(f"{moving}")

            if new_room.monster:
                hero = self.__model["hero"]
                monster = self.__model["dungeon"].monster
                self.start_combat(hero, monster)

            if new_room.contents:
                self.set_bag(new_room)

        except KeyError:
            return f"An error occured. Please verify the {move} is a valid option."

    def start_combat(self, hero = None, monster = None):
        # brawl = DungeonBrawler()
        # self.__view = brawl
        # self.__view.setup()
        # Change over to the DungeonBrawler view
        # while the hero and monster is alive ensure that the event loop continues
            # Update health of both adventurer and monster at the start of each round
            # Compare the attack speed of both the monster and adventurer
            # higher attack speed goes first
            # example: hero - as(5); monster - as(4)
            # Since, we can based on attacks per round we will go with hero / monster
            # hero_attacks = 1.25, so every 4 turns, we get an extra attack.
            # Update DungeonBrawler with relevant information at the start of each round.
            # if monster dies:
                # Collect items, then go back to DungeonCrawler
                # Update hero information within DungeonCrawler
            # if hero dies:
                # Prompt a Game Over frame, with options to start a new game or quit.
        print(f"Hey {hero.name} encountered a {monster.name}. Run away!")

    def set_bag(self, room):
        """Function that sets the bag for the adventurer when a collectable potion or pillar is encountered.
        Model is updated when changes occur.

        :param room: rooms can contain an entrance/exit, potions, pillars, or monsters
        :type room: room
        """
        if room.contents in ("A", "P", "I", "E"):
            pillar_str = self.__model["dungeon"].collect_pillars()

            if pillar_str:
                self.__model["hero"].add_pillar(pillar_str)

        if room.contents in ("H", "V", "M"):
            collected_pots = self.__model["dungeon"].collect_potions()
            self.__model["hero"].add_potions(collected_pots)

    def set_potion(self, potion: str):
        """Function to use health/vision potion in hero inventory.

        :param potion: _description_
        :type potion: str
        """
        if potion == "health" and self.__model["hero"].has_health_potion():
            heal = PotionFactory().create_potion("health")
            self.__model["hero"].heal_adventurer(heal)
            print("DEBUG - Should be using a health potion")
        
        if potion == "vision":
            print(f"DEBUG - Not Implemented yet.")

    def create_adventurer(self, name: str, class_name: str):
        try:
           return self.__model.build_adventurer(name, class_name)
        except ValueError:
            return f"An error occurred.  Please verify {class_name} and {name} are valid options."

    def create_dungeon(self, difficulty: str):
        try:
            return self.__model.build_dungeon(difficulty)
        except ValueError:
            return f"An error occurred.  Please verify {difficulty} is a valid option."

    def update_adv_info(self):
        """Update the DungeonCrawler frame with hero information from the model.
        """
        hero_name = self.__model["hero"].name
        hero_hp = self.__model["hero"].current_hitpoints
        hero_max_hp = self.__model["hero"].max_hitpoints
        self.__view.set_adventurer_info(hero_name, hero_hp, hero_max_hp)

    def update_dungeon_display(self):
        """Update the DungeonCrawler frame with map information from the model.
        """
        print("DEBUG - Retrieving the hero position")

        adv_telemetry = self.__model["dungeon"]
        self.__view.set_dungeon_display(adv_telemetry)

    def update_adv_bag(self):
        """Update the DungeonCrawler frame with hero inventory information from the model.
        """
        print("DEBUG - Pressing the Bag Button")
        pillars = self.__model["hero"].pillars_collected
        health_pots = self.__model["hero"].health_pots
        vision_pots = self.__model["hero"].vision_pots

        bag = {
            "pillars": pillars,
            "health": health_pots,
            "vision": vision_pots
        }
        print(f"DEBUG - {bag}")
        self.__view.set_bag_display(bag)

    def update_adv_map(self):
        """Update the frame with map information from the model.
        """
        print("DEBUG - Pressing the Map Button")
        
    def still_playing(self):
        return self.__model["hero"].is_alive()

if __name__ == "__main__":
    db = DungeonBuilder()
    gv = dungeon_adventure_GUI()
    gc = GameController(db, gv)
    gc.frame_setup()
