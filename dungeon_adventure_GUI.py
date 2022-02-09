from tkinter import *
from tkinter import filedialog

class dungeon_adventure_GUI:

    def __init__(self):
        self.root = Tk()  # create the root window
        self.welcome_screen_frame = Frame(self.root)  # create a frame within that root window
        self.welcome_screen_canvas = Canvas(self.welcome_screen_frame, width=800, height=600, bg="black") # canvas within that frame

        self.welcome_window()
        self.welcome_screen_frame.pack()
        self.root.mainloop()

    def create_new_game_window(self):
        # checkout this site https://www.youtube.com/watch?v=tpwu5Zb64lQ
        global pop  # to make it accessiable to other functions, otherwise tkinter won't work in our way
        pop = Toplevel(self.root)
        pop.title("New Game")
        pop.geometry("600x300")
        btn2 = Button(pop, text="Confirm New Game").place(relx=0.75,rely=0.9)


    def load_existing_game_window(self):
        global pop  # to make it accessiable to other functions, otherwise tkinter won't work in our way
        pop = Toplevel(self.root)
        pop.title("Load Game")
        pop.geometry("600x300")
        btn3 = Button(pop, text="Load Gxisting Game").place(relx=0.75, rely=0.9)

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


