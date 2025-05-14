import sqlite3
global one
one = 1
global two
two = 2
global zero
zero = 0
# print songs depending on stream count ascending
def print_song_stream_asc():
    '''Printing according to number of streams from smallest to biggest'''
    # Variables
    Database = 'musicwithstream.db'
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id order by streams asc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Printing results nicely
    print(f"{'Name':<50}{'Artist':<20}{'Genre':<20}{'Streams on spotify'}")
    for music in results:
        print(f"{music[0]:<50}{music[2]:<20}{music[3]:<20}{music[1]:<20}")

# print songs depending on stream count descending
def print_song_stream_desc():
    '''Printing according to number of streams from largest to smallest'''
    # Variables
    Database = 'musicwithstream.db'
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id order by streams desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Printing results nicely
    print(f"{'Name':<50}{'Artist':<20}{'Genre':<20}{'Streams on spotify'}")
    for music in results:
        print(f"{music[0]:<50}{music[2]:<20}{music[3]:<20}{music[1]}")

# print songs depending on stream count ascending after choosing minimum
def print_song_stream_asc_min():
    '''Printing according to number of streams from smallest to biggest'''
    # Variables
    check = 0
    Database = 'musicwithstream.db'
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id order by streams asc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    usermargin = input('What is the minimum amount of streams a song should have?\n')
    while True:
        try:
            usermargin = int(usermargin)
            for music in results:
                if music[1] >= usermargin:
                    check = check + one
            if check == zero:
                usermargin = input(f'There are no songs that have a higher stream count then {usermargin} please input another number\n')
            else:
                print(f"{'Name':<50}{'Artist':<20}{'Genre':<20}{'Streams on spotify'}")
                for music in results:
                    if music[1] >= usermargin:
                        print(f"{music[0]:<50}{music[2]:<20}{music[3]:<20}{music[1]:<20}")
                break
        except ValueError:
            usermargin = input('Please enter a valid number\n')

# print songs depending on stream count descending after choosing maximum
def print_song_stream_desc_max():
    '''Printing according to number of streams from largest to smallest'''
    # Variables
    check = 0
    Database = 'musicwithstream.db'
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id order by streams desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    usermargin = input('What is the maximum amount of streams a song should have?\n')
    while True:
        try:
            usermargin = int(usermargin)
            for music in results:
                if music[1] <= usermargin:
                    check = check + one
            if check == zero:
                usermargin = input(f'There are no songs that have a lower stream count then {usermargin} please input another number\n')
            else:
                print(f"{'Name':<50}{'Artist':<20}{'Genre':<20}{'Streams on spotify'}")
                for music in results:
                    if music[1] <= usermargin:
                        print(f"{music[0]:<50}{music[2]:<20}{music[3]:<20}{music[1]:<20}")
                break
        except ValueError:
            usermargin = input('Please enter a valid number\n')


# print songs depending on stream count ascending
def print_according_to_stream():
    '''Printing according to number of streams based on user input'''
    userinput = input('1. Print from smallest to largest\n2. Print from largest to smallest\n3. Choose minimum stream count\n4. Choose maximim stream count\n')
    while True:
        try:
            userinput = int(userinput)
            if userinput == 1:
                print_song_stream_asc()
                break
            elif userinput == 2:
                print_song_stream_desc()
                break
            elif userinput == 3:
                print_song_stream_asc_min()
                break
            elif userinput == 4:
                print_song_stream_desc_max()
            else:
                userinput = input('Please input a valid number\n')
        except ValueError:
            userinput = input('Please input a valid number\n')

print_according_to_stream()