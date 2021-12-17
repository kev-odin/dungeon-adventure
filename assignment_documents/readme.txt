Group: Halt Catch Fire (HCF)
The Spoony Bard

Extra-credit attempts:
- Easy, Medium, Hard, and Inhumane difficulty in dungeon (and consequently rooms!) with a simple builder!
- Each pillar collected will add powers to the adventurer:
    1) Abstraction - Health potions collected are doubled
    2) Polymorphism - Vision potions collected are doubled
    3) Inheritance - Pit damage is cut in reduced
    4) Encapsulation - Health potions have increased potency
    5) All pillars collected - Max hitpoints can be increased with potions
- Adventurers have different default values based on the difficulty:
    1) easy - more than 100 hitpoints, two health and vision potions
    2) medium - more than 95 hitpoints, one health and vision potion
    3) hard - more than 90 hitpoints, one health and vision potion
    3) inhumane - more than 85 hitpoints, ONLY one vision potion
- Unique flavor text for full dungeon immersion.
- Plural values as needed based on the value at collection.
- Endgame summary results shown upon player win or loss.

What we worked on & how long:
Kevin (Total time: ~45 hours)
adventurer.py - 20 hours
testing - 10 hours
UML beauty - 5 hours
health_potion.py - 2 hours
vision_potion.py - 2 hours
Group meetings - 2 hours
refactoring main.py - 4 hours
potion_factory.py - 1 hour

Xingguo - 34+ hours
map.py - 1 hour
main.py - 24 hours
test_map.py - 9 hours
Group meetings - 2 hours

Steph -> Current time spent: 36+ hours total
I need to stop refactoring code for fun and writing a bunch of tests.
Time to working: 4.5 hours to minimal viable functionality.
This readme!  Now with more exclamation points!
Bug bash & refactoring~!
UML uglification - 2 hr
dungeon_builder.py
dungeon.py
room.py -> Done
test_room.py -> Done
test_dungeon.py
test_dungeon_iterator.py
test_dungeon_builder.py
Group meetings - 2 hours

Shortcomings:
Steph - Mock tests would be more robust.  Integration testing would be helpful.  No GUI.  The potions and pits behind
inaccessible walls was an intentional homage to games we've played before, and Steph refuses to solve them since all
pillars are accessible and she finds it funny.

Kevin - I think that I could have utilized the factory pattern a little bit more. Right now health potions seem to be the 
only object that is being made. We discovered later that vision potions were better implemented with map.py

Questions for Tom:
Best practices for cleaning up class member variables necessary for creation, but not necessary after.
Best practices for writing clean unit tests with redundant code or more complex code.
Kevin - Why are properties not clear with setting dictionaries? I kept running into issues with setting values.
Kevin - Where is the best place for numerous print statments?

Git ShortLog:
308241561 (Xingguo):
      added main empty file to test git/github
      merge main into xingguo Merge branch 'main' into xingguo
      Add empty main and map py
      merge test to xingguo
      basic logic draft of the main and map py
      added gitignore file
      added some logic to the main, still learning all the process with the help of my teammates class
      some more brainstorming ideas for main
      updated the first menu....
      merge steph's branch to xingguo
      merge kev's branch to xingguo
      add empty test main and test map py
      more logic updates with main
      merge steph's branch to xingguo
      struggling with all the logics, a good struggle though
      merge steph's branch to xingguo
      updated main with more logic
      more main logic, created dungeon and adventure, but still need more reading
      merge kevin's branch to xingguo
      moving forward, slowly, but still. printed out the dungeon, and the current room.
      can move around the dungeon and print the traveled rooms
      merge kevin's branch to xingguo
      added winning condition
      updated
      I want to merge all of your branches, so I need to push mine first. Do not know if there is another way around
      merge test branch to xingguo
      modified main game logic
      add kevin's branch to xingguo
      adding map classgit add .
      debugging sos
      first win
      second pass of the game
      third pass of the game. Working now still needs to do some cleaning up
      Some git issue, had no idea why
      cleaning up the while loop
      vision potion works now
      corner cases taken cared of. Now it should not break easily.
      before I merge kevin's branch to xingguo
      cleaning up the map
      Thanks Kevin
      begin test classes
      commenting on key points
      test classes and one bug fixing in the main
      yeah! all done :)
      updated test class
      clearning up the comments
      Okay, now it is prettier.
      added play again for main and documentations for map

Kevin:
      feat: add initial assignment files
      feat: add boilerplate for adventurer class
      feat: add boilerplate for potion abc
      docs: reorg UML elements, add class field, add pdf
      test: add basic init tests for adventurer
      feat: add basic potion setup
      feat: add random hp value, add create adventurer
      test: add negative value tests
      feat: add has_all_pillars, update potions found
      feat: new current_health, and max health
      docs: add docstring to classes and methods
      feat: add brainstorm functionality
      test: writing tests for potions, import lament T_T
      feat: add functions to alter adventurer game state
      test: add tests for inventory, health, and pillars
      feat: add readable string, add cheat codes
      feat: add names for heal amounts, clean comments
      test: add type checking tests
      Merge branch 'kevc_adventurer' into test
      feat: clean up methods, add unique potion names
      feat: add robust error catching
      test: add comprehensive tests
      feat: add docstrings, remove extra functions
      docs: update readme
      feat: plural modification added
      test: fix isInstance
      docs: initial UML solution draft
      docs: add UML classes, fields, and methods
      feat: plural statements
      refactor: adventurer class can use health potions
      Merge branch test into 'kevc_adventurer'
      docs: add UML diagram relationships
      docs: UML add composition, map signatures
      refactor: used built-in function
      refactor: use adventurer function, print statement
      feat: better character creation
      test: character creation tests
      feat: add difficulty descriptions
      feat: add pillar powers for adventurer collection
      test: pillar power tests basic mechanics
      feat: altered 'kevin's starting health
      feat: add dialogue for entrance/exit rooms
      refactor: consistent printing
      refactor: add common as baseline potion
      feat: add engame stat counters
      fix: print align
      refactor: moving print statements to main
      refactor: removed print statements from adventurer
      refactor: clean up comments
      Merge branch 'kevc_test_refactor' into test
      docs: add new endgame screen for turn in
      refactor: add static method for endgame
      refactor: add input handling for replay
      refactor: clean up summary
      docs: add turn-in results

Stephanie:
      Just room, need to save my tests.
      Create test_room.py
      Traversal works.
      basic dungeon functionality working.  Need to randomize generation.
      Merge pull request #2 from kev-odin/kevc
      Merge pull request #3 from kev-odin/test
      Merge branch 'steph' of github.com:kev-odin/The_Spoony_Bard
      added dungeon iterator and tests
      added room factory.  More Pillar Bug Bashing.
      I think this was before I started messing with it today.  Here's hoping.
      modifying variables for less redundancy and variable management.  Updated room and test_room.  Updated other files to match.  Contains bug from no longer tracking visited.  Irregular stack overflow.  Still identifying issue.
      Resolved the stack overflow bug.  Refactored dungeon some more.
      more refractoring and restructoring.  room with single door setter and getter.
      Commented dungeon.  Added capable completion unit tests and adventurer unit tests.  Cleaned up iterator.  Added more room tests.  Added more dungeon tests.
      Added collect_potions and pit_damage dungeon methods and testing.
      Added collect pillars.
      Created dungeon builder.  Need to clean up my tests a LOT.  They messy.  Need more dungeon builder tests and more private method tests.
      fixed iterator test
      Added rest of basic tests for dungeon_builder.  Also cleaned up typo in room, updated time tracker.
      added some comments to builder
      typo fix
      Updated readme for tracking todos and what's finished and time.
      Added get_visible_dungeon_string method in dungeon to simplify Xingguo's map making! And test.
      Fixed a bug, fixed Kev's suggestion, added total_rows and total_columns property for Xingguo map building, added a few more tests and clarified some comments.
      Updated room.py with Kev's refractoring suggestion.
      Merge pull request #4 from kev-odin/steph
      Fixed collect_potions in dungeon.py to not overwrite dungeon.
      Fixed vision potion bug (I hope, ahaha)
      @ symbol on map next to contents where adventurer is.
      added map generation to dungeon builder so main doesn't need to track rows / cols
      updated readme with Xingguo's hours, main.py with dungeon refactor, and unit_tests/test_dungeon.py with refractor
      added win-lose results as is.  Added wasd keymapping for main.py.
      Made static methods static.
      added clarification around what found pillars do and a notice to played if they've found them all.
      Added map key to describe map.
      Updated UML to reflect recent refractors.  I think.