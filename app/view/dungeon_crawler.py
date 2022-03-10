from tkinter import *
import tkinter as tk
import os

# TODO: Readable pillars in the bag view        - Done
# TODO: Ability to use items in the bag view    - Bug
# TODO: Item number not updating after use      - Bug
# TODO: Controller saving                       - Bug

class BaseFrame(tk.Frame):
    def __init__(self):
        self.root = Tk()
        self.root.resizable(height = False, width = False)
        self.root.title("Dungeon Adventure 2.0")
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
        filemenu.add_command(label = "Load game", command= lambda: self.controller.load_game(self.root))
        filemenu.add_command(label = "Quit game", command= self.root.destroy)

        menubar.add_cascade(label = "File", menu = filemenu)

        help = Menu(menubar, tearoff = 0)
        help.add_command(label = "About Us")
        help.add_command(label = "Controls")

        menubar.add_cascade(label = "Help", menu = help)

        self.root.config(menu = menubar)

class DungeonCrawler(BaseFrame):
    def __init__(self):
        super(DungeonCrawler, self).__init__()

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
        map = Button(canvas, text= "Map", command= lambda: self.controller.update_adv_map())
        
        bag.grid(row=2, column=0, sticky="nswe")
        map.grid(row=3, column=0, sticky="nswe")

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
        """Displays the navigation buttons for the DungeonCrawler view. Buttons are greyed out if a door is not present.
        """
        canvas = self.dungeon_crawl_canvas
        active_doors = self.controller.get_current_doors()

        def update_navigation(buttons, doors):
            for button in buttons:
                current_dir = button["text"].lower()
                
                if doors[current_dir]:
                    button["state"] = ACTIVE
                else:
                    button["state"] = DISABLED

        travel_north = Button(
            canvas,
            text="North",
            command= lambda: [self.controller.set_move("n"), self.controller.update_dungeon_display(), update_navigation(nav_group, self.controller.get_current_doors())])
        travel_south = Button(
            canvas, 
            text="South", 
            command= lambda: [self.controller.set_move("s"), self.controller.update_dungeon_display(), update_navigation(nav_group, self.controller.get_current_doors())])
        travel_west = Button(
            canvas,
            text="West", 
            command= lambda: [self.controller.set_move("w"), self.controller.update_dungeon_display(), update_navigation(nav_group, self.controller.get_current_doors())])
        travel_east = Button(
            canvas, 
            text="East", 
            command= lambda: [self.controller.set_move("e"), self.controller.update_dungeon_display(), update_navigation(nav_group, self.controller.get_current_doors())])

        nav_group = (travel_north, travel_south, travel_west, travel_east)
        update_navigation(nav_group, active_doors)

        travel_north.grid(row=1, column=2)
        travel_south.grid(row=3, column=2)
        travel_west.grid(row=2, column=1)
        travel_east.grid(row=2, column=3)

        canvas.pack()

    def set_dungeon_display(self, map, adv_telemetry):
        """Display the current dungeon visual to player in the Dungeon Crawler Frame
        """
        canvas = self.root
        labelFrame_width = 300
        labelFrame_height = 300
        adjacent_rooms_frame = LabelFrame(canvas, width = labelFrame_width, height = labelFrame_height, bg = "White")
        adjacent_rooms_canvas = Canvas(adjacent_rooms_frame, width = 300, height = 300, bg = "white")
        box_width = labelFrame_width/3
        box_height = labelFrame_height/3

        # create a 3x3 grid to show the dungeon
        for i in range(3):
            for j in range(3):
                adjacent_rooms_canvas.create_rectangle(box_width * (j) + 2, box_height * (i) + 2,
                                                       box_width * (j + 1),
                                                       box_height * (i + 1), width=3)

        # use the adventurer's loc to try the doors, if there is a door then print grey room to that direction
        x_adv_loc = adv_telemetry.adventurer_loc[0]
        y_adv_loc = adv_telemetry.adventurer_loc[1]
        for try_door in ['north', 'south', 'east', 'west']:
            if adv_telemetry.get_room([x_adv_loc, y_adv_loc]).get_door(try_door):
                if try_door == 'north':
                    adjacent_rooms_canvas.create_rectangle(box_width * (1),
                                                           box_height * (0),
                                                           box_width * (2),
                                                           box_height * (1), width=3, fill='grey')
                if try_door == 'south':
                    adjacent_rooms_canvas.create_rectangle(box_width * (1),
                                                           box_height * (2),
                                                           box_width * (2),
                                                           box_height * (3), width=3, fill='grey')
                if try_door == 'east':
                    adjacent_rooms_canvas.create_rectangle(box_width * (2),
                                                          box_height * (1),
                                                          box_width * (3),
                                                          box_height * (2), width=3, fill='grey')
                if try_door == 'west':
                    adjacent_rooms_canvas.create_rectangle(box_width * (0),
                                                           box_height * (1),
                                                           box_width * (1),
                                                           box_height * (2), width=3, fill='grey')


        print('map.visited 2d array:')
        print(map.visited_array())

        # print a hero image at the center of the 3x3 grid, potentially we can print different types of hero
        global img
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "image assets/priest.gif") # debug
        img = PhotoImage(file=path)
        img = img.subsample(10)
        adjacent_rooms_canvas.create_image(150, 150, image=img)

        # # print a purple circle at the center of the 3x3 grid to represent the hero
        # adjacent_rooms_canvas.create_oval(125, 125, 175, 175, fill="purple")

        adjacent_rooms_canvas.pack()
        adjacent_rooms_frame.place(relx = 0.5, rely = 0.25, anchor = N)

    def set_bag_display(self, bag_stuff):
        """Display the current hero bag to player

        :param bag_stuff: _description_
        :type bag_stuff: dictionary {pillars : {str : bool}, "health" : int, "vision" : int}
        """

        def update_counter(label, button, potion_type):

            if potion_type == "Health":
                curr_count = self.controller.get_health_pots()
            elif potion_type == "Vision":
                curr_count = self.controller.get_vision_pots()

            if curr_count == 0:
                button["state"] = DISABLED

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
                use_health = Button(potion_frame, text="Use Health Potion", command = lambda: [self.controller.set_potion("health"), update_counter(health_lbl, use_health, "Health")])

                health_lbl.grid(row=0, column=0)
                use_health.grid(row=0, column=1)

            if bag_stuff["vision"]:
                vision_lbl = Label(potion_frame, text = f"Vision Potion Count: {bag_stuff['vision']}", padx = 10)
                use_vision = Button(potion_frame, text="Use Vision Potion", command = lambda: [self.controller.set_potion("vision"), update_counter(vision_lbl, use_vision, "Vision")])

                vision_lbl.grid(row=1, column=0)
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
                # print(dungeon.get_room([i,j]))
                # print(type(dungeon.get_room([i, j])))
                if (dungeon.get_room([i, j]).monster):
                    print(dungeon.get_room([i, j]).monster.char_dict)

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

                # create letter represent the contents
                abbreviation_to_symbols = {
                    'i':('En','green'),
                    'O':('Ex','green'),
                    'H':('H','red'),
                    'V':('V','blue'),
                    'M':('M','orange'),
                    'A':('A','purple'),
                    'P':('P','purple'),
                    'I':('I','purple'),
                    'E':('E','purple'),
                }
                if dungeon.get_room([i, j]).contents in abbreviation_to_symbols.keys():
                    text = abbreviation_to_symbols[dungeon.get_room([i, j]).contents][0] # get the key value from the dictionary
                    color = abbreviation_to_symbols[dungeon.get_room([i, j]).contents][1] # get the key value from the dictionary
                    map_canvas.create_text(box_width * (j + 1 / 4), box_height * (i + 1 / 4),
                                           text=text,
                                           fill=color, font=('Helvetica', str(int(100/rows)), 'bold'))
                                            # "str(int(100/rows))" is used to adjust the font size according to the rows

                # create letter mstr to represent monsters in the room
                if (dungeon.get_room([i, j]).monster):
                    map_canvas.create_text(box_width * (j + 3 / 4), box_height * (i + 3 / 4),
                                           text='mstr',
                                           fill='red', font=('Helvetica', str(int(100 / rows))))


        # create purple dot to represent adventurer
        x_adventurer_loc = dungeon.adventurer_loc[0]
        y_adventurer_loc = dungeon.adventurer_loc[1]
        map_canvas.create_oval(box_width * (y_adventurer_loc+1/4), box_height * (x_adventurer_loc+ 1/4),
                               box_width * (y_adventurer_loc+3/4),box_height * (x_adventurer_loc+ 3/4), fill="purple")


        print(dungeon.get_visible_dungeon_string())  # debug

        map_canvas.pack()
        close_map_window = Button(map_window, text="Close Map", command=map_window.destroy)
        close_map_window.place(relx=1.0, rely=1.0, anchor=SE)

class DungeonBrawler(BaseFrame):
    def __init__(self):
        super(DungeonBrawler, self).__init__()

    def setup(self):
        self.dungeon_brawl_frame = Frame(self.root, width = 800, height = 600, bg = "black")
        self.root.title("Dungeon Adventure 2.0 - DungeonCrawler")
        left_frame = Frame(self.dungeon_brawl_frame, width = 400, height = 400, bg = "green")
        right_frame = Frame(self.dungeon_brawl_frame, width = 400, height = 400, bg = "red")
        combat_log = Frame(self.dungeon_brawl_frame, width = 400, height = 200, bg = "blue")
        combat_action = Frame(self.dungeon_brawl_frame, width= 400, height = 200, bg = "white")
        

        # self.create_hero_frame(left_frame, "hello")
        self.set_combat_action(combat_action)
        self.set_combat_log(combat_log)

        # left_frame.grid(row = 0, column= 0)
        # right_frame.grid(row = 0, column= 1)
        # combat_action.grid(row = 1, column=0)
        # combat_log.grid(row = 1, column= 1)


        # left_frame.pack(fill='both', side='left', expand='True')
        # right_frame.pack(fill='both', side='right', expand='True')

        left_frame.place(x=0, y= 0)
        right_frame.place(x = 400, y = 0)
        #
        combat_action.place(relx = 0.15, rely = 0.8)
        combat_log.place(relx = 0.5, rely = 0.7)

        self.dungeon_brawl_frame.pack()
    def create_hero_frame(self, parent, hero = None):
        hero_frame = Frame(parent)
        hero_label = Label(hero_frame, text = f"{hero}", bg="white")
        hero_frame.pack(side = TOP)
        hero_label.grid(row = 0, column=0)

    def set_monster(self, monster = None):
        monster_frame = Frame(self.right_frame)
        monster_label = Label(monster_frame, text = f"{monster}")
        monster_label.pack()

    def set_combat_log(self, parent_frame, event = None):
        canvas = parent_frame
        text = Text(canvas, height=10, width=55)
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
