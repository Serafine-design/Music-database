import sqlite3

def find_song_using_artist():
    '''Enter genre to find song'''
    artistcheck = 0
    Database = 'music.db'
    number = 1
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "SELECT * From music JOIN artist ON music.artist_id = artist.artist_id;"
    sql2 = "SELECT * FROM music JOIN genre ON music.genre_id = genre.genre_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    userartist = input('Enter your artist of choice please.\n').upper()
    while True:
        print('')
        for artist in results:
            if userartist == artist[5].upper():
                for genre in result2:
                    if genre[1] == artist[1]:
                        print(f"{artist[1]:<30}{genre[5]}")
                        artistcheck = artistcheck + 1
        
        if artistcheck == 0:
            userartist =  input('Not a valid artist please make sure you have the correct spelling.\n').upper()
        else:
            break
    db.close()

find_song_using_artist()