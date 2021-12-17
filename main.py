from adventurer import Adventurer
from dungeon_builder import DungeonBuilder
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
        Obtains the name of the adventurer and difficulty level from the user
        """
        self.print_welcome()  # print the logo and welcome message
        while True:
            help_or_continue = input(
                                     "\'h\' : for all commands of the game\n"
                                     "\'c\' : for continue\n"
                                     "\nYour choice: "
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
            self.print_difficulty_description()
            desired_difficulty = input("Choose a difficulty level: ").lower()
            if desired_difficulty in ("easy", "medium", "hard", "inhumane"):
                break
            else:
                print(f"{desired_difficulty} is not a valid selection difficulty setting.")

        self.print_narrative()  # print the narrative
        print("\nYour adventurer " + adventurer_name.upper() + " is ready. Good luck!")

        # Creates a Dungeon Object with desired difficulty
        db = DungeonBuilder()
        dungeon = db.build_dungeon(desired_difficulty)
        # Get the map from dungeon builder.
        adv_curr_map = db.map

        # Creates an Adventurer Object
        adventurer = Adventurer(adventurer_name, desired_difficulty)

        print("Entrance room displayed below: ")
        print(f"{dungeon.get_room(dungeon.entrance)}")  # print current room
        print(f"{adventurer}")  # print initial adventurer for player, otherwise will need to use "i"

        player_stats = {
                "used health pots"      : 0,#
                "used vision pots"      : 0,#
                "heroic falls"          : 0,#
                "potential pit damage"  : 0,#
                "moves to exit"         : 0,#
                "map opened"            : 0,#
                "pillars collected"     : 0,#
                "cheat counter"         : 0 #
            }

        while True:  # another while game loop

            if adventurer.is_alive() and \
                    adventurer.has_all_pillars() and \
                    dungeon.adventurer_loc == dungeon.exit:
    
                print("\n:) Woo-hoo! you win the game!")
                print("\nWhole dungeon displayed below: ")
                print(dungeon.get_visible_dungeon_string())  # print whole dungeon

                # if win, ask player if they would like to play again
                play_again = input("Play again? (y/n): ")
                if play_again.lower() == "y":
                    self.game_flow()
                else:
                    print("Thanks, Bye!")
                    exit()

            elif not adventurer.is_alive():
                print("\n:( Uh-oh, better luck next time!")
                break

            else:
                move_or_command = (input("Your move or command: ")).lower()
                if move_or_command == "p":  # if player choose to use health potion
                    if adventurer.has_health_potion():
                        
                        health_potion_created = PotionFactory.create_potion("health")
                        adventurer.heal_adventurer(health_potion_created)
                        player_stats["used health pots"] += 1

                elif move_or_command == "v":  # if player choose to use vision potion
                    if adventurer.has_vision_potion():
                        adv_curr_map.use_vision_potion(row=dungeon.adventurer_loc[0], col=dungeon.adventurer_loc[1])
                        print(dungeon.get_visible_dungeon_string(adv_curr_map.visited_array()))
                        player_stats["used vision pots"] += 1

                elif move_or_command == "h":
                    self.print_complete_menu() # h: show entire command menu

                elif move_or_command == "i":   # i: show adventurer info
                    print(adventurer.name+"'s status listed below: \n" + f"{adventurer}")

                elif move_or_command == "m":   # m: show adventurer map
                    player_stats["map opened"] += 1

                    print("Map Key:\n@ - YOU ARE HERE! :D\n"
                          "A P I E - A pillar!  Collect to unlock powers and win the game!\nX - a pit\n"
                          "H - Health Potion\nV - Vision Potion\nM - Multiple (pit, potions)\ni - Entrance\nO - Exit\n"
                          "|| or - Open doors\n* - Boulders blocking your path.")
                    print("Currently known rooms displayed below: \n")
                    adv_curr_map.set_visited_room(dungeon.adventurer_loc[0], dungeon.adventurer_loc[1])
                    print(dungeon.get_visible_dungeon_string(adv_curr_map.visited_array()))

                elif move_or_command == "wd":   # w: show whole dungeon
                    player_stats["cheat counter"] += 1
                    print("Whole dungeon displayed below: \n")
                    print(dungeon.get_visible_dungeon_string())  # print whole dungeon
                    print(adventurer)
                    print(player_stats)

                elif move_or_command == "q":  # quit
                    print("\nThanks, Bye!")
                    break

                elif move_or_command in ("w", "a", "s", "d"):
                    # check if there is a door in the desired moving direction
                    move = {"w": "north", "a": "west", "s": "south", "d": "east"}
                    try:
                        new_room = dungeon.move_adventurer(move[move_or_command])
                        adv_curr_map.set_visited_room(dungeon.adventurer_loc[0], dungeon.adventurer_loc[1])  # update map
                        player_stats["moves to exit"] += 1
                        print("Current room displayed below: \n" + f"{new_room}")
                    except ValueError:
                        print("No doors in that direction, please choose again.")
                        continue

                    # check the contents in the room, automatically pick the item if any
                    if new_room.contents == " ":
                        print(f"{adventurer.name} discovered nothing in this room.")
                    if new_room.contents == "i":
                        print(f"{adventurer.name} recognized this location as the entrance of the dungeon.")
                    if new_room.contents == "O":
                        print(f"{adventurer.name} recognized this location as the exit of the dungeon.")
                        if adventurer.has_all_pillars():
                            print(f"{adventurer.name} felt the four pillars resonate together dispelling the invisible barrier.")
                        else:
                            print(
                                f"{adventurer.name} tried to push against the exit door. However, an invisible barrier prevented escape.\n"
                                f"A voice whispers in the {adventurer.name}'s ear: 'Collect the pillars, save the world.'\n"
                                )

                    if new_room.contents in ("A", "P", "I", "E"):
                        pillar_dict = {"A": "Abstraction is found!!  It grants double health potion collection.",
                                       "P": "Polymorphism is found!!  It grants double vision potion collection.",
                                       "I": "Inheritance is found!! It slows your fall, reducing pit damage by half.",
                                       "E": "Encapsulation is found!! It increases health potion potency."}
                        print("Pillar of " + f"{pillar_dict[new_room.contents]}")
                        pillar_str = dungeon.collect_pillars()
                        if pillar_str:
                            adventurer.add_pillar(pillar_str)
                            player_stats["pillars collected"] += 1

                        if adventurer.has_all_pillars():
                            print(
                                f"{adventurer.name} has collected all the pillars.  The dungeon is starting to collapse."
                                f"\nFlee to the exit as quickly as possible before it's too late!")
                    
                    adventurer.add_potions(dungeon.collect_potions())

                    # automatically take damage if there is a pit
                    if new_room.pit_damage:
                        recieved_dmg = new_room.pit_damage
                        adventurer.damage_adventurer(recieved_dmg)
                        player_stats["potential pit damage"] += recieved_dmg
                        player_stats["heroic falls"] += 1
                else:
                    print(f"Invalid input. {adventurer.name} is confused. Please choose again.")
                    self.print_complete_menu()
                    continue

        self.print_player_statistics(adventurer_name.upper(), player_stats)

    @staticmethod
    def print_welcome():
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
     1) Collect all the four pillars of OOP, 
     2) Get to the exit safely. 

Items randomly placed in each room:
     1) Healing potion(random heal amount),
     2) Vision potion(reveal adjacent rooms), 
     3) Pit(random damage to adventurer), 
     4) OOP pillars("A","P","I","E").\n    
Good luck!!! 
                    """
        print(welcome_page)

    @staticmethod
    def print_narrative():
        print("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━༻❁༺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
              "\nLong before the birth of the world today, \n"
              "the giant sky was supported by four OOP pillars.\n"
              "Society as a whole was prosperous and mirthful, \n"
              "until one day... The pillars DISAPPEARED!!\n"
              "The sky then started to descend, and continued descending over time...\n"
              "In the midst of all the confusion, our hero emerges:\n"
              "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━༻❁༺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    @staticmethod
    def print_complete_menu():
        print(
              "\nStatus commands: \n"
              "\ti: show adventurer info\n"
              "\tm: show adventurer map\n"
              "Item commands: \n"
              "\tp: use health potion\n"
              "\tv: use vision potion\n"
              "Other commands: \n"
              "\th: help menu\n"
              "\tq: quit the game\n"
              "Movement commands: \n"
              "\tw: move up\n"
              "\ts: move down\n"
              "\ta: move left\n"
              "\td: move right\n"
        )

    @staticmethod
    def print_difficulty_description():
        print(
            f"\nAvailable difficulty settings:\n"
            f"\n\teasy - more than 100 hitpoints, two health and vision potions\n"
            f"\tmedium - more than 95 hitpoints, one health and vision potion\n"
            f"\thard - more than 90 hitpoints, one health and vision potion\n"
            f"\tinhumane - more than 85 hitpoints, ONLY one vision potion\n"
        )
    @staticmethod
    def print_player_statistics(name, stat_dict):
        print(f"\n{name}'s Endgame Summary")

        for key, value in stat_dict.items():
            print(f"{key}: {value}".capitalize())
        print("\n")

if __name__ == "__main__":
    main = Main()
    main.game_flow()
