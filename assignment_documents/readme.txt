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

Xingguo - 25 hours
map.py - 1 hour
main.py - 24 hours
Group meetings - 2 hours

Steph -> Current time spent: 30 hours total so far?!
I need to stop refactoring code for fun and writing a bunch of tests.
Time to working: 4.5 hours to minimal viable functionality.
This readme!  Now with more exclamation points!
dungeon_builder.py
dungeon.py
room.py -> Done
test_room.py -> Done
test_dungeon.py
test_dungeon_iterator.py
test_dungeon_builder.py
Group meetings - 2 hours

Shortcomings:
Mock tests would be more robust since I had to delete most of my private method tests once methods were no longer
private or no longer predictable.  Testing successful traversal is an okay compromise?  But less helpful if something
more specific breaks with modification.

Questions for Tom:
Best practices for cleaning up class member variables necessary for...creation, but not necessary after.
Best practices for writing clean unit tests with redundant code or more complex code.
Kevin - Why are properties not clear with setting dictionaries? I kept running into issues with setting values.
