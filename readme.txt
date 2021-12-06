The Spoony Bard
Extra-credit attempts:
Easy, Medium, Hard, and Inhumane difficulty in dungeon (and consequently rooms!) -> TODO finish

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

Steph
This readme!  Now with more exclamation points!
TODO make dungeon builder to keep creation of rooms and dungeons together in one place and have different difficulties.
dungeon.py -> Likely needs more features for Xingguo.
test_dungeon.py -> TODO add more tests and error checking
room.py -> Done?
test_room.py -> Done?

Shortcomings:
Mock tests would be more robust since I had to delete most of my private method tests once methods were no longer
private or no longer predictable.  Testing successful traversal is an okay compromise?  But less helpful if something
more specific breaks with modification.

Questions for Tom:
Best practices for cleaning up class member variables necessary for...creation, but not necessary after.
Best practices for writing clean unit tests with redundant code or more complex code.