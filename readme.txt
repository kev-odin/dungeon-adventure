The Spoony Bard
Extra-credit attempts:
Easy, Medium, Hard, and Inhumane difficulty in dungeon (and consequently rooms!) with a simple builder!

What we worked on & how long:
Kevin
UML beauty
adventurer.py
health_potion.py
vision_potion.py
potion_factory.py
(observer, observable?)

Xingguo
map.py
dungeon_adventure.py

Steph -> Current time spent: 30 hours total so far?!
I need to stop refactoring code for fun and writing a bunch of tests.
Time to working: 4.5 hours to working with tests in one giant dungeon and room class
This readme!  Now with more exclamation points!
dungeon_builder.py
dungeon.py
room.py -> Done?
test_room.py -> Done?  -> TODO test private methods?
test_dungeon.py -> TODO test private methods
test_dungeon_iterator.py
test_dungeon_builder.py -> TODO more extensive testing, user error testing


Shortcomings:
Mock tests would be more robust since I had to delete most of my private method tests once methods were no longer
private or no longer predictable.  Testing successful traversal is an okay compromise?  But less helpful if something
more specific breaks with modification.

Questions for Tom:
Best practices for cleaning up class member variables necessary for...creation, but not necessary after.
Best practices for writing clean unit tests with redundant code or more complex code.