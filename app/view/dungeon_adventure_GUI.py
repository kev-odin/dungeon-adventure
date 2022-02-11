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
        global pop1  # to make it accessiable to other functions, otherwise tkinter won't work in our way
        pop1 = Toplevel(self.root)
        pop1.title("New Game")
        pop1.geometry("600x300")

        difficulty_label= Label(pop1, text="Select your game difficulty level")
        difficulty_label.pack()


        level_options = [
            "Easy",
            "Medium",
            "Hard"
        ]

        level_options_description = {
            "Easy":"This is the easy mode.This is the easy mode.This is the easy mode.This is the easy mode.",
            "Medium":"This is the medium mode.This is the medium mode.This is the medium mode.This is the medium mode.",
            "Hard":"This is the hard mode.This is the hard mode.This is the hard mode.This is the hard mode."
        }

        clicked = StringVar()
        clicked.set(level_options[0]) # set the default greyed out level

        drop_down_difficulty = OptionMenu(pop1, clicked, *level_options) # create a dropdown menu
        drop_down_difficulty.pack()

        difficulty_description = Label(pop1, text="Difficulty level decription:")
        difficulty_description.pack()

        description_frame = LabelFrame(pop1, text=clicked.get())
        description_frame.pack()

        description_details = Message(description_frame, text=level_options_description[clicked.get()],aspect=500)
        description_details.pack()


        btn2 = Button(pop1, text="Confirm",command=pop1.destroy).place(relx=0.75,rely=0.9)
        btn2.pack()


    def load_existing_game_window(self):
        global pop2  # to make it accessiable to other functions, otherwise tkinter won't work in our way
        pop2 = Toplevel(self.root)
        pop2.title("Load Game")
        pop2.geometry("600x300")


        btn3 = Button(pop2, text="Load Gxisting Game", command = pop2.destroy).place(relx=0.75, rely=0.9)

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


