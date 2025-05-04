import sqlite3

def find_song_using_artist():
    '''Enter genre to find song'''
    check = 0
    artistcheck = 0
    Database = 'musicwithstream.db'
    number = 1
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select * from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    userartist = input('Enter your artist of choice please.\n').upper()
    while True:
        print('')
        for artist in results:
            if userartist == artist[6].upper():
                check = check + 1
        if check != 0:
            print('Name                                              Genre               Streams on Spotify')
            for artist in results:
                if userartist == artist[6].upper():
                    print(f"{artist[1]:<50}{artist[6]:<20}{artist[4]}")
            break
        else:
            userartist = input('Not a valid artist please make sure you have the correct spelling.\n').upper()
            check = 0
    db.close()

find_song_using_artist()