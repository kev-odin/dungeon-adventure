from adventurer import Adventurer
from map import Map
from dungeon import Dungeon


class Main:
    def __init__(self):
        pass
    def startMainMenu(self):
        # show the title info(text), group info, basic instructions(h --help),(e -exit)
        # h--help
        # wsad-- u d l f
        # i for player current info health, pillar...
        # p for health pots
        # v for vision pots
        print("instruction") # read a text file
        print("please enter command")
        while True:
            command = input("")
            if command == 'h':
                self.display_basic_commands('h')
                continue
            elif command == 'e':
                break
            else:
                self.startGame()
            # handle exceptions

    def startGame(self):
        pass
        # create 1, 2, 3
        # get user command

    def move(self):
        # adventurer interates with dun
        # if alive let the user to interacte if dead, exit
        # if adv at the exit? if adv has all the pillars?
        # add the traveled room to the list and display to the map
        pass

    def display_basic_commands(self):
        # print out ....   test it works correctly
        pass
    def display_player_info(self):
        playe_name = input("Welcome to Dnd, Please enter your player's name: ")
        pass
    def move(self):
        pass


if __name__ == "__main__": # when this file is run,
    main = Main()
    main.start()