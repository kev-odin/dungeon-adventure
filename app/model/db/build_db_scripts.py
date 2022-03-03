"""
Below are the scripts for building the python sql database.
"""
import sqlite3
con = sqlite3.connect('app.db')
cur = con.cursor()

# cur.execute('''CREATE TABLE dng_diff
#                 (difficulty text, impassable_chance real, hp_chance real, vp_chance real, many_chance real, monster_chance real, max_hp_pots int, max_vp int, row int, col int)''')
#
# cur.execute("INSERT INTO dng_diff VALUES ('Easy', 0.05, 0.1, 0.05, 0.05, 0.1, 2, 2, 5, 5)")
# cur.execute("INSERT INTO dng_diff VALUES ('Medium', 0.07, 0.1, 0.05, 0.1, 0.12, 2, 1, 8, 8)")
# cur.execute("INSERT INTO dng_diff VALUES ('Hard', 0.08, 0.1, 0.05, 0.15, 0.15, 1, 1, 10, 10)")
# cur.execute("INSERT INTO dng_diff VALUES ('Inhumane', 0.1, 0.01, 0.01, 0.3, 0.2, 1, 1, 20, 20)")
#

# cur.execute('''CREATE TABLE classes
#                (name text, hp int, attack_speed int, hit_chance float, min_dmg int, max_dmg int, block_chance float, special text)''')
#
# cur.execute("INSERT INTO classes VALUES ('Warrior', 125, 4, 0.8, 35, 60, 0.2, 'Crushing Blow')")
# cur.execute("INSERT INTO classes VALUES ('Priestess', 75, 5, 0.7, 25, 45, 0.3, 'Heal')")
# cur.execute("INSERT INTO classes VALUES ('Thief', 75, 6, 0.8, 20, 40, 0.4, 'Sneak Attack')")
#
# con.commit()
#
# cur.execute('''CREATE TABLE monsters
#                (name text, hp int, attack_speed int, hit_chance float, min_dmg int, max_dmg int, heal_chance float, min_heal int, max_heal int)''')
#
# cur.execute("INSERT INTO monsters VALUES ('Ogre', 200, 2, 0.6, 30, 60, 0.1, 30, 60)")
# cur.execute("INSERT INTO monsters VALUES ('Gremlin', 70, 5, 0.8, 15, 30, 0.4, 20, 40)")
# cur.execute("INSERT INTO monsters VALUES ('Skeleton', 100, 3, 0.8, 30, 50, 0.3, 30, 50)")

# cur.execute('''CREATE TABLE classes
#                (name text, hp int, attack_speed int, hit_chance float, min_dmg int, max_dmg int, block_chance float, special text)''')

# con.commit()

cur.execute('''CREATE TABLE saves
                (timestamp text, hero_name text, class text, difficulty text, current_hp int, max_hp int, dungeon text, adventurer text, map text)''')

con.commit()

con.close()
