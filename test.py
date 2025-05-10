import sqlite3

def enter_song_to_print():
    breaks = False
    check = 0
    import random
    Database = 'musicwithstream.db'

    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music_id, music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    while True:
        if breaks:
            break
        while True:
            if check == 0:
                songinput = input("Please enter your song name or type in exit to exit.\n").upper()
            elif check > 0:
                    songinput = input("Please enter a valid song.\n").upper()
                    check = 0
            if songinput == 'EXIT':
                breaks = True
                break
            else:
                for music in results:
                    if songinput == music[1].upper():
                        print('Name                                              Artist              Genre               Streams on spotify')
                        print(f"{music[1]:<50}{music[3]:<20}{music[4]:<20}{music[2]:<20}")
                        check = 0
                        break
                    else:    
                        check = check + 1

enter_song_to_print()