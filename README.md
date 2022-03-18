# Dungeon Adventure 2.0: The Spoony Bard Returns

### Project Synopsis
Dungeon Adventure 2.0: The Spoony Bard Returns (bards not yet included) is an expansion of the original Dungeon Adventure game from the previous class.  Most aspects of the game were designed per the specs provided by Tom, as well as some minor modifications with the hopes and dreams of extra credit.  It is a pure python game dependent on TKinter.

#### Responsibilities:
# TODO Please check this to see if I missed any of your contributions!
Kevin Chung
Hours clocked: ~70 hours
1) game_controller.py code
2) BaseFrame
3) DungeonCrawler(Dungeon traversal, inventory management, and item usage)
4) DungeonBrawler(Combat completed in turns, combat history log, and potion usage)
5) Turning in weekly deliverables
6) SRS
7) UML

Xingguo Huang
Hours clocked: ~72 hours
1) DungeonAdventureGUI(adventurer information from user)
2) Map display(3x3 grid) and map display(whole dungeon) for debugging
3) Colors adjustment on DungeonCrawler dungeon display to make the game more user-friendly
4) Win/lose window set up and game summary display 

Stephanie Liu
Hours clocked: ~60 hours
1) Model & DB code (including refactoring Kevin's adventurer code from last quarter to match the needs of this quarter)
2) app\view\load_view.py in all its ugly glory, and refactoring of views to call supers to allow load_view to be opened from relevant views.
3) Save and Load methods in controller/game_controller.py
4) Debugging of view / controller / model integration prior to project demo
5) This document!
6) UML
7) SRS

#### Extra Credit Hopefuls:
1) Classes stored in database.
2) Dungeon difficulty stored in database.
3) Pillar unique powers included in game (double health potion collection, double vision potion collection, reduced damage, improved potion potency that allows increasing maximum health).
4) Health potions usable in combat.
5) Really well documented, human-readable code.
6) Great test coverage and OOP implentation with mocks for abstract classes (app\unit_tests\character_tests\abstract_classes\tests)
7) Fleeing implemented in demo version!
8) Packages to assist with easy module import and not a giant file with all our game's files.
9) Turn order for each round completed in a single attack action in DungeonBrawler

### To run project:
0) Verify Python 3.something is installed:
   1) https://www.python.org/downloads/
1) Verify PIP is installed:
   1) https://pip.pypa.io/en/stable/installation/
2) In terminal in main directory (same as where setup.py is located), run following command:
   1) pip install -e .  
3) Verify TKinter installed:
   1) https://www.tutorialspoint.com/how-to-install-tkinter-in-python
4) Run main.py in app\main.py

### Dependencies:
1) Python 3.something
2) PIP
3) TKinter
4) SQLite

### Project design docs:
assignment_documents\the_spoony_bard_returns_uml.pdf
assignment_documents\SRS.pdf

### Pivotal Tracker
assignment_documents\pivotal_tracker.pdf

### Shortcomings
UI is manually tested.  Some integration bugs exist.  Room init code has not been fully refracted like most other classes to store all the generation information and logic within the dungeon_builder.

### Problems overcome
- Integration challenges.
- TKinter was not very intuitive and had some unexpected limits and inconsistent documentation.
- Refactoring old code base to allow easier integration with new features, and designing that adjustment to make sense and be modular.

### Git History
# TODO INCLUDE ME TOO