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
        text = Label(adjacent_rooms, text = "Place Maze Here...", bg = "White")

        # print(adv_telemetry.get_room(adv_telemetry.adventurer_loc)) # this get room will return a room(string)
        # print(adv_telemetry.get_room(adv_telemetry.adventurer_loc).string_top())

        for i in range(9):
            b = 'b'+str(i)
            if (b == 'b4'):
                b = Button(adjacent_rooms)
                b.img = PhotoImage(file='/Users/hxg/Library/Mobile Documents/com~apple~CloudDocs/Desktop/UniversityOfWashington/TCSS504Winter/Assignment9-Groupwork/The_Spoony_Bard/app/view/image assets/priest.gif')
                # b.img = PhotoImage()
                b.img = b.img.subsample(10, 10)
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
        map_window.geometry("420x420")  # window dimension 20 pixel greater than canvas, for the display purpose
        canvas_width = "400"
        canvas_height = "400"
        map_canvas = Canvas(map_window, width=canvas_width, height=canvas_height)
        # print(map.visited_array()) # we can use this to display or cover the rooms
        rows = map.get_rows()
        box_width = int(canvas_width)/rows
        cols = map.get_cols()
        box_height = int(canvas_height)/cols

        # create the boxes of the dungeon, original dungeon missing the very top and left boarder. might be a tkinter thing.
        for i in range(rows):
            for j in range(cols):
                # (box_width)*j+2 to make sure the very left and top boarder is also printed
                map_canvas.create_rectangle(box_width * j + 2, box_height * i + 2, box_width * (j + 1), box_height * (i + 1), width=3)
                # map_canvas.create_rectangle((box_width) * j, (box_height) * i, box_width * (j + 1),
                                            # box_height * (i + 1), width=3)

        # Traverse through the 2d array and draw component of the room
        for i in range(rows):
            for j in range(cols):

                # create rectangle to represent doors
                for try_door in ['north', 'east', 'west', 'south']:
                    if dungeon.get_room([i,j]).get_door(try_door):
                        if try_door == 'east':
                            map_canvas.create_line(box_width * (j + 1), box_height * (i + 1 / 4), box_width * (j + 1),
                                                   box_height * (i + 3 / 4), width=10, fill='white')
                        if try_door == 'west':
                            map_canvas.create_line(box_width * (j), box_height * (i + 1 / 4), box_width * (j),
                                                   box_height * (i + 3 / 4), width=10, fill='white')
                        if try_door == 'north':
                            map_canvas.create_line(box_width * (j+1/4), box_height * (i), box_width * (j+3/4),
                                                   box_height * (i), width=10, fill='white')
                        if try_door == 'south':
                            map_canvas.create_line(box_width * (j + 1 / 4), box_height * (i+1), box_width * (j + 3 / 4),
                                                   box_height * (i + 1), width=10, fill='white')

                abbrevation_to_symbols = {
                    'i':('En','green'),
                    'O':('Ex','green'),
                    'H':('H','red'),
                    'V':('V','blue'),
                    'M':('M','yellow'),
                    'A':('A','purple'),
                    'P':('P','purple'),
                    'I':('I','purple'),
                    'E':('E','purple'),
                }

                if dungeon.get_room([i, j]).contents in abbrevation_to_symbols.keys():
                    text = abbrevation_to_symbols[dungeon.get_room([i, j]).contents][0]
                    color = abbrevation_to_symbols[dungeon.get_room([i, j]).contents][1]
                    map_canvas.create_text(box_width * (j + 1 / 4), box_height * (i + 1 / 4),
                                           text=text,
                                           fill=color, font=('Helvetica', '30', 'bold'))



                # if dungeon.get_room([i, j]).contents == 'i':
                #     # "i", "O", "H", "V", "X", "M", "A", "P", "I", "E","*"
                #     map_canvas.create_text(box_width * (j + 1 / 4), box_height * (i + 1 / 4),
                #                            text="En",
                #                            fill="green", font=('Helvetica', '30', 'bold'))
                # elif dungeon.get_room([i, j]).contents == 'O':
                #     map_canvas.create_text(box_width * (j + 1 / 4), box_height * (i + 1 / 4),
                #                            text="Ex",
                #                            fill="green", font=('Helvetica', '30', 'bold'))
                # elif dungeon.get_room([i, j]).contents == 'H':
                #     map_canvas.create_text(box_width * (j + 1 / 2), box_height * (i + 1 / 2),
                #                            text="H",
                #                            fill="red", font=('Helvetica', '30', 'bold'))
                # elif dungeon.get_room([i, j]).contents == 'V':
                #     map_canvas.create_text(box_width * (j + 1 / 2), box_height * (i + 1 / 2),
                #                            text="V",
                #                            fill="blue", font=('Helvetica', '30', 'bold'))
                # elif dungeon.get_room([i, j]).contents == 'M':
                #     map_canvas.create_text(box_width * (j + 1 / 2), box_height * (i + 1 / 2),
                #                            text="M",
                #                            fill="yellow", font=('Helvetica', '30', 'bold'))
                # elif dungeon.get_room([i, j]).contents == 'A':
                #     map_canvas.create_text(box_width * (j + 1 / 2), box_height * (i + 1 / 2),
                #                            text="A",
                #                            fill="purple", font=('Helvetica', '30', 'bold'))
                # elif dungeon.get_room([i, j]).contents == 'P':
                #     map_canvas.create_text(box_width * (j + 1 / 2), box_height * (i + 1 / 2),
                #                            text="P",
                #                            fill="purple", font=('Helvetica', '30', 'bold'))
                # elif dungeon.get_room([i, j]).contents == 'I':
                #     map_canvas.create_text(box_width * (j + 1 / 2), box_height * (i + 1 / 2),
                #                            text="I",
                #                            fill="purple", font=('Helvetica', '30', 'bold'))
                # elif dungeon.get_room([i, j]).contents == 'E':
                #     map_canvas.create_text(box_width * (j + 1 / 2), box_height * (i + 1 / 2),
                #                            text="E",
                #                            fill="purple", font=('Helvetica', '30', 'bold'))


        # create purple dot to represent adventurer
        x_adventurer_loc = dungeon.adventurer_loc[0]
        y_adventurer_loc = dungeon.adventurer_loc[1]
        map_canvas.create_oval(box_width * (y_adventurer_loc+1/4), box_height * (x_adventurer_loc+ 1/4),
                               box_width * (y_adventurer_loc+3/4),box_height * (x_adventurer_loc+ 3/4), fill="purple")

        # M stands for multiple items, H for health potion, V for vision potion
        # if dungeon.get_room([i, j]).health_potion and dungeon.get_room([i, j]).vision_potion:
        #     map_canvas.create_text(box_width * (j + 1 / 2), box_height * (i + 1 / 2),
        #                            text="M",
        #                            fill="green", font=('Helvetica', '30', 'bold'))
        # elif dungeon.get_room([i, j]).health_potion:
        #     map_canvas.create_text(box_width * (j + 1 / 2), box_height * (i + 1 / 2),
        #                            text="H",
        #                            fill="red", font=('Helvetica', '30', 'bold'))
        # elif dungeon.get_room([i, j]).vision_potion:
        #     map_canvas.create_text(box_width * (j + 1 / 2), box_height * (i + 1 / 2),
        #                            text="V",
        #                            fill="blue", font=('Helvetica', '30', 'bold'))



        # # create text "En" to represent entrance, "Ex" to represent exit
        # x_entrance_loc = dungeon.entrance[0]
        # y_entrance_loc = dungeon.entrance[1]
        # map_canvas.create_text(box_width *(y_entrance_loc+1/4), box_height * (x_entrance_loc+ 1/4), text = "En",
        #                        fill="green", font=('Helvetica','30','bold'))
        # x_exit_loc = dungeon.exit[0]
        # y_exit_loc = dungeon.exit[1]
        # map_canvas.create_text(box_width * (y_exit_loc + 1 / 4), box_height * (x_exit_loc + 1 / 4), text="Ex",
        #                        fill="green", font=('Helvetica', '30', 'bold'))



        # map_canvas.create_rectangle(box_width * 0, 0, box_width * 1, box_height)
        # map_canvas.create_rectangle(box_width * 1, 0, box_width * 2, box_height)
        # map_canvas.create_rectangle(box_width * 2, 0, box_width * 3, box_height)
        # map_canvas.create_rectangle(box_width * 3, 0, box_width * 4, box_height)
        # map_canvas.create_rectangle(box_width * 4, 0, box_width * 5, box_height)

        # map_canvas.create_rectangle(box_width * 0, box_height * 1, box_width * 1, box_height * 2)
        # map_canvas.create_rectangle(box_width * 1, box_height * 1, box_width * 2, box_height * 2)
        # map_canvas.create_rectangle(box_width * 2, box_height * 1, box_width * 3, box_height * 2)
        # map_canvas.create_rectangle(box_width * 3, box_height * 1, box_width * 4, box_height * 2)
        # map_canvas.create_rectangle(box_width * 4, box_height * 1, box_width * 5, box_height * 2)


        print(dungeon.get_visible_dungeon_string())  # debug

        map_canvas.pack()
        close_map_window = Button(map_window, text="Close Map", command=map_window.destroy)
        close_map_window.place(relx=1.0, rely=1.0, anchor=SE)

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
