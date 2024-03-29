# checkout Kevin shared site https://www.pythontutorial.net/tkinter/
# checkout this site https://www.youtube.com/watch?v=tpwu5Zb64lQ
from tkinter import *
from app.view.load_view import LoadView
import os.path


class dungeon_adventure_GUI:
    def setup(self, controller, root=None):
        if root is None:
            self.root = Tk()  # create the root window
        else:
            for widget in root.winfo_children():  # Clears screen
                widget.destroy()
            self.root = root
        self.root.title("Dungeon Adventure 2.0")
        self.root.resizable(width=False, height=False) # fixed size
        self.welcome_screen_frame = Frame(self.root)  # create a frame within that root window
        self.welcome_screen_canvas = Canvas(self.welcome_screen_frame,width=800, height=600, bg="white") # canvas within that frame
        self.welcome_window(controller)
        self.welcome_screen_frame.pack()
        self.__controller = controller

        self.settings = {
            "name"       : None,
            "difficulty" : None,
            "class_name" : None
        }

    def start_main_loop(self):
        self.root.mainloop()

    def destruct(self):
        self.root.destroy()

    def send_settings(self):
        return self.settings

    def send_to_controller(self, controller):
        controller.set_model()

    def create_new_game_window(self, controller):
        global game_difficulty  # global variable, look for details in def display_selected()
        global pop1  # to make it accessiable to other functions, otherwise tkinter won't work in our way
        pop1 = Toplevel(self.root)
        pop1.geometry("750x450")
        pop1.resizable(width=False, height=False)
        pop1.title("New Game")

        label1= Label(pop1, text="Select your game difficulty level")
        label1.pack()

        level_options = [
            "Easy",
            "Medium",
            "Hard",
            "Inhumane"
        ]
        level_options_description = {
            "Easy":"This is the easy mode. Your hero will be traveling through a 5x5 dungeon.",
            "Medium":"This is the medium mode. Your hero will be traveling through a 8x8 dungeon.",
            "Hard":"This is the hard mode.Your hero will be traveling through a 10x10 dungeon.",
            "Inhumane": "This is the Inhumane mode.Your hero will be traveling through a 20x20 dungeon."
        }

        clicked = StringVar()
        clicked.set(level_options[0]) # set the default greyed out level

        description_frame = Frame(pop1) # create a frame to hold label_frame1 and description_message

        def display_selected(selected):
            for widget in description_frame.winfo_children(): # Way to rewrite the label frame, looks for every child of frame
                widget.destroy()
            selected = clicked.get()
            self.settings["difficulty"] = selected # store the difficulty level in a variable

            label_frame1 = LabelFrame(description_frame, text=selected)
            label_frame1.pack()

            description_message = Message(label_frame1, text=level_options_description[selected], aspect=500)
            description_message.pack()


        option_menu1 = OptionMenu(pop1, clicked, *level_options, command=display_selected) # create a dropdown menu
        option_menu1.pack()

        lable2 = Label(pop1, text="Difficulty level descriptions:")
        lable2.pack()

        description_frame.pack() # pack it afterwards the line of "description_frame = Frame(pop1)"

        display_selected(clicked.get())

        btn2 = Button(pop1, text="Confirm New",command=lambda : self.get_adventurer_info(pop1, controller)).place(relx=0.75,rely=0.9)

    def get_adventurer_info(self, pop1, controller):
        for widget in pop1.winfo_children():  # Way to rewrite the label frame, looks for every child of frame
            widget.destroy()

        label3 = Label(pop1, text="Choose your hero's name:").pack()
        name = StringVar()
        hero_name = Entry(pop1, textvariable=name)
        hero_name.pack()

        label4 = Label(pop1, text="Choose your hero type:").pack()

        hero_options = [
            "Warrior",
            "Priestess",
            "Thief"
        ]
        hero_options_description = {
            "Warrior": "As the name suggests, this hero is so powerful and has a large hit points.",
            "Priestess": "Who doesn't want to be immune from all the attacks? This hero can heal herself with her special ability.",
            "Thief": "Special ability of this hero is to use sneak attack.  40% chance of doing two attacks.  20% chance of no attacks.  40% chance of normal attack"
        }

        clicked = StringVar()
        clicked.set(hero_options[0])  # set the default greyed out level

        hero_frame = Frame(pop1)

        def get_player_entered_name(): # we need this function because Entry widget requires storing the name in a functions.
            # we tried to just use .get(), but it seems that did not work. this is a work around.
            self.settings["name"] = hero_name.get()

        def display_selected_hero(selected):
            for widget in hero_frame.winfo_children(): # Way to rewrite the label frame, looks for every child of frame
                widget.destroy()
            selected = clicked.get()
            hero_type = selected
            # self.settings["name"] = hero_name             # Kevin - Setting NOT stored in dictionary to send to controller
            self.settings["class_name"] = hero_type         # Kevin - Setting stored in dictionary to send to controller

            label_frame2 = LabelFrame(hero_frame, text=selected)
            label_frame2.pack()

            hero_description = Message(label_frame2, text=hero_options_description[selected], aspect=500)
            hero_description.pack()

        option_menu2 = OptionMenu(pop1, clicked, *hero_options, command=display_selected_hero) # dropdown menu of hero types
        option_menu2.pack()

        hero_frame.pack()                       # we create the frame previously at line hero_frame = Frame(pop1), now we need pack()
        display_selected_hero(clicked.get())    # display the default hero type description.

        btn = Button(pop1, text="Start Game", command = lambda: [get_player_entered_name(), self.send_to_controller(controller)])
        # bind multiple command in one click
        btn.place(relx=0.75,rely=0.9)

    def load_existing_game_window(self, controller):
        view = LoadView()
        view.setup(controller, self.root)

    def welcome_window(self, controller):

        canvas = self.welcome_screen_canvas

        new_game_btn = Button(canvas, text="New Game", command = lambda: self.create_new_game_window(controller))
        load_game_btn = Button(canvas, text="Load Game", command = lambda: self.load_existing_game_window(controller))
        quit_game_btn = Button(canvas, text="Quit Game", command = lambda: self.destruct())

        new_game_btn.place(relx=0.5,rely=0.5, anchor = CENTER)
        load_game_btn.place(relx=0.5, rely=0.6, anchor = CENTER)
        quit_game_btn.place(relx=0.5, rely=0.7, anchor = CENTER)

        global img
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "image assets/welcome_bg.gif")
        img = PhotoImage(file=path)
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.pack()
