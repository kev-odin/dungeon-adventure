from tkinter import *
import tkinter as tk

# TODO: Readable pillars in the bag view        - Done
# TODO: Ability to use items in the bag view    - Bug
# TODO: Item number not updating after use      - Bug
# TODO: Controller saving                       - Bug

class BaseFrame(tk.Frame):
    def __init__(self):
        self.root = Tk()
        self.root.resizable(height = False, width = False)
        self.root.title("Dungeon Adventure 2.0 - The Spoony Bard Returns")
        self.root.geometry("800x600")
        self.controller = None
        self.basic_menu_bar()

    def destruct(self):
        self.root.destroy()

    def start_main_loop(self):
        self.root.mainloop()

    def set_controller(self, controller):
        self.controller = controller

    def basic_menu_bar(self):
        menubar = Menu()

        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "New game", command= lambda: self.controller.start_new())
        filemenu.add_command(label = "Save game", command= lambda: self.controller.save_game())
        filemenu.add_command(label = "Load game", command= lambda: self.controller.load_game())
        filemenu.add_command(label = "Quit game", command= self.root.destroy)

        menubar.add_cascade(label = "File", menu = filemenu)

        help = Menu(menubar, tearoff = 0)
        help.add_command(label = "About Us")
        help.add_command(label = "Controls")
        
        menubar.add_cascade(label = "Help", menu = help)

        self.root.config(menu = menubar)

    def load_existing_game_window(self):
        pop = Toplevel(self.root)
        pop.geometry("750x450")
        pop.resizable(width=False, height=False)
        pop.title("Load Game")

        btn3 = Button(pop, text="Confirm Load", command = pop.destroy).place(relx=0.75, rely=0.9)
        btn3.pack(self.root)

class DungeonCrawler(BaseFrame):
    def setup(self, controller):
        self.root.title("Dungeon Adventure 2.0 - DungeonCrawler")
        self.dungeon_crawl_frame = Frame(self.root, highlightbackground="Blue", highlightthickness=2)
        self.dungeon_crawl_canvas = Canvas(self.dungeon_crawl_frame, width=800, height=600)
        self.adventurer_canvas = Canvas(self.dungeon_crawl_frame, width=400, height=600)
        self.controller = controller

        self.adventurer_action()
        self.dungeon_navigation()

        self.controller.update_dungeon_display()
        self.controller.update_adv_info()

        self.dungeon_crawl_frame.pack()

    def update_display(self, controller):
        canvas = self.root
        dungeon = LabelFrame(canvas, width = 600, height = 400, bg = "White")
        text = Label(dungeon, text = f"{controller}", bg = "White")
        text.place(relx = 0.5, rely = 0.5, anchor = N)

    def adventurer_action(self):
        """Display base actions such as map and bag inventory
        """
        canvas = self.dungeon_crawl_canvas
        bag = Button(canvas, text= "Bag", command= lambda: self.controller.update_adv_bag())
        map = Button(canvas, text= "Map", command= lambda: self.controller.still_playing())
        
        bag.grid(row=3, column=1, sticky="nswe")
        map.grid(row=3, column=2, sticky="nswe")

        canvas.pack()

    def set_adventurer_info(self, adv_name, curr_hp, max_hp):
        """Display base adventurer information to be displayed during dungeon crawl.

        Args:
            adv_name (str): name of heroic adventurer
            curr_hp (int): current hitpoints
            max_hp (int): max hitpoints
        """
        canvas = self.dungeon_crawl_canvas
        name = Label(canvas, text = f"Name: {adv_name}", bg = 'White')
        name.grid(row = 0, column = 0)

        health = Label(canvas, text = f"Health Points: {curr_hp} / {max_hp}", bg = 'Green')
        health.grid(row = 1, column = 0)

        canvas.pack()

    def dungeon_navigation(self):
        canvas = self.dungeon_crawl_canvas

        encode = {
            "north" : "n",
            "south" : "s",
            "west"  : "w",
            "east"  : "e"
        }

        direction = {
            "north" : True,
            "south" : True,
            "west"  : False,
            "east"  : True
        }

        # for pos, door in enumerate(direction):
        #     if direction[door]:
        #         button = Button(canvas, text = {door}, command= lambda: self.controller.set_move(encode[door]))
        #         button.grid(row = 2, column=pos)

        travel_north = Button(canvas, text="North", command= lambda: self.controller.set_move("n"))
        travel_south = Button(canvas, text="South", command= lambda: self.controller.set_move("s"))
        travel_west = Button(canvas, text="West", command= lambda: self.controller.set_move("w"))
        travel_east = Button(canvas, text="East", command= lambda: self.controller.set_move("e"))

        travel_north.grid(row=2, column=1)
        travel_south.grid(row=2, column=2)
        travel_west.grid(row=2, column=3)
        travel_east.grid(row=2, column=4)

        canvas.pack()

    def set_dungeon_display(self, local_rooms):
        """Display the current dungeon visual to player in the Dungeon Crawler Frame
        """
        canvas = self.root
        
        dungeon = LabelFrame(canvas, width= 400, height= 400, bg= "White")
        text = Label(dungeon, text= "Place Maze Here...", bg= "White")

        dungeon.place(relx= 0.5, rely= 0.25, anchor= N)
        text.place(relx= 0.5, rely= 0.5, anchor= N)

    def set_bag_display(self, bag_stuff):
        """Display the current hero bag to player

        :param bag_stuff: _description_
        :type bag_stuff: dictionary {pillars : {str : bool}, "health" : int, "vision" : int}
        """

        def update_counter(label, potion_type):
            
            if potion_type == "Health":
                curr_count = self.controller.get_health_pots()
            elif potion_type == "Vision":
                curr_count = self.controller.get_vision_pots()

            label["text"] = f"{potion_type} Potion Count: {curr_count}"

        bag = Toplevel(self.root)
        bag.geometry("400x400")
        bag.resizable(width= False, height= False)
        bag.title("Adventurer Inventory")

        close_bag = Button(bag, text= "Close Bag", command= bag.destroy)
        close_bag.pack(side=BOTTOM, fill=X)

        if bag_stuff["pillars"]:
            pillar_frame = LabelFrame(bag, text = "Pillars Collected")
            pillar_frame.pack(side=TOP)

            pillar_description = {
                "A": ("Abstraction", "Grants double health potion collection."),
                "P": ("Polymorphism", "Grants double vision potion collection."),
                "I": ("Inheritance", "Grants reduced damage."),
                "E": ("Encapsulation", "Grants improved potion potency.")
            }

            for pillar, status in bag_stuff["pillars"].items():
                if status:
                    pillar_str = pillar_description[pillar][0]
                    pillar_pwr = pillar_description[pillar][1]
                    pillar_lbl = Label(pillar_frame, text= f"{pillar_str, pillar_pwr}")
                    pillar_lbl.pack()

        if bag_stuff["health"] or bag_stuff["vision"]:
            potion_frame = LabelFrame(bag, text = "Potions Collected")
            potion_frame.pack(side=TOP)

            if bag_stuff["health"]:
                health_lbl = Label(potion_frame, text = f"Health Potion Count: {bag_stuff['health']}", padx = 10)
                use_health = Button(potion_frame, text="Use Health Potion", command = lambda: [self.controller.set_potion("health"), update_counter(health_lbl, "Health")])
                
                health_lbl.grid(row=0, column=0)
                use_health.grid(row=0, column=1)

            if bag_stuff["vision"]:
                vision_lbl = Label(potion_frame, text = f"Vision Potion Count: {bag_stuff['vision']}", padx = 10)
                use_vision = Button(potion_frame, text="Use Vision Potion", command = lambda: [self.controller.set_potion("vision"), update_counter(vision_lbl, "Vision")])
                
                vision_lbl.grid(row=1, column=0)
                use_vision.grid(row=1, column=1)

class DungeonBrawler(BaseFrame):
    def setup(self):
        self.dungeon_brawl_frame = Frame(self.root)
        self.root.title("DungeonBrawler")
        left_frame = Frame(self.dungeon_brawl_frame, width = 400, height = 400, bg = "green")
        right_frame = Frame(self.dungeon_brawl_frame, width = 400, height = 400, bg = "red")
        combat_log = Frame(self.dungeon_brawl_frame, width = 400, height = 200, bg = "blue")
        combat_action = Frame(self.dungeon_brawl_frame, width= 400, height = 200, bg = "white")
        
        self.dungeon_brawl_frame.pack() 
        # self.create_hero_frame(left_frame, "hello")
        self.set_combat_action(combat_action)
        self.set_combat_log(combat_log)

        left_frame.grid(row = 0, column= 0)
        right_frame.grid(row = 0, column= 1)
        combat_action.grid(row = 1, column=0)
        combat_log.grid(row = 1, column= 1)

    def create_hero_frame(self, parent, hero = None):
        hero_frame = Frame(parent)
        hero_label = Label(hero_frame, text = f"{hero}", bg="white")
        hero_frame.pack(side = TOP)
        hero_label.grid(row = 0, column=0)
        
        # return hero_frame

    def set_monster(self, monster = None):
        monster_frame = Frame(self.right_frame)
        monster_label = Label(monster_frame, text = f"{monster}")
        monster_label.pack()

    def set_combat_log(self, parent_frame, event = None):
        canvas = parent_frame
        text = Text(canvas, height=10)
        text.grid(row=0, column=0, sticky='ew')
        scrollbar = Scrollbar(canvas, orient='vertical', command= text.yview)
        scrollbar.grid(row=0, column=0, sticky='ns')

    def set_combat_action(self, parent_frame):
        canvas = parent_frame

        attack = Button(canvas, text="Attack", command= lambda: self.controller.set_move("n"))
        special = Button(canvas, text="Special", command= lambda: self.controller.set_move("s"))
        bag = Button(canvas, text="Bag", command= lambda: self.controller.set_move("w"))

        attack.grid(row=0, column=1)
        special.grid(row=0, column=2)
        bag.grid(row=0, column=3)
        
        # return canvas

    def update_monster(self, controller):
        pass

    def update_hero(self, controller):
        pass

    def update_combat_action(self, controller):
        pass

    def update_combat_log(self, controller):
        pass

if __name__ == "__main__":
    test = DungeonBrawler()
    test.setup()
    test.start_main_loop()
