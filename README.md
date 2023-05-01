# Dungeon Adventure 2.0: The Spoony Bard Returns

![last-commit](https://img.shields.io/github/last-commit/kev-odin/dungeon-adventure?style=for-the-badge)
![count](https://img.shields.io/github/languages/count/kev-odin/dungeon-adventure?style=for-the-badge)
![language](https://img.shields.io/github/languages/top/kev-odin/dungeon-adventure?style=for-the-badge)
![project-size](https://img.shields.io/github/repo-size/kev-odin/dungeon-adventure?style=for-the-badge)
![love](https://img.shields.io/badge/made%20with-%E2%9D%A4%EF%B8%8F-grey?style=for-the-badge)

## Table of Contents

- Click on the hamburger menu in the top left corner of the README.md cell.

## Project Synopsis

Dungeon Adventure 2.0: The Spoony Bard Returns (bards not yet included) is an expansion of our original Dungeon Adventure game.

A pure python game dependent on TKinter.

      In this game, you play as a novice programmer who finds themselves trapped in a mysterious
      dungeon. Your task is to escape the dungeon by collecting the 4 pillars of object oriented
      programming: abstraction, encapsulation, inheritance, and polymorphism.The dungeon is filled with
      hidden dangers at every turn. Deadly traps and ferocious monsters lurk in the shadows, waiting for
      their next victim. You must use your programming skills to navigate the treacherous terrain and
      avoid these dangers.

      But beware - the dungeon is full of traps and enemies that will test your skills to the limit.
      You'll need to use all your wits and cunning to survive and make it to the end of the dungeon.

      Can you collect all four pillars of object oriented programming and escape the dungeon alive? Only
      time will tell. Good luck, adventurer!

## Features

### Game Start

![Start](/assets/dungeon_splash.png)

### Creating a new game, select one of three adventurers

![Create](/assets/dungeon_create.gif)

### Moving around the dungeon by using the navigation buttons

![Nav](/assets/dungeon_navigation.gif)

### Fight monsters throughout the harrowing adventure

![Combat](/assets/dungeon_combat.gif)

### Use the in-game map to determine the location of the exit

![Map](/assets/dungeon_map.gif)

### Collect all the pillars to unlock hidden powers

![Powers](/assets/dungeon_powers.gif)

### Save your progress and pick up where you left off

![Load](/assets/dungeon_load.gif)

### Escape the dungeon alive with all 4 pillars to win

![Win](/assets/dungeon_win.gif)

## Functional Requirements

1. Classes stored in database.
2. Dungeon difficulty stored in database.
3. Pillar unique powers included in game (double health potion collection, double vision potion collection, reduced damage, improved potion potency that allows increasing maximum health).
4. Health potions usable in combat.
5. Really well documented, human-readable code.
6. Great test coverage and OOP implentation with mocks for abstract classes (app/unit_tests/character_tests/abstract_classes/tests)
7. Fleeing implemented in demo version!
8. Packages to assist with easy module import and not a giant file with all our game's files.
9. Turn order for each round completed in a single attack action in DungeonBrawler

## Contributors:

**Kevin Chung**

- Hours clocked: ~70 hours
- Git history entries: 74

1. game_controller.py code
2. BaseFrame
3. DungeonCrawler(Dungeon traversal, inventory management, and item usage)
4. DungeonBrawler(Combat completed in turns, combat history log, and potion usage)
5. Turning in weekly deliverables
6. Software Requirements Sheet (SRS)
7. Unified Modeling Language (UML)

**Xingguo Huang**

- Hours clocked: ~72 hours
- Git history entries: 66

1. DungeonAdventureGUI(adventurer information from user)
2. Map display(3x3 grid) and map display(whole dungeon) for debugging
3. Colors adjustment on DungeonCrawler dungeon display to make the game more user-friendly
4. Win/lose window set up and game summary display

**Stephanie Liu**

- Hours clocked: ~60 hours
- Git history entries: 66

1. Model & DB code (including refactoring Kevin's adventurer code from last quarter to match the needs of this quarter)
2. app\view\load_view.py in all its ugly glory, and refactoring of views to call supers to allow load_view to be opened from relevant views.
3. Save and Load methods in controller/game_controller.py
4. Debugging of view / controller / model integration prior to project demo
5. README.md
6. UML
7. SRS

## Dependencies:

- Python 3.9+
- PIP
- TKinter
- SQLite

## How to play and run the project:

0. Verify [Python 3.9+][py3] is installed:

1. Verify [PIP][pip] is installed:

2. Open a terminal in project root directory, run following commands:

- `python3 -m venv venv`
- `source/bin/activate`
- `pip install -e .`

3. Verify [TKinter][tkinter] installed:

4. Start the game with this command

- `python3 app/main.py`

[py3]: https://www.python.org/downloads/
[pip]: https://pip.pypa.io/en/stable/installation/
[tkinter]: https://www.tutorialspoint.com/how-to-install-tkinter-in-python

## Project design docs and completed user stories

- assignment_documents/the_spoony_bard_returns_uml.pdf
- assignment_documents/SRS.pdf
- assignment_documents/pivotal_tracker.pdf

## Challenges

- The project has some integration bugs that need to be addressed.
- There have been challenges with tKinter to make it behave properly for gameplay, which requires further investigation.
- The use of TKinter was not very intuitive and the documentation was inconsistent, leading to some unexpected limitations and challenges.

## Lessons Learned

- UI testing is done manually, which may result in missed issues or errors.
- The room initialization code needs to be fully refactored to store all the generation information and logic within the dungeon_builder class, like other classes in the project.
- The game could benefit from more descriptive information when entering rooms to improve the player experience.
- In some instances throughout the project code, the view and controller components felt coupled together, which could be refactored to improve the overall design and architecture.
- Refactoring the old code base to allow for easier integration with new features is needed. This requires a thoughtful design approach to ensure that the adjustment is modular and makes sense for the project's architecture.
