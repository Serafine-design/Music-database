import sqlite3

def print_song_name_asc():
    Database = 'musicwithstream.db'

    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id order by music asc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('Name                                              Artist              Genre               Streams on spotify')
    for music in results:
        print(f"{music[0]:<50}{music[2]:<20}{music[3]:<20}{music[1]:<20}")

def print_song_name_desc():
    Database = 'musicwithstream.db'

    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id order by music desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('Name                                              Artist              Genre               Streams on spotify')
    for music in results:
        print(f"{music[0]:<50}{music[2]:<20}{music[3]:<20}{music[1]:<20}")
def print_song_stream_asc():
    Database = 'musicwithstream.db'

    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id order by streams asc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('Name                                              Artist              Genre               Streams on spotify')
    for music in results:
        print(f"{music[0]:<50}{music[2]:<20}{music[3]:<20}{music[1]:<20}")
def print_song_stream_desc():
    Database = 'musicwithstream.db'

    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id order by streams desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('Name                                              Artist              Genre               Streams on spotify')
    for music in results:
        print(f"{music[0]:<50}{music[2]:<20}{music[3]:<20}{music[1]:<20}")



def print_all_songs():
    '''print all songs'''
    count = 0
    userinput = input('How should I print the songs?\n1. According to Name\n2. According to Number of Streams\n')
    while True:
        if count == 1:
            break
        try:
            userinput = int(userinput)
        except ValueError:
            userinput = input('please enter a valid number\n')
        if userinput == 1:
            print('How should I print the songs')
            userinput2 = input('1. Alphabetical order\n2. Reverse alphabetical order.\n')
            while True:
                try: 
                    userinput2 = int(userinput2)
                    if userinput2 == 1:
                        print_song_name_asc()
                        count = count + 1
                        break
                    elif userinput2 == 2:
                        print_song_name_desc()
                        count = count + 1
                        break
                    else:
                        userinput2 = input('plase enter a valid number\n')
                except ValueError:
                    userinput2 = input('please enter a valid number\n')
        elif userinput == 2:
            print_song_stream_desc()
            break
        else:
            userinput = input('Please enter a valid number\n')

print_all_songs()