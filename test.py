import sqlite3

db = sqlite3.connect('music.db')
cursor = db.cursor()
sql = "SELECT * FROM music;"
cursor.execute(sql)
results = cursor.fetchall()

for music in results:
    print(music)

db.close()