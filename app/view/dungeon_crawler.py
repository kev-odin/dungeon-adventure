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
        map = Button(canvas, text= "Map", command= lambda: self.controller.update_adv_map())
        
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

    def set_dungeon_display(self, map, adv_telemetry):
        """Display the current dungeon visual to player in the Dungeon Crawler Frame
        """
        canvas = self.root
        labelFrame_width = 300
        labelFrame_height = 300
        adjacent_rooms_frame = LabelFrame(canvas, width = labelFrame_width, height = labelFrame_height, bg = "White")
        adjacent_rooms_canvas = Canvas(adjacent_rooms_frame, width = 300, height = 300, bg = "black")
        box_width = labelFrame_width/3
        box_height = labelFrame_height/3

        for i in range(3):
            for j in range(3):
                # create a 3x3 grid to show the dungeon
                adjacent_rooms_canvas.create_rectangle(box_width * (j) + 2, box_height * (i) + 2,
                                                       box_width * (j + 1),
                                                       box_height * (i + 1), width=3)



        x_offset = adv_telemetry.adventurer_loc[0] - 1
        y_offset = adv_telemetry.adventurer_loc[1] - 1

        for i in range(adv_telemetry.adventurer_loc[0] - 1, adv_telemetry.adventurer_loc[0] + 2):
            for j in range(adv_telemetry.adventurer_loc[1] - 1, adv_telemetry.adventurer_loc[1] + 2):

                if not map.visited_array()[i][j]:

                    adjacent_rooms_canvas.create_rectangle(box_width * (j - x_offset) + 2,
                                                           box_height * (i - y_offset) + 2,
                                                           box_width * (j - x_offset + 1),
                                                           box_height * (i - y_offset + 1), width=3,fill='grey')


        print('map.visited 2d array:')
        print(map.visited_array())

        print(map.visited_array()[adv_telemetry.adventurer_loc[0] - 1][adv_telemetry.adventurer_loc[1] - 1])

        print("set_dungeon_display print adv_loc:")
        print(adv_telemetry.adventurer_loc)
        print((adv_telemetry.adventurer_loc[0] - 1, adv_telemetry.adventurer_loc[1]- 1)) # top left
        print((adv_telemetry.adventurer_loc[0] - 1, adv_telemetry.adventurer_loc[1] ))  # top middle
        print((adv_telemetry.adventurer_loc[0] - 1, adv_telemetry.adventurer_loc[1] +1))  # top right

        # base_dir = os.path.dirname(os.path.abspath(__file__))
        # path = os.path.join(base_dir, "image assets/priest.gif") # debug
        # img = PhotoImage(file=path)
        # adjacent_rooms_canvas.create_image(125, 125, image=img, anchor='nw')

        # print a purple circle on the 3x3 grid to represent the hero
        # adjacent_rooms_canvas.create_oval(125, 125, 175, 175, fill="purple")

        # greyed out the box if that room is no traveled yet

        # adjacent_rooms_canvas.create_rectangle(0, 0, box_width * (1),
        #                                        box_height * (1), width=3, fill = 'grey')


        # print(adv_telemetry.get_room(adv_telemetry.adventurer_loc)) # this get room will return a room(string)
        # print(adv_telemetry.get_room(adv_telemetry.adventurer_loc).string_top())

        # print a purple circle on the 3x3 grid to represent the hero, no matter what it is centered
        adjacent_rooms_canvas.create_oval(125, 125, 175, 175, fill="purple")

        # use the adventurer_loc from the dungeon class to update the current dungeon display window
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
        self.root.title("Dungeon Adventure 2.0 - DungeonCrawler")
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
