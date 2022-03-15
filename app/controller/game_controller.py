from app.model.dungeon.dungeon_builder import DungeonBuilder
from app.model.db.save_manager import SaveManager
from app.model.items.potion_factory import PotionFactory
from app.view.dungeon_crawler import DungeonCrawler, DungeonBrawler
from app.view.dungeon_adventure_GUI import dungeon_adventure_GUI
from app.view.load_view import LoadView

# TODO: https://www.youtube.com/watch?v=ihtIcGkTFBU
# TODO: Update adventurer bag when entering a room  - Done
# TODO: Update view with room contents              - Done
# TODO: Save Game                                   - Done
# TODO: Room Dungeon Canvas                         - Done
# TODO: Dungeon Map Canvas                          - Done
# TODO: DungeonBrawler                              - WIP
# TODO: Start New                                   - WIP
# TODO: Load Game                                   - Done
# TODO: Quit Game                                   - Done

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
        self.__base = view

    def start_new(self, parent):
        """Function to restart game from the start.
        """
        print(f"Starting new game...")
        self.__model = None
        self.__view = None
        db = DungeonBuilder()
        gui = dungeon_adventure_GUI()
        self.__model = db
        self.__view = gui
        self.__view.setup(self, parent)

    def load_game(self, view_root):
        """
        Opens menu to load a game.
        :param view: current view's tk root.
        :return:
        """
        load_view = LoadView()
        load_view.setup(controller=self, parent=view_root)
        print(f"Launching load menu...")

    def get_saved_games(self):
        """
        Loads all the saved games.  Keys for dictionary: "timestamp", "hero_name", "class", "difficulty", "current_hp",
        "max_hp".
        :return: List of dictionaries representing all the saves games basic information.
        """
        games = SaveManager.get_saved_games()
        print("Games retrieved.")
        return games

    def load_game_to_model(self, timestamp: str):
        """
        Loads game from the database then converts it into Dungeon, Model, Adventurer classes, and sets to current model
        :param timestamp: str matching timestamp key from get_saved_games dictionary.
        """
        game = SaveManager.load(timestamp)
        db = DungeonBuilder()
        game = db.load_game(game)
        self.set_model(game)
        print("Game loaded.")

    def save_game(self, game):
        """
        Saves the game to the database.
        :return: True if saved, False if an error occurred.
        """
        dungeon, adventurer, map = game["dungeon"], game["hero"], game["map"]
        dungeon, adventurer, map = dungeon.json_dict, adventurer.char_dict, map.map_dict
        print(f"Game saved.")
        return SaveManager.save(dungeon, adventurer, map)

    def frame_setup(self):
        """Builds tKinter frames for the user based on the current view.
        """
        self.__view.setup(self)
        self.__view.start_main_loop()

    def game_start(self):
        """Switches over to the DungeonCrawler view after the dungeon has been created.
        """
        global crawl
        self.window_destroy()
        crawl = DungeonCrawler()
        self.__view = crawl
        self.frame_setup()

    def window_destroy(self):
        """Specific call from controller to close the current view to user.
        """
        print(f"DEBUG - Destroyed by Controller! {self}")
        self.__view.destruct()

    def set_model(self, game=None):
        """Function that grabs user settings from the view and pass to controller.
        It can also receive the game from a loaded game state.
        Controller passes the settings to the model. Creates the model model dictionary for
        organization.
        :param game: dict with "dungeon", "map", and "adventurer" keys.  If None, will build from scratch given settings.
        """
        if game is None:  # Allows same method to be used when loading a game vs. new game.
            entry = self.__view.send_settings()
            dungeon = self.create_dungeon(entry["difficulty"])
            hero = self.create_adventurer(entry["name"], entry["class_name"])
            dungeon_map = self.__model.map
        else:
            dungeon, dungeon_map, hero = game["dungeon"], game["map"], game["adventurer"]

        print(f"DEBUG - Dungeon created successfully. Passing off to DungeonCrawler")

        self.__model = {
            "dungeon": dungeon,
            "map": dungeon_map,
            "hero": hero
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
            moving = self.get_dungeon()  # DEBUG
            print(f"{moving}")
            print(f"Exit: {self.__model['dungeon'].exit}, Current: {self.__model['dungeon'].adventurer_loc}")

            if new_room.monster:
                hero = self.get_hero()
                monster = self.get_monster()
                self.start_combat(hero, monster)

            if new_room.contents:
                self.set_bag(new_room)

        except KeyError:
            return f"An error occured. Please verify the {move} is a valid option."

    def start_combat(self, hero, monster):
        print(f"Hey {hero.name} encountered a {monster.name}.")
        action_string = f"{hero.name} encountered a {monster.name}."
        
        brawl = DungeonBrawler()
        self.actions_capture = []
        self.actions_capture.append(action_string)

        self.turn_list = self.determine_attacks_per_round(hero, monster)
        
        self.__brawl = brawl
        self.__brawl.setup(self, hero, monster)
        self.__brawl.update_combat_log(self.actions_capture)

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

    def determine_attacks_per_round(self, hero, monster):
        hero_order = [hero.attack_speed * x for x in range(1, 10)]
        monster_order = [monster.attack_speed * x for x in range(1, 10)]
        
        match = min(set(hero_order).intersection(monster_order))

        hero_strike = hero_order.index(match)
        monster_strike = monster_order.index(match)

        if hero_strike <= monster_strike:
            turn_order = [hero for _ in range(monster_strike + 1)]
            turn_order.append(monster)
        else:
            turn_order = [monster for _ in range(hero_strike + 1)]
            turn_order.append(hero)

        return turn_order
        
    def end_combat(self):
        """After Combat Ends, the player should be back into the DungeonCrawler view
        """
        self.__brawl.destruct()
        room = self.get_room(self.get_hero_location())
        room.clear_room()
        self.update_adv_info()

    def set_action(self, action: str, hero, target):
        action_string = ""

        if self.still_playing():
            monster_heal = []
            
            if action == "attack":
                for turn in self.turn_list:
                    hero_dmg = hero.attack()
                    monster_dmg = target.attack()
                    
                    if turn is hero:
                        monster_heal = target.take_damage(hero_dmg)
                        action_string = f"{hero.name} inflicted {hero_dmg} to the {target.name}"
                        if hero_dmg == 0:
                            action_string = f"{hero.name} attack bounced off the {target.name}!"
                        if monster_heal > 0:
                            action_string += f", but the {target.name} healed for {monster_heal}."

                    else:
                        action_string = ""
                        total_monster_dmg = hero.take_damage(monster_dmg)

                        if total_monster_dmg == 0:
                            action_string += f"{hero.name} negated the incoming damage from the {target.name}!"
                        else:
                            action_string = f"{target.name} inflicted {total_monster_dmg} to {hero.name}"
                        
                    self.actions_capture.append(action_string)

            if action == "special":
                action_string = f"{hero.name}"
                if hero.adv_class == "Priestess":
                    heal_amount = hero.use_special()
                    action_string += f" healed for {heal_amount}."
                else:
                    monster_heal, monster_heal2 = 0, 0
                    hero_special = hero.use_special()
                    if type(hero_special) is tuple:
                        monster_heal = target.take_damage(hero_special[0])
                        monster_heal2 = target.take_damage(hero_special[1])
                        action_string += f" dealt {hero_special[0]} and {hero_special[1]}"
                    else:
                        monster_heal = target.take_damage(hero_special)
                        action_string += f" dealt {hero_special}"
                    
                    action_string += f" to {target.name} using {hero.special}"
                    
                    if monster_heal:
                        action_string += f", and {target.name} healed for {monster_heal}"
                    if monster_heal2:
                        action_string += f", and {target.name} healed for {monster_heal2}"
                
                self.actions_capture.append(action_string)
                action_string = ""
                
                monster_dmg = target.attack()
                total_monster_dmg = hero.take_damage(monster_dmg)

                if total_monster_dmg == 0:
                    action_string += f"{hero.name} negated the incoming damage from {target.name}!"
                else:
                    action_string += f"{target.name} inflicted {total_monster_dmg} to {hero.name}"
                
                self.actions_capture.append(action_string)

            if target.current_hitpoints <= 0:
                self.actions_capture.append(f"{hero.name} defeated the {target.name}")
                self.__brawl.update_combat_log(self.actions_capture)                
                # self.end_combat()

            if hero.current_hitpoints <= 0:
                self.actions_capture.append(f"{target.name} defeated {hero.name}.")
                self.__brawl.update_combat_log(self.actions_capture)
                self.__view.set_lose_message(hero, self.__view.root)
                # self.end_combat()

        self.__brawl.update_combat_log(self.actions_capture)

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
            hero = self.__model["hero"]
            self.__view.set_adventurer_info(hero.name, hero.current_hitpoints, hero.max_hitpoints)
            print("DEBUG - Should be using a health potion")

            if self.actions_capture:
                potion_str = f"{hero.name} used {heal.name} and increased {heal.heal_amount} HP"
                self.actions_capture.append(potion_str)
                self.__brawl.update_combat_log(self.actions_capture)

        if potion == "vision" and self.__model["hero"].has_vision_potion():
            print(f"DEBUG - Should be using a vision potion")

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
        hero_name = self.get_hero_name()
        hero_hp = self.get_hero_curr_hp()
        hero_max_hp = self.get_hero_max_hp()
        self.__view.set_adventurer_info(hero_name, hero_hp, hero_max_hp)

    def update_dungeon_display(self):
        """Update the DungeonCrawler frame with map information from the model.
        """
        print("DEBUG - Retrieving the hero position")
        map = self.__model["map"]
        adv_telemetry = self.__model["dungeon"]
        self.__view.set_dungeon_display(map, adv_telemetry)

    def update_adv_bag(self):
        """Update the DungeonCrawler frame with hero inventory information from the model.
        """
        print("DEBUG - Pressing the Bag Button")
        pillars = self.get_collected_pillars()
        health_pots = self.get_health_pots()
        vision_pots = self.get_vision_pots()

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
        map = self.__model["map"]           # follow Kevin's example of update_adv_info and update_adv_bag, we get the pillar from the model and send it back to the view
        dungeon = self.__model["dungeon"]   # and then view is going to use this info to prepare the display

        self.__view.set_map_display(map, dungeon)

    def update_win_message(self):
        '''
        Display the corresponding message immediately after win the game
        '''
        dungeon = self.__model["dungeon"]
        hero = self.__model["hero"]

        self.__view.set_win_message(dungeon, hero, self.__view.root)

    def update_lose_message(self):
        '''
        Display the corresponding message immediately after lose the game
        '''
        hero = self.__model["hero"]
        self.__view.set_lose_message(hero, self.__view.root)

    def get_hero(self):
        """Hero getter for the model.
        :return: Hero object
        """
        return self.__model["hero"]

    def get_monster(self):
        """Returns the current monster that the hero has encountered in the room.
        :return: Monster object
        """
        return self.__model["dungeon"].monster

    def get_hero_name(self):
        """Hero name getter for the model.
        :return: str
        """
        return self.__model["hero"].name

    def get_hero_curr_hp(self):
        """Hero current hp getter for the model.
        :return: int
        """
        return self.__model["hero"].current_hitpoints

    def get_hero_max_hp(self):
        """Hero max hp getter for the model.
        :return: int
        """
        return self.__model["hero"].max_hitpoints

    def get_collected_pillars(self):
        """Hero current health count getter for the model.
        :return: int
        """
        return self.__model["hero"].pillars_collected

    def get_health_pots(self):
        """Hero current health count getter for the model.
        :return: int
        """
        return self.__model["hero"].health_pots

    def get_vision_pots(self):
        """Hero current vision count getter for the model.
        :return: int
        """
        return self.__model["hero"].vision_pots

    def get_dungeon(self):
        """Entire dungeon representation in this string
        :return: str
        """
        return self.__model["dungeon"].get_visible_dungeon_string()

    def get_hero_location(self):
        return self.__model["dungeon"].adventurer_loc

    def get_room(self, location):
        return self.__model["dungeon"].get_room(location)

    def get_current_doors(self):
        current_loc = self.get_hero_location()
        current_room = self.get_room(current_loc)
        return current_room.doors

    def still_playing(self):
        return self.__model["hero"].is_alive()

if __name__ == "__main__":
    db = DungeonBuilder()
    gv = dungeon_adventure_GUI()
    gc = GameController(db, gv)
    gc.frame_setup()
