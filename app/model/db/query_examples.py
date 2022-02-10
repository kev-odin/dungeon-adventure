import sqlite3

con = sqlite3.connect('app.db')
cur = con.cursor()

print("\nMonsters Table:")
for row in cur.execute('SELECT * FROM monsters'):
    print(row)

print("\nClasses Table:")
for row in cur.execute('SELECT * FROM classes'):
    print(row)

