import sqlite3
con = sqlite3.connect('app.db')
cur = con.cursor()

cur.execute('''CREATE TABLE classes
               (name text, hp int, attack_speed int, hit_chance float, min_dmg int, max_dmg int, block_chance float, special text)''')

cur.execute("INSERT INTO classes VALUES ('Warrior', 125, 4, 0.8, 35, 60, 0.2, 'Crushing Blow')")
cur.execute("INSERT INTO classes VALUES ('Priestess', 75, 5, 0.7, 25, 45, 0.3, 'Heal')")
cur.execute("INSERT INTO classes VALUES ('Thief', 75, 6, 0.8, 20, 40, 0.4, 'Sneak Attack')")

con.commit()

cur.execute('''CREATE TABLE monsters
               (name text, hp int, attack_speed int, hit_chance float, min_dmg int, max_dmg int, heal_chance float, min_heal int, max_heal int)''')

cur.execute("INSERT INTO monsters VALUES ('Ogre', 200, 2, 0.6, 30, 60, 0.1, 30, 60)")
cur.execute("INSERT INTO monsters VALUES ('Gremlin', 70, 5, 0.8, 15, 30, 0.4, 20, 40)")
cur.execute("INSERT INTO monsters VALUES ('Skeleton', 100, 3, 0.8, 30, 50, 0.3, 30, 50)")

con.commit()

con.close()
