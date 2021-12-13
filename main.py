'''
Time used: 26 hours
xingguo
'''

from adventurer import Adventurer
from dungeon import Dungeon
from dungeon_builder import DungeonBuilder
from health_potion import HealthPotion
from vision_potion import VisionPotion
from map import Map
from potion import Potion
from potion_factory import PotionFactory

class Main:
    '''
    main method that contains the main logic for the game
    '''
    def __init__(self):
        pass

    def game_flow(self):
        welcome_page = """
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

Your goal: 
     1⃣ collect all the four pillars of OOP, 
     2⃣ get to the exit safely. 
 
Items randomly placed in each room:
     1⃣ Healing potion(random heal amount),
     2⃣ Vision potion(reveal adjacent room), 
     3⃣ Pit(random damage to adventurer), 
     4⃣ OOP pillars("A","P","I","E").
     
Good luck!!! 
                """
        print(welcome_page)
        bool_flag = True
        while bool_flag:  # menu loop
            help_or_continue = input(
                                     "\'H\' : for all commands of the game\n"
                                     "\'C\' : for continue \nPlease enter your choice: "
                                    )
            if help_or_continue.lower() == 'h':
                self.print_complete_menu()
                break
            elif help_or_continue.lower() == 'c':
                break
            else:
                print("Invalid input, choose again.\n")
                continue  # invalid input

        # obtain name and difficulty level from player
        adventurer_name = input("Now please enter a name for your adventurer: ")
        desired_difficulty = input("Now please enter a difficulty level(easy/medium/hard/inhumane): ").lower()

        print("\nYour adventurer "+adventurer_name+" is ready. Good luck!")

        # Creates a Dungeon Object with desired difficulty
        db = DungeonBuilder(desired_difficulty)
        dungeon = db.build_dungeon(desired_difficulty)

        # Creates an Adventurer Object
        adventurer = Adventurer(adventurer_name, desired_difficulty)
        # print("Adventurer status listed below: \n" + f"{adventurer}")

        # why we need to create the map here?
        map_one = Map(dungeon.total_rows, dungeon.total_columns)
        map_one.set_visited_room(dungeon.entrance[0], dungeon.entrance[1])

        print("Entrance room displayed below: ")
        print(f"{dungeon.get_room(dungeon.entrance)}") # print current room

        # print("Map to show visited room: ")
        # print(dungeon.get_visible_dungeon_string(map_one.visited_array())) # map to print visited room

        # print("Whole dungeon displayed below: ")
        # print(dungeon.get_visible_dungeon_string()) # print whole dungeon, debugging purpose now

        while True:  # another while game loop
            # print(f"{dungeon.get_room(dungeon.adventurer_loc)}")
            # print(f"{dungeon.adventurer_loc}")
            # print(f"{dungeon.exit}")

            # if 1. alive 2. get the 4 pillars  3.arrived at the exit
            if adventurer.is_alive() and \
                    adventurer.has_all_pillars() and \
                    dungeon.adventurer_loc == dungeon.exit:
                print("Congrats! you win the game!")
                break
            elif not adventurer.is_alive():
                print("Your adventurer is dead, better luck next time!")
                break
            else:
                move_or_command = input("Please input your move or command: ")
                if move_or_command.lower() == "p":
                    health_potion_created = PotionFactory.create_potion("health")
                    adventurer.use_health_potion()
                    heal_num = health_potion_created.heal_amount
                    adventurer.heal_adventurer(heal_num)
                elif move_or_command.lower() == "v":
                    pass
                elif move_or_command.lower() == "i":   # i: show adventurer info
                    print("Adventurer status listed below: \n" + f"{adventurer}")
                elif move_or_command.lower() == "m":   # m: show adventurer map
                    print("Currently visited rooms displayed below: ")
                    map_one.set_visited_room(dungeon.adventurer_loc[0], dungeon.adventurer_loc[1])
                    print(dungeon.get_visible_dungeon_string(map_one.visited_array()))
                elif move_or_command.lower() == "w":   # m: show whole dungeon
                    print("Whole dungeon displayed below: ")
                    print(dungeon.get_visible_dungeon_string()) # print whole dungeon, debugging purpose now
                elif move_or_command.lower() == "q":  # quit
                    print("Thanks,Bye!")
                    break
                elif move_or_command.lower() == "north":
                    new_room = dungeon.move_adventurer("north")
                elif move_or_command.lower() == "south":
                    new_room = dungeon.move_adventurer("south")
                elif move_or_command.lower() == "west":
                    new_room = dungeon.move_adventurer("west")
                elif move_or_command.lower() == "east":
                    new_room = dungeon.move_adventurer("east")
                else:
                    print("Invalid input, choose again.")
                    continue

                print("New_room displayed below: \n"+f"{new_room}")

                # print the new room status(H/V/P/M)
                # print(
                #       "New_room health potion #: " + f"{new_room.health_potion}" + "\n" +
                #       "New_room vision potion #: " + f"{new_room.vision_potion}" + "\n" +
                #       "New_room pit damage: " + f"{new_room.pit_damage}" + "\n" +
                #       "New_room contents: " + f"{new_room.contents}" + "\n"
                #     )

                if new_room.health_potion:
                    print(adventurer.name+" found " + f"{new_room.health_potion}" + " health potion!")
                if new_room.vision_potion:
                    print(adventurer.name+" found " + f"{new_room.vision_potion}" + " vision potion!")
                if new_room.contents:
                    if new_room.contents == "A":
                        print(adventurer.name+" found pillar of Abstraction!")
                    elif new_room.contents == "P":
                        print(adventurer.name+" found pillar of Polymorphism!")
                    elif new_room.contents == "I":
                        print(adventurer.name+" found pillar of Inheritance!")
                    elif new_room.contents == "E":
                        print(adventurer.name+" found pillar of Encapsulation!")
                adventurer.add_potions(dungeon.collect_potions())
                pillar_str = dungeon.collect_pillars()
                if pillar_str:
                    adventurer.add_pillar(pillar_str)
                if new_room.pit_damage > 0:
                    adventurer.damage_adventurer(new_room.pit_damage)

                # report the most current status to the player, eg: print(f"{adventurer}")
                # print adventurer status
                # print("Adventurer status listed below: \n" + f"{adventurer}")



    def print_complete_menu(self):
        print(
              "\nMovement commands: \n"
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


