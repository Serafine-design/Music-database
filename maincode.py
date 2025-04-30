import sqlite3

Database = 'music.db'

db = sqlite3.connect(Database)
cursor = db.cursor()
sql = "SELECT * FROM music;"
cursor.execute(sql)
results = cursor.fetchall()

for music in results:
    print(f"Music: {music[1]}")

db.close()