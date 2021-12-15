from adventurer import Adventurer
from dungeon_builder import DungeonBuilder
from map import Map
from potion_factory import PotionFactory


class Main:
    """
    main method that contains the main logic for the game
    when choosing adventurer names:
        "gary" : hidden name for all pillars collected
        "kevin" : hidden name for pre collected health and vision potion
        "tom" : hidden name for unlimited hit points.
    when playing the game:
        "w": hidden option for testing that prints out the entire Dungeon.
    """

    def game_flow(self):
        """
        Introduces the game describing what the game is about and how to play
        Creates a Dungeon Object and a Adventurer Object
•       Obtains the name of the adventurer and difficulty level from the user
        """
        self.print_welcome()  # print the logo and welcome message
        while True:
            help_or_continue = input(
                                     "\'h\' : for all commands of the game\n"
                                     "\'c\' : for continue \n"
                                     "Your choice: "
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
        adventurer_name = input("Choose an adventurer name: ")

        while True:
            desired_difficulty = input("Choose a difficulty level(easy/medium/hard/inhumane): ").lower()
            if desired_difficulty in ("easy", "medium", "hard", "inhumane"):
                break
            else:
                continue

        self.print_narrative()  # print the narrative
        print("\nYour adventurer "+adventurer_name.upper()+" is ready. Good luck!")

        # Creates a Dungeon Object with desired difficulty
        db = DungeonBuilder(desired_difficulty)
        dungeon = db.build_dungeon(desired_difficulty)

        # Creates an Adventurer Object
        adventurer = Adventurer(adventurer_name, desired_difficulty)

        # create the map to store the starting location
        adv_curr_map = Map(dungeon.total_rows, dungeon.total_columns)
        adv_curr_map.set_visited_room(dungeon.entrance[0], dungeon.entrance[1])

        print("Entrance room displayed below: ")
        print(f"{dungeon.get_room(dungeon.entrance)}")  # print current room

        while True:  # another while game loop
            if adventurer.is_alive() and \
                    adventurer.has_all_pillars() and \
                    dungeon.adventurer_loc == dungeon.exit:
                print("\n:) Woo-hoo! you win the game!")
                print("\nWhole dungeon displayed below: ")
                print(dungeon.get_visible_dungeon_string())  # print whole dungeon
                break
            elif not adventurer.is_alive():
                print("\n:( Uh-oh, better luck next time!")
                break
            else:
                move_or_command = (input("Your move or command: ")).lower()
                if move_or_command == "p":  # if player choose to use health potion
                    if adventurer.has_health_potion():
                        health_potion_created = PotionFactory.create_potion("health")
                        adventurer.heal_adventurer(health_potion_created)
                    else:
                        continue
                elif move_or_command == "v":  # if player choose to use vision potion
                    if adventurer.vision_pots > 0:
                        for i in range(dungeon.adventurer_loc[0]-1, dungeon.adventurer_loc[0]+2):
                            for j in range(dungeon.adventurer_loc[1]-1, dungeon.adventurer_loc[1]+2):
                                if self.room_in_bound(i, j, dungeon):
                                    adv_curr_map.set_visited_room(i, j)  # we set the adjacent room's visibility as True
                        adventurer.vision_pots -= 1  # decrease the vision potion every time player used one
                        print(adventurer.name+" used a vision potion, which revealed all valid adjacent rooms.")
                        print(dungeon.get_visible_dungeon_string(adv_curr_map.visited_array()))
                    else:
                        print("No vision potion in " + adventurer.name + "'s inventory yet.")
                        continue
                elif move_or_command == "i":   # i: show adventurer info
                    print(adventurer.name+"'s status listed below: \n" + f"{adventurer}")
                elif move_or_command == "m":   # m: show adventurer map
                    print("Currently visited rooms displayed below: ")
                    adv_curr_map.set_visited_room(dungeon.adventurer_loc[0], dungeon.adventurer_loc[1])
                    print(dungeon.get_visible_dungeon_string(adv_curr_map.visited_array()))
                elif move_or_command == "w":   # m: show whole dungeon
                    print("Whole dungeon displayed below: ")
                    print(dungeon.get_visible_dungeon_string())  # print whole dungeon
                elif move_or_command == "q":  # quit
                    print("Thanks,Bye!")
                    break
                elif move_or_command in ("north", "south", "west", "east"):
                    # check if there is a door in the desired moving direction
                    if dungeon.get_room(dungeon.adventurer_loc).get_door(move_or_command):
                        new_room = dungeon.move_adventurer(move_or_command)
                        adv_curr_map.set_visited_room(dungeon.adventurer_loc[0], dungeon.adventurer_loc[1])  # update the visited rooms
                        print("New_room displayed below: \n" + f"{new_room}")
                    else:
                        print("No doors in that direction, choose again")
                        continue
                    # check the contents in the room, automatically pick the item if any
                    if new_room.contents == " ":
                        print("Nothing found in this room.")
                    if new_room.contents in ("A", "P", "I", "E"):
                        print("Pillar \"" + f"{new_room.contents}" + "\" is found!!")
                    adventurer.add_potions(dungeon.collect_potions())
                    pillar_str = dungeon.collect_pillars()
                    if pillar_str:
                        adventurer.add_pillar(pillar_str)
                    # automatically take damage if there is a pit
                    if new_room.pit_damage > 0:
                        adventurer.damage_adventurer(new_room.pit_damage)
                else:
                    self.print_in_game_commands_list()
                    continue

    def room_in_bound(self, row, col, dungeon):
        if row < 0 or row > dungeon.total_rows:
            return False
        elif col < 0 or col > dungeon.total_columns:
            return False
        else:
            return True

    def print_welcome(self):
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
     2⃣ Vision potion(reveal adjacent rooms), 
     3⃣ Pit(random damage to adventurer), 
     4⃣ OOP pillars("A","P","I","E").    
Good luck!!! 
                    """
        print(welcome_page)

    def print_narrative(self):
        print("\n┏━━━━━━━━━━━━━━━━━━━━━━━━༻❁༺━━━━━━━━━━━━━━━━━━━━━━━━┓"
              "\nLong before the birth of the world today, \n"
              "the giant sky was supported by four OOP pillars.\n"
              "Society as a whole was prosperous and mirthful, \n"
              "until one day... The pillars DISAPPEARED!!\n"
              "The sky then started to descend, and continued descending over time...\n"
              "In the midst of all the confusion, our hero emerges:\n"
              "┗━━━━━━━━━━━━━━━━━━━━━━━━༻❁༺━━━━━━━━━━━━━━━━━━━━━━━━┛")

    def print_complete_menu(self):
        print(
              "\nStatus commands: \n"
              "\ti: show adventurer info\n"
              "\tm: show adventurer map\n"
              "Item commands: \n"
              "\tp: use health potion\n"
              "\tv: use vision potion\n"
              "Other commands: \n"
              "\tq: quit the game\n"
              "Movement commands: \n"
              "\tnorth: move up\n"
              "\tsouth: move down\n"
              "\twest: move left\n"
              "\teast: move right\n"
        )

    def print_in_game_commands_list(self):
        print("Invalid input, choose again.\n"
              "\'i\' for adventurer status\n"
              "\'m\' for current traveled room/ map\n"
              "\'w\' for whole dungeon map\n"
              "\'p\' for using health potion\n"
              "\'v\' for using vision potion\n"
              "\'q\' for quit the game\n"
              "or \'north\', \'east\', etc.")


if __name__ == "__main__":
    main = Main()
    main.game_flow()
