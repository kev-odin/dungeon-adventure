from tkinter import *


class LoadView:
    """
    View for loading games from the save db.  Displays each save as a separate button with basic user information.
    """
    @staticmethod
    def setup(controller, parent):
        games = controller.get_saved_games()
        load_screen = Toplevel(parent)
        load_screen.geometry("800x450")
        load_screen.resizable(width=False, height=False)
        load_screen.title("Select a Game to Load")
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
            button_dict[timestamp] = Button(load_screen, text=button_text[timestamp], command=func)
            button_dict[timestamp].place(relx=curr_x, rely=curr_y)
            curr_y += 0.05
        btn3 = Button(load_screen, text="Cancel", command=lambda: load_screen.destroy())
        btn3.place(relx=0.75, rely=0.9)
