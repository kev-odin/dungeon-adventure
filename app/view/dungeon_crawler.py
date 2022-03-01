from tkinter import *
import tkinter as tk

# TODO: Readable pillars in the bag view
# TODO: Ability to use items in the bag view

class BaseFrame(tk.Frame):
    def __init__(self):
        self.root = Tk()
        self.root.resizable(height = False, width = False)
        self.root.title("Dungeon Adventure 2.0 - The Spoony Bard Returns")
        self.root.geometry("800x600")
        self.basic_menu_bar()

    def destruct(self):
        self.destroy()

    def start_main_loop(self):
        self.root.mainloop()

    def basic_menu_bar(self):
        menubar = Menu()

        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "New game...")
        filemenu.add_command(label = "Save game")
        filemenu.add_command(label = "Load game", command=self.load_existing_game_window)
        filemenu.add_command(label = "Quit game", command=self.root.destroy)

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
        self.dungeon_crawl_frame = Frame(self.root, highlightbackground="Blue", highlightthickness=2)
        self.dungeon_crawl_canvas = Canvas(self.dungeon_crawl_frame, width=800, height=600)
        self.adventurer_canvas = Canvas(self.dungeon_crawl_frame, width=400, height=600)

        self.adventurer_action(controller)
        self.dungeon_navigation(controller)

        controller.update_dungeon_display()
        controller.update_adv_info()

        self.dungeon_crawl_frame.pack()

    def update_display(self, controller):
        canvas = self.root
        
        dungeon = LabelFrame(canvas, width = 600, height = 400, bg = "White")
        text = Label(dungeon, text = f"{controller}", bg = "White")
        text.place(relx = 0.5, rely = 0.5, anchor = N)

    def adventurer_action(self, controller):
        """Display base actions such as map and bag inventory
        """
        canvas = self.dungeon_crawl_canvas
        bag = Button(canvas, text= "Bag", command = lambda: controller.update_adv_bag())
        map = Button(canvas, text= "Map", command = lambda: controller.update_adv_map()) #
        
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

    def dungeon_navigation(self, controller):
        canvas = self.dungeon_crawl_canvas

        travel_north = Button(canvas, text="North", command= lambda: controller.set_move("n"))
        travel_south = Button(canvas, text="South", command= lambda: controller.set_move("s"))
        travel_west = Button(canvas, text="West", command= lambda: controller.set_move("w"))
        travel_east = Button(canvas, text="East", command= lambda: controller.set_move("e"))

        travel_north.grid(row=2, column=1)
        travel_south.grid(row=2, column=2)
        travel_west.grid(row=2, column=3)
        travel_east.grid(row=2, column=4)

        canvas.pack()

    def set_dungeon_display(self, adv_telemetry):
        """Display the current dungeon visual to player in the Dungeon Crawler Frame
        """
        canvas = self.root
        adjacent_rooms = LabelFrame(canvas, width = 300, height = 300, bg = "White")
        # text = Label(dungeon, text = "Place Maze Here...", bg = "White")
        print(adv_telemetry.get_room(adv_telemetry.adventurer_loc)) # this get room will return a room(string)
        print(adv_telemetry.get_room(adv_telemetry.adventurer_loc).string_top())

        for i in range(9):
            b = 'b'+str(i)
            if (b == 'b4'):
                b = Button(adjacent_rooms)
                # b.img = PhotoImage(file='/Users/hxg/Library/Mobile Documents/com~apple~CloudDocs/Desktop/UniversityOfWashington/TCSS504Winter/Assignment9-Groupwork/The_Spoony_Bard/app/view/image assets/priest.gif')
                b.img = PhotoImage()
                # b.img2 = b.img.subsample(10, 10)
                b.config(height=100, width=100, image=b.img)
                # b.config(height=100, width=100, text="---")
                b.grid(row=int(i/3), column=int(i%3))
                b.grid(sticky = "NWSE")
            else:
                b = Button(adjacent_rooms)
                b.img = PhotoImage()
                b.config(height=100, width=100, image=b.img, compound=CENTER)
                b.grid(row=int(i / 3), column=int(i % 3))
                b.grid(sticky="NWSE")


        # use the adventurer_loc from the dungeon class to update the current dungeon display window

        adjacent_rooms.place(relx = 0.5, rely = 0.25, anchor = N)
        # text.place(relx = 0.5, rely = 0.5, anchor = N)

    def set_bag_display(self, bag_stuff):
        bag = Toplevel(self.root)
        bag.geometry("400x400")
        bag.resizable(width = False, height = False)
        bag.title("Adventurer Inventory")


        print(bag_stuff)
        close_bag = Button(bag, text="Close Bag", command = bag.destroy)
        close_bag.pack(side=BOTTOM, fill=X)

        if bag_stuff["pillars"]:
            pillar_frame = LabelFrame(bag, text = "Pillars Collected")
            pillar_frame.pack(side=TOP)

            for pillar, status in bag_stuff["pillars"].items():
                pillar_lbl = Label(pillar_frame, text=f"{pillar, status}")
                pillar_lbl.pack()

        if bag_stuff["health"] or bag_stuff["vision"]:
            potion_frame = LabelFrame(bag, text = "Potions Collected")
            potion_frame.pack(side=TOP)

            if bag_stuff["health"]:
                health_str = f"Health Potion Count: " + str(bag_stuff["health"])
                health_count = Label(potion_frame, text = f"{health_str}", padx = 10)
                use_health = Button(potion_frame, text="Use Health Potion", command = bag.destroy)
                health_count.grid(row=0, column=0)
                use_health.grid(row=0, column=1)

            if bag_stuff["vision"]:
                vision_str = f"Vision Potion Count: " + str(bag_stuff["vision"])
                vision_count = Label(potion_frame, text = f"{vision_str}", padx = 10)
                use_vision = Button(potion_frame, text="Use Vision Potion", command = bag.destroy)
                vision_count.grid(row=1, column=0)
                use_vision.grid(row=1, column=1)

    def set_map_display(self, map, dungeon):
        map_window = Toplevel(self.root)
        map_window.title("Dungeon complete map")

        map_window.geometry("400x400")

        # print(map.get_rows()) # debug
        # print(map.get_cols()) # debug
        # print(dungeon.total_rows)
        # print(dungeon.total_columns)

        print(dungeon.get_visible_dungeon_string())  # debug


        for row in range(0, map.get_rows()):
            for col in range(0, map.get_cols()):
                b = Button(map_window)
                b.img = PhotoImage()
                b.config(height=400/(map.get_cols()+1), width=400/(map.get_rows()+1), image=b.img, compound=CENTER)
                # b.grid(row=int(row / 3), column=int(col % 3))
                b.grid(row=int(row), column=int(col))
                b.grid(sticky="NWSE")


        close_map_window = Button(map_window, text="Close Map", command=map_window.destroy)
        close_map_window.place(relx=0.5, rely=0.9)

class DungeonBrawler(BaseFrame):
    def setup(self):
        self.dungeon_brawl_frame = Frame(self.root)
        self.adventurer_frame = Frame(self.dungeon_brawl_frame, width = 400, height = 400, bg = "green")
        self.monster_frame = Frame(self.dungeon_brawl_frame, width = 400, height = 400, bg = "red")
        self.combat = Frame(self.dungeon_brawl_frame, width = 800, height = 200, bg = "blue")
        
        self.adventurer_frame.pack(side=LEFT, fill=X)
        self.monster_frame.pack(side=RIGHT, fill=X)
        self.combat.pack(side=BOTTOM, fill = Y)
        
        self.dungeon_brawl_frame.pack()

    def set_monster(self):
        pass

    def set_hero(self):
        pass

    def set_combat(self):
        pass

    def update_monster(self, controller):
        pass

    def update_hero(self, controller):
        pass

    def update_combat(self, controller):
        pass

if __name__ == "__main__":
    test = DungeonBrawler()
    test.setup()
    test.start_main_loop()
