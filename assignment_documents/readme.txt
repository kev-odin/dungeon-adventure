The Spoony Bard
Extra-credit attempts:
Easy, Medium, Hard, and Inhumane difficulty in dungeon (and consequently rooms!) with a simple builder!
Each pillar collected will add powers to the adventurer:
    1) Abstraction - Health potions collected are doubled
    2) Polymorphism - Vision potions collected are doubled
    3) Inheritance - Pit damage is cut in reduced
    4) Encapsulation - Health potions have increased potency
    5) All pillars collected - Max hitpoints can be increased with potions

What we worked on & how long:
Kevin (Total time: 43 hours)
UML beauty - 5 hours
adventurer.py - 20 hours
health_potion.py - 2 hours
vision_potion.py - 2 hours
potion_factory.py - 1 hour
testing - 10 hours
Group meetings - 2 hours
refactoring - 1 hour

Xingguo - 34 hours
map.py - 1 hour
main.py - 24 hours
test_map.py - 9 hours
Group meetings - 2 hours

Steph -> Current time spent: 34 hours total so far?!
I need to stop refactoring code for fun and writing a bunch of tests.
Time to working: 4.5 hours to minimal viable functionality.
This readme!  Now with more exclamation points!
Bug bash & refactoring~!
dungeon_builder.py
dungeon.py
room.py -> Done
test_room.py -> Done
test_dungeon.py
test_dungeon_iterator.py
test_dungeon_builder.py
Group meetings - 2 hours

Shortcomings:
Mock tests would be more robust.  Integration testing would be helpful.  No GUI.  The potions and pits behind
inaccessible walls was an intentional homage to games we've played before, and Steph refuses to solve them since all
pillars are accessible and she finds it funny.

Questions for Tom:
Best practices for cleaning up class member variables necessary for creation, but not necessary after.
Best practices for writing clean unit tests with redundant code or more complex code.
Kevin - Why are properties not clear with setting dictionaries? I kept running into issues with setting values.
