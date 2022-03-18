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

Challenges with tKinter to behave properly for gameplay. Could be more descriptive when entering rooms. View and controller components felt coupled together
in some instances throughout the project code. 

### Problems overcome
- Integration challenges.
- TKinter was not very intuitive and had some unexpected limits and inconsistent documentation.
- Refactoring old code base to allow easier integration with new features, and designing that adjustment to make sense and be modular.

### Git History
Xingguo H. (66):
      added the basic welcome window with three empty buttons
      solved the issue that image does not show if not in init. by adding global img
      added the link for the tutorial pf popup
      added button window
      before the pair
      added difficulty level and need improvement for the level description message box
      added message box but need to make it sync with the level
      nothing new
      working changes to the level and description, but still needs to deal with the additional message
      difficulty level varies now. Second pop window still needs to be populated
      get_adventurer_info is basically done, need the next function to transport the data to controller
      add
      moved dungeon adventure GUI to view
      save before merging kevin's branch
      conflict resolved and merged Kevin's week2 iteration to xingguo
      trying to fix the bug that setting dictionary can't update the name
      Entry now can send the name to dictionary
      now the name can be sent to controller
      using pycharm to push
      basic 3x3 grid done!
      added the hero image to the 3 x 3 grid
      added the hero image to the 3 x 3 grid
      after merging with kevin's branch
      resolve merge conflict
      adjust the cell size by devide the row and col numbers
      map grrid done
      updated grid
      door can be displayed in a certain room, still  needs to be implemented for all rooms
      east doors are working fine now. Just needs some simple calculation to get the rest 3 doors
      west doors are working fine now.
      4 doors are working now
      created oval to represent adventurer location
      Create text En/ Ex to represent entrance and exit
      Generated all the symbols using room.content()
      cleaner code to generate symbols on map
      trying to display the untraveled room
      deleted unused image
      changed to font size to fit all the dungeon sizes
      added a reference 'map' in controller code for update_dungeon_display() so that it will be easier to create the view
      commit before merging week4 to xingguo
      fixed the bug for clicking map not showing
      if there is an accessible room, print that room in grey
      set_dungeon_display can show the relevant room accessibility(with a grey room on that direction) if player click a valid direction
      hero image can be printed at the center of 3x3
      fix the brawler window widget positions
      added mstr to represent monster in the room, we can go deeper to describe the type of monster if needed.
      adjusted a little bit of the button of crawler window
      adjusted the background of the dungeon display and the position of the hero
      Changed the color of the accessible rooms to white in the 3x3 grid. Win/lose message can be displayed but needs to be fully implemented.
      The winning message can display if player is alive with 4 pillars and at the exit.
      commit before merging week5 to xingguo
      can show win and lose message
      frames and canvas can be wiped out if win or lose the game. Leaves room for the stats window and play again button
      added 3 simple button on the win/lose message window. needs to implement the logic
      Adjusted the description and the some readability issue
      map, the 2d array is updated for the visited rooms
      map is now not printing the contents correctly. if we choose to print the traveled room.
      vision potion works now.
      Starting to work on the game stats
      Game stats set up, needs more config
      Updated Readme.md
      Update end game summary
      Update end game summary 2
      Stats print revised
      Stats print revised 2
      Stats print revised 3
      About us and Control windows

Stephanie Liu (47):
      Added packages to clean up codebase structure.  Use pip install -e . to get packages working in your environment.
      Shifted files for more cleanliess and easy packaging structure.
      Script to build db and fill it with monsters and hero classes.
      More folder order to chaos.
      Added dng difficulty to database, added sample scripts as examples to query db.
      Finished adding query helper for database, unit tests for database.
      Fixed a pathing for a dungeon builder test package.
      Removed difficulty setting code from adventurer.  Added loading dict of defaults.
      Refactored adventurerer to include classes, updated tests, refactored dungeon builder to take adventurerer building code to central location, refactored name of variable in db.
      Game_Controller sample
      Refactoring monster and adventurer dungeon char abstraction.  Not working, do not use.
      Continuing to abstract information out of adventurer to dungeon character.  Templating warrior, monster, priestess, healable with some details completed.  Need to finish adding and refractoring unit tests.  Need to implement monsters into dungeon builder.  Need to build character factory.
      Added skills.  Need to test.  Bad steph not testing first
      Skills for characters and tests for classes all in.  Abstraction cleaned up.
      Updated DB to remove pit damage.  Updated room to reflect monsters, dungeon builder to build monsters and place them in rooms with Ogres in pillar rooms, priestess multiple inheritance address, tests written and modified, slight restructuring with tests that are abstract put in separate folder.
      Comment update for dungeon.
      Move test-adventurerer to abstract classes tests.
      bugbash: fixed dungeon_builder relying on max_pit_damage after monster refactor
      feat: saves added.  Refactored dungeon_characters, rooms, and dungeon to contain dictionaries in json-friendly format.  Saves these data into the saves table in the db.  Added new table to sqlite db for saves.  Tested saves, dicts, etc.
      ref: minor refractor for readability in QueryHelper for saves.
      feat: included maps to saves.  Refactored maps to be a dictionary, refactored tests, dungeon builder, save_manager to reflect this.  Included additional column in app.db.
      bug: Fixed call signature in json_dict test.
      feat: Clean up with comments.  Added room.doors property to get dict of doors.  Included tests.
      feat: finished implementing saves in controller.
      ref: whoops, forgot to remove the save game todo.
      feat: load working on backend.  save_manager loads from database using query_helper into form dugeon_builder can consume.  SaveManager.get_saved_games() and load() are both worth reviewing, and DungeonBuilder.load_game(game: dict).  Tests included.
      feat: added loads functionality: changes include calling super init on crawler and brawler build, adding passing self.root to BaseFrame, load_view file, lines 59-84 of game_controller to add loads, modification to set_model method to allow loading from a saved game instead of just building.
      bug: Cheating to get all my pixels to fit.
      com: comments.
      Added save file Spoony Bard for class demo.
      Minor refractor for readability in load_view.py and PEP8 conformity.
      bug: minor visual error in load_view.
      bug: excessive blocking, excessive healing, overhealing, unable to lose, unable to win, location for entrance and exit and adventurer loading as lists vs tuples in dungeon builder.  Steph fixed alllll the things, mwahahaha.
      bug: fixed starting new game.  Current error with menu irregularly causing game to crash.  Looking into it.
      ref: removed debugging statement from monster.py
      feat: added specials to combat.
      bug: string didn't show monster heals.
      bug: clear room of monsters after winning.
      feat: update view with hero's current health upon using potion.
      feat: made new main.py to run game so descriptions are simpler for srs.
      test: added mock classes of adventurer and healable to allow testing of abstract classes.
      doc: added README.md
      docs: added spoony_bard_returns_uml, added and updated README.md
      Minor adjustment.
      bug: reverted save_game in game_controller.py to previous state.
      bug: fixed dynamic combat log in update_combat_log method.  Can scroll to the left or right if text log exceeds width, otherwise static to 85.
      bug: reverted save_game to proper state.
      docs: Pivotal Tracker screenshots in assignment_documents and updated README.md to include hours.  Still needs Git history when Kevin finishes merges

Kevin (74):
      docs: add UML, SRS initial, UI design drafts
      learn: gui testing, not working
      feat: add dungeon crawler basic buttons
      chore: picture added
      feat: add window size 800x600
      feat: week 2 iteration
      learn: getting controller code setup
      learn: meeting
      feat: basic view controller seems to be working
      feat: rename follow convention
      learn: meeting with Tom to discuss Controller code
      learn: MVC after Tom
      bug: removed image for X, in to make dev easier
      feat: passing settings between view and controller
      learn: sending information to model
      docs: remove comments
      bug: name does not update yet
      feat: game creates dungeon and changes view
      bugs: dungeon not created..
      fix: instantiate dungeon first, non-func buttons
      refactor: clear responsibility of controller
      feat: outline for DungeonBrawler
      feat: frames in place for DungeonBrawler
      feat: adv bag sent to view - SUCCESS!
      learn: add signatures for DungeonBrawler
      learn: controller growing pains
      feat: properly set dict for model
      chore: added TODO section
      feat: movement and pillar/potion collection
      docs: add docstrings for methods
      feat: bag display for hero
      docs: new TODO items
      bug: removed str().lower() for model creation
      blocked: able to use potion, not updated in view
      feat: add pillar desc in bag window
      feat: add outline frames for DungeonBrawler
      feat: DungeonBrawler frames with buttons
      feat: add psuedocode for combat
      bug: new game not working
      fix: potions update properly now
      refactor: add helper methods for model access
      feat: clean up branch, saves, maps, bag display
      feat: button navigation implemented
      feat: base Brawler frames implemented
      feat: big red button
      feat: able to get back to DungeonCrawler
      style: clean up lines
      feat: DungeonBrawler attack, potion, frames
      debug: helper button to skip combat added
      bugfix: improved handling of multiple labels
      feat: basic combat implemented
      doc: prep for Demo
      bug: some bugs with damage to dungeon character
      bugfix: health potions update
      feat: combat log is providing actions
      feat: potion use for Brawler working
      docs: clean up comments
      feat: combat turn order
      feat: combat turns implemented, updates combat
      feat: DungeonBrawler logs for special and attack
      docs: add function definitions
      feat: combat win, back to DungeonCrawler
      docs: clean up debug and add docstr
      docs: remove debug comments
      feat: remove debug comments
      feat: clean up combat logic
      feat: special attacks trade blows
      docs: clean up code comments
      feat: post 4pm update
      fix: potions captured in combat
      docs: added for functions in DungeonBrawler
      fix: removed clipping labels after combat
      docs: Removing debug statements
      refactor: clean up combat logic
      fix: adjust frame size to fit help text