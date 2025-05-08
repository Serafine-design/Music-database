import sqlite3
def print_random_song():
    import random
    Database = 'musicwithstream.db'

    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music_id, music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
