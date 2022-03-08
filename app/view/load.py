import tkinter as tk
import dungeon_adventure_GUI as da_gui

def load_existing_game_window(self):
    global pop2
    pop2 = Toplevel(self.root)
    pop2.geometry("750x450")
    pop2.resizable(width=False, height=False)
    pop2.title("Load Game")

    btn3 = Button(pop2, text="Confirm Load", command=pop2.destroy)
    btn3.place(relx=0.75, rely=0.9)