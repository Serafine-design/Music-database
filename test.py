import sqlite3

def print_song_name_asc():
    Database = 'musicwithstream.db'

    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id order by music asc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for music in results:
        print(music)


def print_all_songs():
    '''print all songs'''
    Database = 'musicwithstream.db'

    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "SELECT * FROM music;"
    cursor.execute(sql)
    results = cursor.fetchall()

    userinput = input('yes or no')
    
    if userinput == 'yes':
        print_hello()
    else:
        for music in results:
            print(f"Music: {music[1]}")

    db.close()

print_song_name_asc()