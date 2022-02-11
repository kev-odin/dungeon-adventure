# checkout Kevin shared site https://www.pythontutorial.net/tkinter/
# checkout this site https://www.youtube.com/watch?v=tpwu5Zb64lQ
from tkinter import *

class dungeon_adventure_GUI:

    def __init__(self):
        self.root = Tk()  # create the root window
        self.welcome_screen_frame = Frame(self.root)  # create a frame within that root window
        self.welcome_screen_canvas = Canvas(self.welcome_screen_frame,width=800, height=600, bg="black") # canvas within that frame

        self.welcome_window()
        self.welcome_screen_frame.pack()
        # self.welcome_screen_frame.forget
        self.root.mainloop()

    def create_new_game_window(self):
        global pop  # to make it accessiable to other functions, otherwise tkinter won't work in our way
        pop = Toplevel(self.root)
        pop.title("New Game")
        pop.geometry("600x300")

        difficulty_label= Label(pop, text="Select your game difficulty level")
        difficulty_label.pack()


        level_options = [
            "Easy",
            "Medium",
            "Hard"
        ]

        clicked = StringVar()
        clicked.set(level_options[0]) # set the default greyed out level

        drop_down_difficulty = OptionMenu(pop, clicked, *level_options) # create a dropdown menu
        drop_down_difficulty.pack()

        difficulty_description = Label(pop, text="Difficulty level decription:")
        difficulty_description.pack()

        difficulty_description_details = Label(pop, text="box shape here...and the details in it")
        difficulty_description_details.pack()


        # name_label = Label(pop, text="Enter your hero's name:")
        # name_label.pack()
        # e = Entry(pop)
        # e.pack()




        btn2 = Button(pop, text="Confirm",command=pop.destroy).place(relx=0.75,rely=0.9)
        btn2.pack()


    def load_existing_game_window(self):
        global pop  # to make it accessiable to other functions, otherwise tkinter won't work in our way
        pop = Toplevel(self.root)
        pop.title("Load Game")
        pop.geometry("600x300")


        btn3 = Button(pop, text="Load Gxisting Game", command = pop.destroy).place(relx=0.75, rely=0.9)

    def welcome_window(self):

        canvas = self.welcome_screen_canvas

        new_game_btn = Button(canvas, text="New Game", command=self.create_new_game_window).place(relx=0.5,rely=0.5)
        load_game_btn = Button(canvas, text="Load Game", command=self.load_existing_game_window).place(relx=0.5, rely=0.6)
        quit_game_btn = Button(canvas, text="Quit Game", command=self.root.destroy).place(relx=0.5, rely=0.7)

        global img # to make it accessiable to other functions, otherwise tkinter won't work in our way
        img = PhotoImage(file="welcome_bg.gif")
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.pack()


if __name__ == "__main__":
    game = dungeon_adventure_GUI()


