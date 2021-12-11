'''
Time used: 20 hours
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
    main method that contains the main logic for playing the game
    '''
    def __init__(self):
        self.visited_array = []
        self.create_visited_room_array()

    def game_flow(self):  # menu loop
        print("\nWelcome! \nGame logo or rules prints here \n")  # read a text file to display the game logo
        bool_flag = True
        while bool_flag:
            help_or_continue = input("Please enter:\n "
                                     "\'h\' : for all commands of the game\n "
                                     "\'c\' : for continue \n ")
            if help_or_continue == 'h':
                self.print_complete_menu()
                break
            elif help_or_continue == 'c':
                break
            else:
                continue # invalid input

        # another while game loop
        adventurer_name = input("Now please enter a name for your adventurer: ")
        desired_difficulty = input("Now please enter a difficulty level(easy/medium/hard/inhumane): ")
        print("\nFollowing is your game, good luck!\n")

        # Creates a Dungeon Object with desired difficulty
        db = DungeonBuilder(desired_difficulty)  # question: why all levels are the same size? 5;8;10;20?
        dungeon = db.build_dungeon(desired_difficulty)
        # dungeon =  db.build_dungeon(desired_difficulty) # question:

        # Creates a Adventurer Object
        adventurer = Adventurer(adventurer_name, desired_difficulty)
        self.set_visited_room(dungeon.entrance[0], dungeon.entrance[1])

        print("Entrance room displayed below: ") # we only want to print the current room
        # print(dungeon.get_visible_dungeon_string(self.visited_array)) # print visited room
        print(f"{dungeon.get_room(dungeon.entrance)}")

        # print("Debugging purpose, whole dungeon displayed below: ")
        # print(dungeon.get_visible_dungeon_string()) # print whole dungeon, debugging purpose now

        print("Adventurer status right now:")
        print(adventurer)

        while True:
            move = input("Based on your current room, please input your move: ")
            new_room = dungeon.move_adventurer(move)
            print("Current room: \n"+f"{new_room}")
            # adv_location = dungeon.adventurer_loc()
            # print("I want to print out the current room!")
            # print(dungeon.get_room(adv_location[0], adv_location[1]))

            print(
                  "new_room health potion #: " + f"{new_room.health_potion}" + "\n" +
                  "new_room vision potion #: " + f"{new_room.vision_potion}" + "\n" +
                  "new_room pit damage: " + f"{new_room.pit_damage}" + "\n" +
                  "new_room contents are: " + f"{new_room.contents}" + "\n" +
                  "Adventurer status right now:" + f"{adventurer}"
                )

            # here we could do some modifications or math deductions of the items. eg potions found, used, health pot changed etc.
            # report the most current status to the player, eg: print(f"{adventurer}")

            print("Print all the visited rooms: ")
            self.set_visited_room(dungeon.adventurer_loc[0], dungeon.adventurer_loc[1])
            print(dungeon.get_visible_dungeon_string(self.visited_array))

        adv = Adventurer(adventurer_name, desired_difficulty)  # repeat creating the adventurer
        bool_flag2 = True
        while bool_flag2:
            if adv.is_alive() and adv.has_all_pillars() and dungeon.adventurer_loc() == dungeon.exit(): # if 1. alive 2. get the 4 pillars  3.arrived at the exit
                print("Congrats! you escaped the dungeon successfully")
                break
            elif adv.is_alive() and not adv.has_all_pillars() and dungeon.adventurer_loc() != dungeon.exit(): # if 1. alive 2. ! get the 4 pillars  3. ! arrived at the exit
                pass
            else:
                pass


        # Here we should use the completeDungeon as the back layer and print the map

        print("\nHere should print the dungeon with the player at the entrance\n")
        # print the dungeon and the current location /room?
        # show the players the valid options?
        command = input("Please enter command: ")

    def create_visited_room_array(self):
        for row in range(0, 20): # how to find out the size,change in the future  5x5;8x8;10x10
            self.visited_array.append([])
            for col in range(0, 20):
                self.visited_array[row].append([])
                self.visited_array[row][col] = False

    def set_visited_room(self, row, col):
        self.visited_array[row][col] = True

    def print_complete_menu(self):
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