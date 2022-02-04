from tkinter import *

class dungeon_adventure_GUI:

    def __init__(self):
        self.root = Tk()
        self.welcome_screen_frame = Frame(self.root)
        self.welcome_screen_canvas = Canvas(self.welcome_screen_frame, width=800, height=600, bg="black")
        img = PhotoImage(file="welcome_bg.gif")
        self.welcome_screen_canvas.create_image(0, 0, anchor=NW, image=img)
        self.welcome_screen_canvas.pack()

        self.welcome_window()
        self.welcome_screen_frame.pack()

        self.root.mainloop()

    def create_new_game_window(self):
        top = Toplevel(self.root)
        # top.mainloop()

    def welcome_window(self):

        canvas = self.welcome_screen_canvas
        # new_game_btn = Button(self.root, text="New Game", command=self.create_new_game_window()).place(relx=0.5, rely=0.5)
        # load_game_btn = Button(self.root, text="Load Game", command='Need a command').place(relx=0.5, rely=0.6)
        # quit_game_btn = Button(self.root, text="Quit Game", command=self.root.destroy).place(relx=0.5, rely=0.7)

        new_game_btn = Button(self.welcome_screen_canvas, text="New Game", command=self.create_new_game_window()).place(relx=0.5,rely=0.5)
        load_game_btn = Button(self.welcome_screen_canvas, text="Load Game", command='Need a command').place(relx=0.5, rely=0.6)
        quit_game_btn = Button(self.welcome_screen_canvas, text="Quit Game", command=self.root.destroy).place(relx=0.5, rely=0.7)

        # img = PhotoImage(file="welcome_bg.gif")
        # self.welcome_screen_canvas.create_image(0, 0, anchor=NW, image=img)
        # self.welcome_screen_canvas.pack()


if __name__ == "__main__":
    game = dungeon_adventure_GUI()


