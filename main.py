'''
Time used: 18 hours
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
    def __init__(self):
        self.visited_array = []
        self.create_visited_room_array()

    def game_flow(self):
        print("\nWelcome! \nprint game logo/rules/info here \n")  # read a text file to display the game logo
        while True:
            help_or_continue = input("Please enter:\n \'h\' : for all commands of the game\n \'c\' : for continue \n \'q\' : for quit the game: ")
            if help_or_continue == 'h':
                print("\nComplete commands of the game: \n"
                      "Movement commands: \n"
                      "\tw: move up\n"
                      "\ts: move down\n"
                      "\ta: move left\n"
                      "\td: move right\n"
                      "Status commands: \n"
                      "\ti: show adventurer info\n"
                      "\tr: show current room\n"
                      "\tm: show adventurer map\n"
                      "Item commands: \n"
                      "\tp: use health potion\n"
                      "\tv: use vision potion\n"
                      "Other commands: \n"
                      "\tq: quit the game\n"
                      "----to be continue----\n")
                break
            elif help_or_continue == 'q':
                print("\tThanks,Bye!")
                break
            elif help_or_continue == 'c':
                print("TODO It should continue to the game!")
            else:
                continue
        adventurer_name = input("Now please enter a name for your adventurer: ")
        desired_difficulty = input("Now please enter a difficulty level(easy/medium/hard/inhumane): ")
        print("Following is your game, good luck!")
        # Creates a Dungeon Object and
        db = DungeonBuilder(desired_difficulty)
        built = db.build_dungeon()

        # Creates a Adventurer Object
        adventurer = Adventurer(adventurer_name, desired_difficulty)
        self.set_visited_room(built.entrance[0],built.entrance[1])
        print(built.get_visible_dungeon_string(self.visited_array)) # print visited room
        print(built.get_visible_dungeon_string()) # print whole dungeon
        while True:
            move = input("Please input your move: ")
            new_room = built.move_adventurer(move)
            print(
                  "new_room health potion: " + str(new_room.health_potion) + "\n" +
                  "new_room vision potion: " + str(new_room.vision_potion) + "\n" +
                  "new_room pit damage: " + str(new_room.pit_damage) + "\n" +
                  "new_room contents in general: " + str(new_room.contents)+ "\n" +
                  adventurer.name + "'s status right now is: " + str(adventurer.health_pots) # can't grab the health reading
                                                                                            # can i use the __str__(self) of adventurer?
                )

            # here we could do some modifications or math deductions of the items. eg potions found, used, health pot changed etc.
            # report the most current status to the player

            self.set_visited_room(built.adventurer_loc[0], built.adventurer_loc[1])
            print(built.get_visible_dungeon_string(self.visited_array))

        adv = Adventurer(adventurer_name, desired_difficulty)  # repeat creating the adventurer
        while True:
            if adv.is_alive() and adv.has_all_pillars() and built.adventurer_loc() == built.exit(): # if 1. alive 2. get the 4 pillars  3.arrived at the exit
                print("Congrats! you escaped the dungeon successfully")
                break
            elif adv.is_alive() and not adv.has_all_pillars() and built.adventurer_loc() != built.exit(): # if 1. alive 2. ! get the 4 pillars  3. ! arrived at the exit
                # keep on doing the main logic
                pass
                dir = input("Please input your commands: ")
                coor = Dungeon.move_adventurer(str(dir))
                # curRoom = completeDungeon.get_room(coor)
                if dir == "w":
                    # move north
                    pass
                elif dir == "s":
                    # move south
                    pass
                elif dir == "a":
                    # move west
                    pass
                elif dir == "d":
                    # move east
                    pass


        # Here we should use the completeDungeon as the back layer and print the map

        print("\nHere should print the dungeon with the player at the entrance\n")
        # print the dungeon and the current location /room?
        # show the players the valid options?
        command = input("Please enter command: ")

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

    def create_visited_room_array(self):
        for row in range(0, 5): # how to find out the size,change in the future  5x5;8x8;10x10
            self.visited_array.append([])
            for col in range(0, 5):
                self.visited_array[row].append([])
                self.visited_array[row][col] = False

    def set_visited_room(self, row, col):
        self.visited_array[row][col] = True


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