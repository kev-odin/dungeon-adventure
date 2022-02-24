from tkinter import *
import tkinter as tk

class BaseFrame(tk.Frame):
    def __init__(self):
        self.root = Tk()
        self.root.resizable(height = False, width = False)
        self.root.title("Dungeon Adventure 2.0 - The Spoony Bard Returns")
        self.root.geometry("800x600")
        self.basic_menu_bar()

    def destruct(self):
        self.root.destroy()

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
        global pop2
        pop2 = Toplevel(self.root)
        pop2.geometry("750x450")
        pop2.resizable(width=False, height=False)
        pop2.title("Load Game")

        btn3 = Button(pop2, text="Confirm Load", command = pop2.destroy).place(relx=0.75, rely=0.9)
        btn3.pack(self.root)

class DungeonCrawler(BaseFrame):
    def setup(self, controller):
        self.dungeon_crawl_frame = Frame(self.root)
        self.dungeon_crawl_canvas = Canvas(self.dungeon_crawl_frame, width=800, height=600, bg = "grey")
        self.adventurer_canvas = Canvas(self.dungeon_crawl_frame, width = 400, height = 600, bg = "black")

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
        map = Button(canvas, text= "Map", command = lambda: controller.still_playing())
        
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

        travel_north = Button(canvas, text="North", command= lambda: controller.update_view())
        travel_south = Button(canvas, text="South", command= lambda: controller.update_view())
        travel_west = Button(canvas, text="West", command= lambda: controller.update_view())
        travel_east = Button(canvas, text="East", command= lambda: controller.update_view())

        travel_north.grid(row=2, column=1)
        travel_south.grid(row=2, column=2)
        travel_west.grid(row=2, column=3)
        travel_east.grid(row=2, column=4)

        canvas.pack()

    def set_dungeon_display(self, local_rooms):
        """Display the current dungeon visual to player in the Dungeon Crawler Frame
        """
        canvas = self.root
        
        dungeon = LabelFrame(canvas, width = 400, height = 400, bg = "White")
        text = Label(dungeon, text = "Place Maze Here...", bg = "White")

        dungeon.place(relx = 0.5, rely = 0.25, anchor = N)
        text.place(relx = 0.5, rely = 0.5, anchor = N)

    def set_bag_display(self, bag):
        bag = Toplevel(self.root)
        bag.title("Adventurer Inventory")
        bag.geometry("400x400")
        print(bag)
        close_bag = Button(bag, text="Close Bag", command = self.destruct)
        close_bag.place(relx=0.4, rely=0.9)

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

if __name__ == "__main__":
    test = DungeonBrawler()
    test.setup()
    test.start_main_loop()
