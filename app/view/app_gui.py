from tkinter import Tk, Canvas, Frame, Button, Menu, simpledialog, ttk
from tkinter import ttk

class App_GUI:
    def __init__(self, root):
        root.title("Dungeon Adventure - The Spoony Bard Returns")
        self.basic_menu_bar()
        base_frame = ttk.Frame(root)

    def start(self):
        pass
    
    def basic_frame(self):
        pass

    def basic_menu_bar(self):
        menubar = Menu()

        addmenu = Menu(menubar, tearoff=0)
        addmenu.add_command(label="Circle")
        addmenu.add_command(label="Rectangle")
        addmenu.add_command(label="Square")
        addmenu.add_command(label="Triangle")
        menubar.add_cascade(label="Add", menu=addmenu)

        removemenu = Menu(menubar, tearoff=0)
        removemenu.add_command(label="Circle")
        removemenu.add_command(label="Rectangle")
        removemenu.add_command(label="Square")
        removemenu.add_command(label="Triangle",)
        menubar.add_cascade(label="Remove", menu=removemenu)

        # self.drawer._root.config(menu=menubar)
        # self.drawer.root.config(menu=menubar)
        self.root.config(menu=menubar)

root = Tk()
App_GUI(root)
root.mainloop()