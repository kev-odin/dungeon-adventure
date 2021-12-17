from adventurer import Adventurer
from dungeon_builder import DungeonBuilder
from potion_factory import PotionFactory


class Main:
    """
    main method that contains the main logic for the game
    when choosing adventurer names:
        "gary"  : hidden name for all pillars collected
        "kevin" : hidden name for pre collected health and vision potion
        "tom"   : hidden name for 1000 hit points.
    
    when playing the game:
        "w"     : hidden option for testing that prints out the entire Dungeon.
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

        print("\nEntrance room displayed below: \n")
        print(f"{dungeon.get_room(dungeon.entrance)}")  # print current room
        print(f"{adventurer}")  # print initial adventurer for player, otherwise will need to use "i"

        player_stats = {
                "game difficulty setting"       : desired_difficulty,#
                "health potions collected"      : 0,#
                "health potions used"           : 0,#
                "health recovered"              : 0,#
                "potential health recovered"    : 0,#
                "vision potions collected"      : 0,#
                "vision potions used"           : 0,#
                "heroic falls"                  : 0,#
                "pit damage received"           : 0,#
                "moves to exit"                 : 0,#
                "map opened"                    : 0,#
                "pillars collected"             : 0,#
                "cheat counter"                 : 0 #
            }

        while True:  # another while game loop

            if adventurer.is_alive() and \
                    adventurer.has_all_pillars() and \
                    dungeon.adventurer_loc == dungeon.exit:
    
                print("\n:) Woo-hoo! you win the game!")
                self.print_player_statistics(dungeon, adventurer, player_stats)

                # if win, ask player if they would like to play again
                play_again = input("\nPlay again? (y/n): ")
                if play_again.lower() == "y":
                    self.game_flow()
                elif play_again.lower() == "n":
                    print("Thanks, Bye!")
                    exit()
                else:
                    print(f"{play_again} is an incorrect command. Please select 'y' or 'n'.")

            elif not adventurer.is_alive():
                print("\n:( Uh-oh, better luck next time!")
                self.print_player_statistics(dungeon, adventurer, player_stats)
                break

            else:
                move_or_command = (input("Your move or command: ")).lower()
                if move_or_command == "p":  # if player choose to use health potion
                    if adventurer.has_health_potion():
                        
                        if adventurer.has_all_pillars():
                            print(f"{adventurer.name} used all pillars to increase max hit points.")
                        
                        if adventurer.pillars_collected["E"]:
                            print(f"{adventurer.name} used the powers of Encapsulation to increase health potion potency.")

                        health_potion = PotionFactory.create_potion("health")
                        heal, health_recovered = adventurer.heal_adventurer(health_potion)
                        
                        player_stats["health potions used"] += 1
                        player_stats["potential health recovered"] += heal
                        player_stats["health recovered"] += health_recovered

                        print(f"{adventurer.name} drank a {health_potion.name} and healed {health_recovered} hitpoint{self.pluralize(health_recovered)}.\n")

                    else:
                        print(f"{adventurer.name} does not have a vision potion.")

                elif move_or_command == "v":  # if player choose to use vision potion
                    if adventurer.has_vision_potion():

                        adv_curr_map.use_vision_potion(row=dungeon.adventurer_loc[0], col=dungeon.adventurer_loc[1])
                        player_stats["vision potions used"] += 1

                        print(f"{adventurer.name} drank a vision potion, which revealed adjacent rooms.\n")
                        print(dungeon.get_visible_dungeon_string(adv_curr_map.visited_array()))
                    
                    else:
                        print(f"{adventurer.name} does not have a vision potion.")


                elif move_or_command == "h":
                    self.print_complete_menu() # h: show entire command menu

                elif move_or_command == "i":   # i: show adventurer info
                    print(adventurer.name+"'s status listed below: \n" + f"{adventurer}")

                elif move_or_command == "m":   # m: show adventurer map
                    print("Map Key:\n@ - YOU ARE HERE! :D\n"
                          "A P I E - A pillar!  Collect to unlock powers and win the game!\nX - a pit\n"
                          "H - Health Potion\nV - Vision Potion\nM - Multiple (pit, potions)\ni - Entrance\nO - Exit\n"
                          "|| or - Open doors\n* - Boulders blocking your path.")
                    print("Currently known rooms displayed below: \n")
                    
                    adv_curr_map.set_visited_room(dungeon.adventurer_loc[0], dungeon.adventurer_loc[1])
                    player_stats["map opened"] += 1

                    print(dungeon.get_visible_dungeon_string(adv_curr_map.visited_array()))

                elif move_or_command == "wd":   # w: show whole dungeon
                    player_stats["cheat counter"] += 1
                    print("CHEATER CHEATER CHEATER or Game Dev\n")
                    self.print_player_statistics(dungeon, adventurer, player_stats)

                elif move_or_command == "q":  # quit
                    print("Thanks, Bye!\n")
                    self.print_player_statistics(dungeon, adventurer, player_stats)
                    break

                elif move_or_command in ("w", "a", "s", "d"):
                    # check if there is a door in the desired moving direction
                    move = {"w": "north", "a": "west", "s": "south", "d": "east"}
                    try:
                        new_room = dungeon.move_adventurer(move[move_or_command])
                        adv_curr_map.set_visited_room(dungeon.adventurer_loc[0], dungeon.adventurer_loc[1])  # update map
                        player_stats["moves to exit"] += 1
                        print("\nCurrent room displayed below:\n" + f"\n{new_room}")
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
                    
                    # potion collection
                    if new_room.contents in ("H", "V", "M"):

                        heal_pot, vision_pot = adventurer.add_potions(dungeon.collect_potions())
                        player_stats["health potions collected"] += heal_pot
                        player_stats["vision potions collected"] += vision_pot
                                                
                        if adventurer.pillars_collected["A"] and heal_pot > 0:
                            print(f"{adventurer.name} used the powers of Abstraction to double health potion collection.")
                        
                        if adventurer.pillars_collected["P"] and vision_pot > 0:
                            print(f"{adventurer.name} used the powers of Polymorphism to double vision potion collection.")

                        if heal_pot != 0:
                            print(f"{adventurer.name} found {heal_pot} health potion{self.pluralize(heal_pot)}.")

                        if vision_pot != 0:
                            print(f"{adventurer.name} found {vision_pot} vision potion{self.pluralize(vision_pot)}.")

                    # automatically take damage if there is a pit
                    if new_room.pit_damage:

                        if adventurer.pillars_collected["I"]:
                            print(f"{adventurer.name} used the powers of Inheritance to fall slower reducing pit damage by half.")

                        recieved_damage = new_room.pit_damage
                        real_damage = adventurer.damage_adventurer(recieved_damage)

                        player_stats["heroic falls"] += 1
                        player_stats["pit damage received"] += real_damage

                        print(f"{adventurer.name} fell into a pit and took {real_damage} point{self.pluralize(real_damage)} of damage.")
                else:
                    print(f"Invalid input. {adventurer.name} is confused. Please choose again.")
                    self.print_complete_menu()
                    continue
 
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
    def print_player_statistics(dungeon, adventurer, stat_dict):
        print("Whole dungeon displayed below:\n")
        print(dungeon.get_visible_dungeon_string())
        print(adventurer)
        print(f"{adventurer.name}'s Endgame Summary")
        for key, value in stat_dict.items():
            print(f"{key}: {value}".capitalize())

    @staticmethod
    def pluralize(value):
        """Method to determine if a value would be a plural value.
        :param value: quantity to assess
        :type value: int
        :return: an s or empty character
        :rtype: string
        """
        if isinstance(value, int):
            plural = "s" if value != 1 else ""
            return plural
        else:
            raise TypeError("Incorrect value. Must pass in a integer.")

if __name__ == "__main__":
    main = Main()
    main.game_flow()
