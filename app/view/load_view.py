import tkinter as tk
from tkinter import *

class LoadView:
    def setup(self, controller, parent):
        games = controller.get_saved_games()
        pop2 = Toplevel(parent)
        pop2.geometry("750x450")
        pop2.resizable(width=False, height=False)
        pop2.title("Select a Game to Load")
        button_text, button_dict = {}, {}
        curr_x, curr_y = 0.01, 0.02
        for game in games:
            game_string = f'Timestamp: {game["timestamp"]}, Name: {game["hero_name"]}, Class: {game["class"]}, ' \
                          f'"Difficulty: {game["difficulty"]}, HP: {game["current_hp"]} / {game["max_hp"]}'
            button_text[game["timestamp"]] = game_string
        # In order to get buttons with variable function calls, need to develop using this method.
        for timestamp in button_text:
            def func(x=timestamp):
                return controller.load_game_to_model(x)
            button_dict[timestamp] = Button(pop2, text=button_text[timestamp], command=func)
            button_dict[timestamp].place(relx=curr_x, rely=curr_y)
            curr_y += 0.05
        btn3 = Button(pop2, text="Cancel", command=lambda: pop2.destroy())
        btn3.place(relx=0.75, rely=0.9)
