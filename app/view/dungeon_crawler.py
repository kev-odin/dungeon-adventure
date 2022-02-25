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
        global pop2
        pop2 = Toplevel(self.root)
        pop2.geometry("750x450")
        pop2.resizable(width=False, height=False)
        pop2.title("Load Game")
        # "A--B--C--D"

        # open up
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
        
        dungeon = LabelFrame(canvas, width = 300, height = 300, bg = "White")
        # text = Label(dungeon, text = "Place Maze Here...", bg = "White")

        for i in range(9):
            b = 'b'+str(i)
            if (b == 'b4'):
                b = Button(dungeon)
                b.img = PhotoImage(file='/Users/hxg/Library/Mobile Documents/com~apple~CloudDocs/Desktop/UniversityOfWashington/TCSS504Winter/Assignment9-Groupwork/The_Spoony_Bard/app/view/image assets/priest.gif')
                # b.ima = PhotoImage()
                b.img2 = b.img.subsample(10, 10)
                b.config(height=100, width=100, image=b.img2)
                b.grid(row=int(i/3), column=int(i%3))
                b.grid(sticky = "NWSE")
            else:
                b = Button(dungeon)
                b.img = PhotoImage()
                b.config(height=100, width=100, image=b.img, compound=CENTER)
                b.grid(row=int(i / 3), column=int(i % 3))
                b.grid(sticky="NWSE")

        # b1 = Button(dungeon)
        # b1.img = PhotoImage()
        # b1.config(height=100, width=100, image=b1.img, compound=CENTER)
        # b1.grid(row=0, column=0)
        #
        # b2 = Button(dungeon)
        # b2.img = PhotoImage()
        # b2.config(height=100, width=100, image=b2.img, compound=CENTER)
        # b2.grid(row=0, column=1)
        #
        # b3 = Button(dungeon)
        # b3.img = PhotoImage()
        # b3.config(height=100, width=100, image=b3.img, compound=CENTER)
        # b3.grid(row=0, column=2)
        #
        # b4 = Button(dungeon)
        # b4.img = PhotoImage()
        # b4.config(height=100, width=100, image=b4.img, compound=CENTER)
        # b4.grid(row=1, column=0)
        #
        # b5 = Button(dungeon)
        # b5.img = PhotoImage()
        # b5.config(height=100, width=100, image=b5.img, compound=CENTER)
        # b5.grid(row=1, column=1)
        #
        # b6 = Button(dungeon)
        # b6.img = PhotoImage()
        # b6.config(height=100, width=100, image=b6.img, compound=CENTER)
        # b6.grid(row=1, column=2)

        dungeon.place(relx = 0.5, rely = 0.25, anchor = N)
        # text.place(relx = 0.5, rely = 0.5, anchor = N)

    def set_bag_display(self, bag):
        bag = Toplevel(self.root)
        bag.title("Adventurer Inventory")
        bag.geometry("400x400")
        print(bag)
        close_bag = Button(bag, text="Close Bag", command = bag.destroy)
        # close_bag = Button(bag, text="Close Bag", command = bag.destruct())
        close_bag.place(relx=0.4, rely=0.9)

    def set_map_display(self, map):
        map = Toplevel(self.root)
        map.title("Dungeon complete map")
        map.geometry("600x600")
        close_map = Button(map, text="Close Map", command=map.destroy)
        close_map.place(relx=0.4, rely=0.9)

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

    test2 = DungeonCrawler()
    test2.set_dungeon_display()

