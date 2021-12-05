'''
Time used: 4 hours
xingguo
'''

# from adventurer import Adventurer
# from map import Map
# from dungeon import Dungeon

# • Contains the main logic for playing the game
#       when run the game, there should be a welcome page show up
#       this is the first receiption desk menu
# • Introduces the game describing what the game is about and how to play
# • Creates a Dungeon Object and a Adventurer Object
# • Obtains the name of the adventurer from the user

class Main:

    # what to do with the init?
    def __init__(self):
        pass


    def show_main_menu(self):
        # 1st menu:
            # show the title info(text), group info, basic instructions(h --help),(e -exit)
        # 2nd menu:
            # wsad-- u d l f
            # i for player current info health, pillar...
            # p for health pots
            # v for vision pots
        print("Instruction") # read a text file to display the game logo
        print("please enter command: ")
        while True:
            command = input("")
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


if __name__ == "__main__": # when this file is run,
    main = Main()
    main.show_main_menu()







"""                                                                                                                   
88888888ba,                                                                                                          
88      `"8b                                                                                                         
88        `8b                                                                                                        
88         88  88       88  8b,dPPYba,    ,adPPYb,d8   ,adPPYba,   ,adPPYba,   8b,dPPYba,                            
88         88  88       88  88P'   `"8a  a8"    `Y88  a8P_____88  a8"     "8a  88P'   `"8a                           
88         8P  88       88  88       88  8b       88  8PP"""""""  8b       d8  88       88                           
88      .a8P   "8a,   ,a88  88       88  "8a,   ,d88  "8b,   ,aa  "8a,   ,a8"  88       88                           
8888888db"'     `"YbbdP'Y88888       88   `"YbbdP"Y8   `"Ybbd8"'   `"YbbdP"'   88       88                           
      d88b                88              aa,    ,88                 ,d                                              
     d8'`8b               88               "Y8bbdP"                  88                                              
    d8'  `8b      ,adPPYb,88  8b       d8   ,adPPYba,  8b,dPPYba,  MM88MMM  88       88  8b,dPPYba,   ,adPPYba,      
   d8YaaaaY8b    a8"    `Y88  `8b     d8'  a8P_____88  88P'   `"8a   88     88       88  88P'   "Y8  a8P_____88      
  d8""""""""8b   8b       88   `8b   d8'   8PP"""""""  88       88   88     88       88  88          8PP"""""""      
 d8'        `8b  "8a,   ,d88    `8b,d8'    "8b,   ,aa  88       88   88,    "8a,   ,a88  88          "8b,   ,aa      
d8'          `8b  `"8bbdP"Y8      "8"       `"Ybbd8"'  88       88   "Y888   `"YbbdP'Y8  88           `"Ybbd8"'                                                                                                                                                                                                                                          
"""