'''
Time used: 24 hours
xingguo
'''

from adventurer import Adventurer
from map import Map
from dungeon import Dungeon
from dungeon_builder import DungeonBuilder

class Main:
    '''
    main method that contains the main logic for the game
    '''
    def __init__(self):
        pass

    def game_flow(self):
        print("\nWelcome! \nGame logo or rules prints here \n")
        bool_flag = True
        while bool_flag:  # menu loop
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

        # obtain name and difficulty level from player
        adventurer_name = input("Now please enter a name for your adventurer: ")
        desired_difficulty = input("Now please enter a difficulty level(easy/medium/hard/inhumane): ")
        print("\nFollowing is your game, good luck!\n")

        # Creates a Dungeon Object with desired difficulty
        db = DungeonBuilder(desired_difficulty)
        dungeon = db.build_dungeon(desired_difficulty)

        # Creates an Adventurer Object
        adventurer = Adventurer(adventurer_name, desired_difficulty)
        print("Adventurer status listed below: \n" + f"{adventurer}")

        # why we need to create the map here?
        map_one = Map(dungeon.total_rows, dungeon.total_columns)
        map_one.set_visited_room(dungeon.entrance[0], dungeon.entrance[1])

        print("Entrance room displayed below: ")
        print(f"{dungeon.get_room(dungeon.entrance)}") # print current room

        print("Map to show visited room: ")
        print(dungeon.get_visible_dungeon_string(map_one.visited_array())) # map to print visited room

        print("Whole dungeon displayed below: ")
        print(dungeon.get_visible_dungeon_string()) # print whole dungeon, debugging purpose now

        while True:  # another while game loop
            # if 1. alive 2. get the 4 pillars  3.arrived at the exit
            print(f"{dungeon.get_room(dungeon.adventurer_loc)}")
            print(f"{dungeon.adventurer_loc}")
            print(f"{dungeon.exit}")

            if adventurer.is_alive() and \
                    adventurer.has_all_pillars() and \
                    dungeon.adventurer_loc == dungeon.exit:
                print("Congrats! you win the game!")
                break
            elif not adventurer.is_alive():
                print("Your adventurer is dead, better luck next time!")
                break
            else:
                move = input("Please input your move: ")
                new_room = dungeon.move_adventurer(move)
                print("New room: \n"+f"{new_room}")

                # print the new room status(H/V/P/M)
                print(
                      "new_room health potion #: " + f"{new_room.health_potion}" + "\n" +
                      "new_room vision potion #: " + f"{new_room.vision_potion}" + "\n" +
                      "new_room pit damage: " + f"{new_room.pit_damage}" + "\n" +
                      "new_room contents are: " + f"{new_room.contents}" + "\n"
                    )

                adventurer.add_potions(dungeon.collect_potions())
                pillar_str = dungeon.collect_pillars()
                if pillar_str:
                    adventurer.add_pillar(pillar_str)
                if new_room.pit_damage > 0:
                    adventurer.damage_adventurer(new_room.pit_damage)
                # report the most current status to the player, eg: print(f"{adventurer}")
                # print adventurer status
                print("Adventurer status listed below: \n" + f"{adventurer}")
    ####################################################################################################
                print("Print all the visited rooms: ")
                map_one.set_visited_room(dungeon.adventurer_loc[0], dungeon.adventurer_loc[1])

                print(dungeon.get_visible_dungeon_string(map_one.visited_array()))
                print("Debugging purpose, whole dungeon displayed below: ")
                print(dungeon.get_visible_dungeon_string()) # print whole dungeon, debugging purpose now
    ####################################################################################################

    def print_complete_menu(self):
        print("\nComplete commands of the game: \n"
              "Movement commands: \n"
              "\tnorth: move up\n"
              "\tsouth: move down\n"
              "\twest: move left\n"
              "\teast: move right\n"
              "Status commands: \n"
              "\ti: show adventurer info\n"
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