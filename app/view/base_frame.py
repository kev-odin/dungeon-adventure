import tkinter as tk

class BaseFrame(tk.Frame):
    def __init__(self):
        self.root = Tk()
        self.root.resizable(height=False, width=False)
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

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New game", command=lambda: self.controller.start_new())
        filemenu.add_command(label="Save game", command=lambda: self.controller.save_game())
        filemenu.add_command(label="Load game", command=lambda: self.controller.load_game())
        filemenu.add_command(label="Quit game", command=self.root.destroy)

        menubar.add_cascade(label="File", menu=filemenu)

        help = Menu(menubar, tearoff=0)
        help.add_command(label="About Us")
        help.add_command(label="Controls")

        menubar.add_cascade(label="Help", menu=help)

        self.root.config(menu=menubar)

    def load_existing_game_window(self):
        pop = Toplevel(self.root)
        pop.geometry("750x450")
        pop.resizable(width=False, height=False)
        pop.title("Load Game")

        btn3 = Button(pop, text="Confirm Load", command=pop.destroy).place(relx=0.75, rely=0.9)
        btn3.pack(self.root)