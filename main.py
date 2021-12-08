'''
Time used: 6 hours
xingguo
'''

from adventurer import Adventurer
from map import Map
from dungeon import Dungeon
from dungeon_builder import DungeonBuilder
"""
Contains the main logic for playing the game
• Introduces the game describing what the game is about and how to play
• Creates a Dungeon Object and a Adventurer Object
• Obtains the name of the adventurer from the user
• Does the following repetitively:
    o Prints the current room (this is based on the Adventurer's current location)
    o Determines the Adventurer's options (Move, Use a Potion)
    o Continues this process until the Adventurer wins or dies
    o NOTE: Include a hidden menu option for testing that prints out the entire Dungeon -- specify what the menu option
        is in your documentation for the DungeonAdventure class
"""


class Main:
    '''
    main method
    '''
    # what to do with the init?
    # if do GUI
    # to create
    def __init__(self):

        pass



    def game_flow(self):
        # 1st menu:
            # show the title info(text), group info, basic instructions(h --help),(e -exit)
        # 2nd menu:
            # wsad-- u d l f
            # i for player current info health, pillar...
            # p for health pots
            # v for vision pots

        print("\nWelcome! \nprint game logo/rules/info here \n")  # read a text file to display the game logo
        # while True:
        #     help_or_continue = input("Please enter \'h\' for all commands of the game, or \'q\' to quit the game: ")
        #     if help_or_continue == 'h':
        #         print("\nComplete commands of the game: \n"
        #               "Movement commands: \n"
        #               "\tw: move up\n"
        #               "\ts: move down\n"
        #               "\ta: move left\n"
        #               "\td: move right\n"
        #               "Status commands: \n"
        #               "\ti: show adventurer info\n"
        #               "\tr: show current room\n"
        #               "\tm: show adventurer map\n"
        #               "Item commands: \n"
        #               "\tp: use health potion\n"
        #               "\tv: use vision potion\n"
        #               "Other commands: \n"
        #               "\tq: quit the game\n"
        #               "----to be continue----\n")
        #         break
        #     elif help_or_continue == 'q':
        #         print("Thanks,Bye!")
        #         break
        #     else:
        #         continue
        # adventurer_name = input("Now please enter a name for your adventurer: ")
        # desired_difficulty = input("Now please enter a difficulty level(easy/medium/hard/inhumane): ")
        print("Following if your game, good luck!")
        # Creates a Dungeon Object and a Adventurer Object
        db = DungeonBuilder("easy")
        built = db.build_dungeon()
        completeDungeon = Dungeon(built)
        # Here we should use the completeDungeon as the back layer and print the map

        print("\nHere should print the dungeon with the player at the entrance\n")
        # print the dungeon and the current location /room?
        # show the players the valid options?
        command = input("Please enter command: ")

        while True:
            # command = input("")
            if command == 'h':
                self.display_basic_commands('h')
                continue
            elif command == 'e':
                break
            else:
                self.startGame()
            # handle exceptions(illegal inputs)
    def show_ingame_menu(self):
        pass

    def start_game(self):
        pass
        # Creates a Dungeon Object and a Adventurer Object
        # get user command

    def move_adventurer(self):
        # adventurer interates with dun
        # if alive let the user to interacte if dead, exit
        # if adv at the exit? if adv has all the pillars?
        # add the traveled room to the list and display to the map
        pass

    def display_basic_commands(self):
        # print out ....   test it works correctly
        print("\nHere we will display all the basic commands\n")


    def display_adventurer_info(self):
        # to call __str__ function of ....?
        pass


if __name__ == "__main__":
    main = Main()
    main.game_flow()







"""
____                                          
|    \  _ _  ___  ___  ___  ___  ___           
|  |  || | ||   || . || -_|| . ||   |          
|____/ |___||_|_||_  ||___||___||_|_|          
                 |___|                         
                                               
 _____    _                 _                  
|  _  | _| | _ _  ___  ___ | |_  _ _  ___  ___ 
|     || . || | || -_||   ||  _|| | ||  _|| -_|
|__|__||___| \_/ |___||_|_||_|  |___||_|  |___|  


Welcome to Dungeon Adventure! 

Your goal is to find all the four pillars of OOP and get to the exit safely. 

Each room of the dungeon will be randomly placed with the following items: 1⃣ Healing potion, 2⃣ Vision potion, 3⃣ Pit, 4⃣ OOP pillars, or nothing

If there are any items listed above 1⃣ -- 4⃣ in the room, you will automatically pick up the item(s) or take the damage.

For the Healing potion and Vision potion, you can choose to use them anytime you want. 

Beware that you have a limited amount of health pot, think before you jump to any room, and use the items wisely.

Good luck!!! 
"""