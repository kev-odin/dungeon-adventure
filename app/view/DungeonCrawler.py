from tkinter import *

class DungeonCrawler:
    def __init__(self):
        self.root = Tk()  # create the root window
        self.root.title("Dungeon Adventure 2.0 - The Spoony Bard Returns")
        self.root.geometry("800x600")
        self.dungeon_crawl_frame = Frame(self.root)  # create a frame within that root window
        self.dungeon_crawl_canvas = Canvas(self.dungeon_crawl_frame, width=800, height=600, bg = "grey") # canvas within that frame
        
        self.basic_menu_bar()
        self.dungeon_navigation()
        self.adventurer_action()
        self.dungeon_display()
        self.dungeon_crawl_frame.pack()
        self.root.mainloop()

    def basic_menu_bar(self):
        menubar = Menu()

        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "New game...")
        filemenu.add_command(label = "Save game")
        filemenu.add_command(label = "Load game")
        filemenu.add_command(label = "Quit game", command=self.root.destroy)

        menubar.add_cascade(label = "File", menu = filemenu)

        help = Menu(menubar, tearoff = 0)
        help.add_command(label = "About Us")
        help.add_command(label = "Controls")
        
        menubar.add_cascade(label = "Help", menu = help)

        self.root.config(menu = menubar)

    def dungeon_navigation(self):
        canvas = self.dungeon_crawl_canvas

        travel_north = Button(canvas, text="North")
        travel_south = Button(canvas, text="South")
        travel_west = Button(canvas, text="West")
        travel_east = Button(canvas, text="East")

        travel_north.grid(row=0, column=0)
        travel_south.grid(row=0, column=1)
        travel_west.grid(row=0, column=2)
        travel_east.grid(row=0, column=3)

        canvas.pack()

    def bag_display(self):
        global bag  # to make it accessiable to other functions, otherwise tkinter won't work in our way
        bag = Toplevel(self.root)
        bag.title("Adventurer Inventory")
        bag.geometry("600x300")

        close_bag = Button(bag, text="Close Bag", command = bag.destroy)
        close_bag.place(relx=0.75, rely=0.9)
        
        close_bag.pack()

    def adventurer_action(self):
        canvas = self.dungeon_crawl_canvas
        bag = Button(canvas, text= "Bag", command = self.bag_display)
        map = Button(canvas, text="Map")
        
        bag.grid(row=1, column=0)
        map.grid(row=1, column=1)

        canvas.pack()

    def dungeon_display(self):
        canvas = self.dungeon_crawl_canvas
        
        dungeon = Frame(self.root, height=400, width=600, bg = "White")
        text = Label(dungeon, text = "Place Maze Here...", bg = "White")

        text.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        dungeon.place(relx = 0.1, rely = 0.15)
        canvas.pack()



if __name__ == "__main__":
    game = DungeonCrawler()
