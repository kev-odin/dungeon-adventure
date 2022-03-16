from tkinter import *
import tkinter as tk
import os
# TODO: About, Directions, Some clean-up with view components.
class BaseFrame(tk.Frame):
    def __init__(self):
        self.root = Tk()
        self.root.resizable(height = False, width = False)
        self.root.title("Dungeon Adventure 2.0")
        self.root.geometry("800x600")
        self.controller = None
        self.basic_menu_bar()

        # add a dictionary for the end of game summary
        self.player_stats = {
                "game difficulty setting"       : "", #done
                "hero max hit points"           : 0, #done
                "hero current hit points"       : 0,# done
                "health potions used"           : 0,#done
                "health potions left"           : 0,#done
                "vision potions used"           : 0,#done
                "vision potions left"           : 0,  #done
                "moves to exit"                 : -1,# done
                "map opened"                    : 0,# done
                "pillars collected"             : 0,# done
            }

    def destruct(self):
        self.root.destroy()

    def start_main_loop(self):
        self.root.mainloop()

    def set_controller(self, controller):
        self.controller = controller

    def basic_menu_bar(self):
        menubar = Menu()

        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "New game", command= lambda: self.controller.start_new(self.root))
        filemenu.add_command(label = "Save game", command= lambda: self.controller.save_game())
        filemenu.add_command(label = "Load game", command= lambda: self.controller.load_game(self.root))
        filemenu.add_command(label = "Quit game", command= lambda: self.destruct())

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

    # def update_display(self, controller):
    #     canvas = self.root
    #     dungeon = LabelFrame(canvas, width = 600, height = 400, bg = "White")
    #     text = Label(dungeon, text = f"{controller}", bg = "White")
    #     text.place(relx = 0.5, rely = 0.5, anchor = N)

    def adventurer_action(self):
        """Display base actions such as map and bag inventory
        """
        canvas = self.dungeon_crawl_canvas
        bag = Button(canvas, text= "Bag", command= lambda: self.controller.update_adv_bag())
        map = Button(canvas, text= "Map", command= lambda: self.controller.update_adv_map())
        
        bag.grid(row=2, column=0, sticky="nswe")
        map.grid(row=3, column=0, sticky="nswe")

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
            command= lambda: [ self.controller.set_move("n"),self.controller.update_dungeon_display(),
                               update_navigation(nav_group,self.controller.get_current_doors()),
                               self.controller.update_win_message()])
        travel_south = Button(
            canvas, 
            text="South", 
            command= lambda: [ self.controller.set_move("s"),self.controller.update_dungeon_display(),
                               update_navigation(nav_group,self.controller.get_current_doors()),
                               self.controller.update_win_message()])
        travel_west = Button(
            canvas,
            text="West", 
            command= lambda: [ self.controller.set_move("w"),self.controller.update_dungeon_display(),
                               update_navigation(nav_group,self.controller.get_current_doors()),
                               self.controller.update_win_message()])
        travel_east = Button(
            canvas, 
            text="East", 
            command= lambda: [ self.controller.set_move("e"),self.controller.update_dungeon_display(),
                               update_navigation(nav_group,self.controller.get_current_doors()),
                               self.controller.update_win_message()])

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
        self.player_stats["moves to exit"] += 1 # step counter for the end game summary

        # use the map size to update the diff level
        if len(map.visited_array()) == 5:
            self.player_stats["game difficulty setting"] = "Easy"
        elif len(map.visited_array()) == 8:
            self.player_stats["game difficulty setting"] = "Medium"
        elif len(map.visited_array()) == 10:
            self.player_stats["game difficulty setting"] = "Hard"
        else:
            self.player_stats["game difficulty setting"] = "Inhumane"


        canvas = self.root
        labelFrame_width = 300
        labelFrame_height = 300
        adjacent_rooms_frame = LabelFrame(canvas, width = labelFrame_width, height = labelFrame_height)
        adjacent_rooms_canvas = Canvas(adjacent_rooms_frame, width = 300, height = 300, bg = "grey")
        box_width = labelFrame_width/3
        box_height = labelFrame_height/3

        # create a 3x3 grid to show the dungeon
        for i in range(3):
            for j in range(3):
                adjacent_rooms_canvas.create_rectangle(box_width * (j) + 2, box_height * (i) + 2,
                                                       box_width * (j + 1),
                                                       box_height * (i + 1), width=3)

        # use the adventurer's loc to try the doors, if there is a door then print white room to that direction
        x_adv_loc = adv_telemetry.adventurer_loc[0]
        y_adv_loc = adv_telemetry.adventurer_loc[1]

        # update the map's visited rooms, so that we can use to print the traveled room
        map.set_visited_room(x_adv_loc, y_adv_loc)

        for try_door in ['north', 'south', 'east', 'west']:
            if adv_telemetry.get_room([x_adv_loc, y_adv_loc]).get_door(try_door):
                if try_door == 'north':
                    adjacent_rooms_canvas.create_rectangle(box_width * (1),
                                                           box_height * (0),
                                                           box_width * (2),
                                                           box_height * (1), width=3, fill='white')
                if try_door == 'south':
                    adjacent_rooms_canvas.create_rectangle(box_width * (1),
                                                           box_height * (2),
                                                           box_width * (2),
                                                           box_height * (3), width=3, fill='white')
                if try_door == 'east':
                    adjacent_rooms_canvas.create_rectangle(box_width * (2),
                                                          box_height * (1),
                                                          box_width * (3),
                                                          box_height * (2), width=3, fill='white')
                if try_door == 'west':
                    adjacent_rooms_canvas.create_rectangle(box_width * (0),
                                                           box_height * (1),
                                                           box_width * (1),
                                                           box_height * (2), width=3, fill='white')




        # print a hero image at the center of the 3x3 grid, potentially we can print different types of hero
        global img
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "image assets/priest.gif") # debug
        img = PhotoImage(file=path)
        img = img.subsample(9)
        adjacent_rooms_canvas.create_image(151, 151, image=img)

        # print a purple circle at the center of the 3x3 grid to represent the hero
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
                self.player_stats["health potions used"] += 1
            elif potion_type == "Vision":
                curr_count = self.controller.get_vision_pots()
                self.player_stats["vision potions used"] += 1

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
                health_lbl = Label(
                    potion_frame,
                    text = f"Health Potion Count: {bag_stuff['health']}",
                    padx = 10
                    )

                use_health = Button(
                    potion_frame,
                    text="Use Health Potion",
                    command = lambda: [
                        self.controller.set_potion("health"),
                        update_counter(health_lbl, use_health, "Health")
                        ])

                health_lbl.grid(row=0, column=0)
                use_health.grid(row=0, column=1)

            if bag_stuff["vision"]:
                vision_lbl = Label(
                    potion_frame,
                    text = f"Vision Potion Count: {bag_stuff['vision']}",
                    padx = 10
                    )
                use_vision = Button(
                    potion_frame,
                    text="Use Vision Potion",
                    command = lambda: [
                        self.controller.set_potion("vision"),
                        update_counter(vision_lbl, use_vision, "Vision")])

                vision_lbl.grid(row=1, column=0)
                use_vision.grid(row=1, column=1)

    def set_map_display(self, map, dungeon):
        self.player_stats['map opened'] += 1 # update how many times map was opened for the end game summary
        map_window = Toplevel(self.root)
        map_window.title("Dungeon complete map")
        map_window.geometry("420x420")  # window dimension 20 pixel greater than canvas, for the display purpose
        canvas_width = "400"
        canvas_height = "400"
        map_canvas = Canvas(map_window, width=canvas_width, height=canvas_height)

        print(map.visited_array()) # we can use this to display or cover the rooms

        rows = map.get_rows()
        box_width = int(canvas_width)/rows
        cols = map.get_cols()
        box_height = int(canvas_height)/cols

        # create the boxes of the dungeon, original dungeon missing the very top and left boarder. might be a tkinter thing.
        for i in range(rows):
            for j in range(cols):
                map_canvas.create_rectangle(box_width * j + 2, box_height * i + 2, box_width * (j + 1), box_height * (i + 1), width=3)

        # Traverse through the 2d array and draw component of the room
        for i in range(rows):
            for j in range(cols):

                # We only print the rooms that is already traveled. Or we get get rid of it by printing everything of the dungeon.
                if map.visited_array()[i][j]:

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

    def set_win_message(self, dungeon, hero, parent):
        '''display the winning message or lost message
        :para dungeon
        :para hero the adventurer
        '''
        if hero.current_hitpoints > 0:
            if dungeon.adventurer_loc == dungeon.exit:
                if hero.has_all_pillars():

                    # update for the end game summary
                    self.player_stats["pillars collected"] = True # update if all pillars collected for the end game summary
                    self.player_stats["hero current hit points"] = hero.current_hitpoints
                    self.player_stats["health potions left"] = hero.health_pots
                    self.player_stats["vision potions left"] = hero.vision_pots
                    self.player_stats["hero max hit points"] = hero.max_hitpoints

                    for widget in self.root.winfo_children():
                        widget.destroy()
                    win_message = Message(self.root, text=f"Congrats, you win, {hero.name}!", width=800)
                    win_message.config(bg='lightgreen', font=('times', 50, 'italic'))
                    win_message.pack(side=tk.TOP)

                    description_frame = LabelFrame(self.root, text=f"{hero.name}'s end-game summary")
                    stats_message = Message(description_frame, text=self.print_win_lose_summary(), width=700)
                    stats_message.config(bg='yellow', font=('times', 20, 'italic'))
                    stats_message.pack()
                    description_frame.pack(pady = 50)

                    canvas = self.root

                    new_game_btn = Button(canvas, text="New Game", command=lambda: self.controller.start_new(self.root))
                    load_game_btn = Button(canvas, text="Load Game", command=lambda: self.controller.load_game(parent))
                    quit_game_btn = Button(canvas, text="Quit Game", command=lambda: self.destruct())

                    new_game_btn.place(relx=0.5, rely=0.74, anchor = CENTER)
                    load_game_btn.place(relx=0.5, rely=0.82, anchor = CENTER)
                    quit_game_btn.place(relx=0.5, rely=0.9, anchor = CENTER)

    def set_lose_message(self, hero, parent):
        for widget in parent.winfo_children():
            widget.destroy()
        lose_message = Message(parent, text=f"Sorry, you lost, {hero.name}!", width=800)
        lose_message.config(bg='red', font=('times', 50, 'italic'))
        lose_message.pack(side=tk.TOP)

        description_frame = LabelFrame(self.root, text=f"{hero.name}'s end-game summary")
        stats_message = Message(description_frame, text=self.print_win_lose_summary(), width=700)
        stats_message.config(bg='yellow', font=('times', 20, 'italic'))
        stats_message.pack()
        description_frame.pack(pady=50)

        canvas = self.root

        new_game_btn = Button(canvas, text="New Game", command=lambda: self.controller.start_new(self.root))
        load_game_btn = Button(canvas, text="Load Game", command=lambda: self.controller.load_game(parent))
        quit_game_btn = Button(canvas, text="Quit Game", command=lambda: self.destruct())

        new_game_btn.place(relx=0.5, rely=0.74, anchor=CENTER)
        load_game_btn.place(relx=0.5, rely=0.82, anchor=CENTER)
        quit_game_btn.place(relx=0.5, rely=0.9, anchor=CENTER)

    def print_win_lose_summary(self):
        win_lose_summary = ""
        for key, value in self.player_stats.items():
            if key != "pillars collected":
                curr = str(key).capitalize() + ' : ' + str(value) + "\n"
            else:
                curr = str(key).capitalize() + ' : ' + str(value)
            win_lose_summary += curr
        return win_lose_summary

class DungeonBrawler(BaseFrame):
    def __init__(self):
        super(DungeonBrawler, self).__init__()

    def setup(self, controller, hero, monster):
        """Builds the basic frames for combat between the hero and the monster.
        """
        self.root.title("Dungeon Adventure 2.0 - DungeonBrawler")
        self.dungeon_brawl_frame = Frame(self.root)
        self.controller = controller
        
        self.left_frame = Frame(self.dungeon_brawl_frame, width = 400, height = 400, bg = "green")
        self.right_frame = Frame(self.dungeon_brawl_frame, width = 400, height = 400, bg = "red")
        self.combat_log = Frame(self.dungeon_brawl_frame, width = 800, height = 200, bg = "blue")
        self.combat_action = Frame(self.dungeon_brawl_frame, width= 400, height = 200, bg = "white")

        self.left_frame['relief'] = SUNKEN
        self.right_frame['relief'] = SUNKEN
        self.combat_log['relief'] = SUNKEN
        self.combat_action['relief'] = SUNKEN

        self.left_frame['borderwidth'] = 10
        self.right_frame['borderwidth'] = 10
        self.combat_log['borderwidth'] = 10
        self.combat_action['borderwidth'] = 10

        self.left_frame.grid(row = 0, column= 0)
        self.right_frame.grid(row = 0, column= 1)
        self.combat_action.grid(row = 1, columnspan=2)
        self.combat_log.grid(row = 2, columnspan=2)
        
        self.set_combat_action(self.combat_action, hero, monster)
        self.create_combat_log(self.combat_log)
        self.create_hero_frame(self.left_frame, hero)
        self.create_monster_frame(self.right_frame, monster)

        self.dungeon_brawl_frame.pack()
    
    def update_labels(self, *args):
        """Function to help with dynamically update labels during combat phase.
        :param: *args include self.hero_hp, self.health_pot, and self.monster_hp
        """
        for label in args:
            if label is self.hero_hp:
                new_max = self.controller.get_hero_max_hp()
                new_hp = self.controller.get_hero_curr_hp()
                label["text"] = f"Health: {new_hp}/{new_max}"

            if label is self.health_pot:
                new_pots = self.controller.get_health_pots()
                label["text"] = f"Health Potions: {new_pots}"

            if label is self.monster_hp:
                new_hp = self.controller.get_monster().current_hitpoints
                max_hp = self.controller.get_monster().max_hitpoints
                label["text"] = f"Health: {new_hp} / {max_hp}"

    def create_hero_frame(self, parent, hero):
        """Grouping the relevant labels together in a single parent frame(self.left_frame)
        for the hero combatant.
        """       
        self.hero_hp = Label(
            parent, 
            text = f"Health: {hero.current_hitpoints}/{hero.max_hitpoints}"
            )

        self.health_pot = Label(
            parent,
            text = f"Health Potions: {hero.health_pots}"
        )
        
        hero_name = Label(
            parent, 
            text = f"Name: {hero.name}"
            )
        
        attack_sp = Label(
            parent,
            text = f"Attack Speed: {hero.attack_speed}"
        )

        hit_chance = Label(
            parent,
            text = f"Hit Chance: {hero.hit_chance}"
        )
        
        self.hero_hp.grid(row=1, column=0)
        self.health_pot.grid(row=2, column=0)

        hero_name.grid(row=0, column=0)
        attack_sp.grid(row=3, column=0)
        hit_chance.grid(row=4, column=0)

    def create_monster_frame(self, parent, monster):
        """Grouping the relevant labels together in a single parent frame(self.right_frame)
        for the monster combatant.
        """                
        self.monster_hp = Label(
            parent,
            text = f"Health: {monster.current_hitpoints} / {monster.max_hitpoints}"
            )

        monster_name = Label(
            parent, 
            text = f"Monster Type: {monster.name}")
        
        monster_hit_chance = Label (
            parent,
            text = f"Hit Chance: {monster.hit_chance}"
        )

        attack_sp = Label(
            parent,
            text = f"Attack Speed: {monster.attack_speed}"
        )

        hit_chance = Label(
            parent,
            text = f"Hit Chance: {monster.hit_chance}"
        )

        self.monster_hp.grid(row=1, column=0)
        
        monster_name.grid(row=0, column=0)
        monster_hit_chance.grid(row=2, column=0)
        attack_sp.grid(row=3, column=0)
        hit_chance.grid(row=4, column=0)

    def create_combat_log(self, parent):
        """Creating the combat log on DungeonBrawler frame.

        :param parent: existing frame that will keep the Combat ListBox object
        """

        canvas = parent
        text = Label(canvas, text = "Combat Log")
        self.text_log = Listbox(canvas)

        text.grid(row=0)
        self.text_log.grid(row=1)

    def update_combat_log(self, event):
        """Erases previous entries and repopulates the ListBox in reverse order.
        Most recent actions are displayed on top.

        :param event: combat actions that have occured and captured between the model and user
        :type event: list
        """
        self.text_log.delete(0, END)
        self.text_log.grid_forget()
        text_box_width = len(max(event, key=len))

        for idx, event in enumerate(event[::-1], start = 1):
            self.text_log.insert(idx, event)
        
        self.text_log["width"] = text_box_width
        self.text_log.grid(row=1)

    def set_combat_action(self, parent, hero, monster):
        """Enable valid button states for the hero while in combat with the monster.
        Main entry for the user to interact with the model.

        :param parent: placeholder for the existing combat action frames.
        :param hero: Current hero combatant
        :param monster: Current monster combatant
        """

        def potion_state(button):
            current_potion = self.controller.get_health_pots()
            if current_potion == 0:
                button["state"] = DISABLED
            else:
                button["state"] = ACTIVE

        attack = Button(
            parent, 
            text="Attack", 
            command= lambda: [
                self.controller.set_action("attack", hero, monster),
                self.update_labels(self.hero_hp, self.monster_hp)
                ])
        
        special = Button(
            parent, 
            text=f"{hero.special}", 
            command= lambda: [
                self.controller.set_action("special", hero, monster),
                self.update_labels(self.hero_hp, self.monster_hp)
                ])
        
        health_potion = Button(
            parent, 
            text= "Use Health Potion", 
            command= lambda: [
                self.controller.set_potion("health"),
                potion_state(health_potion),
                self.update_labels(self.hero_hp, self.health_pot)
                ])

        end_combat = Button(
            parent,
            text="DEBUG - SKIP COMBAT",
            bg="orange",
            command= lambda: [self.controller.end_combat()]
        )

        potion_state(health_potion)

        attack.grid(row=0, column=0)
        special.grid(row=0, column=1)
        health_potion.grid(row=0, column=2)
        end_combat.grid(row=0, column=3)

    def set_crawler_update(self):
        self.combat_action.grid_forget()
        self.crawler = Frame(self.dungeon_brawl_frame)
        back_to_crawler = Button(
            self.crawler,
            text="Return to Dungeon",
            bg="green",
            command= lambda: [self.controller.end_combat()]
        )
        back_to_crawler.grid(row=0)
        self.crawler.grid(row=3)
