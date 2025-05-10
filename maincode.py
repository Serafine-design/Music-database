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
        except ValueError:
            userinput = input('please enter a valid number\n')


def find_song_using_genre():
    '''Enter genre to find song'''
    Database = 'musicwithstream.db'
    number = 1
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "SELECT * From music JOIN artist ON music.artist_id = artist.artist_id;"
    cursor.execute(sql)
    results = cursor.fetchall()

    usergenre = input('What genre do you want?\n1. Hip Hop\n2. Jazz\n3. Religious\n4. Rock\n5. J-pop\n6. K-pop\n7. Classical\n8. Rap\n9. Pop\n10. EDM\n11. Alternative rock\n12. Soul\n13. Funk\n')
    while True:
        try:
            usergenre = int(usergenre)
            if usergenre > 15:
                usergenre = input('please enter a valid number\n')
            else:
                print(f"Name                                              Artist              Streams on spotify")
                for music in results:
                    if music[3] == usergenre:
                        print(f"{music[1]:<50}{music[6]:<20}{music[4]}")
                break
        except ValueError:
            usergenre = input('Please enter a valid number\n')
        
    db.close()

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

def print_random_song():
    import random
    Database = 'musicwithstream.db'

    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music_id, music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    number = (random.randint(0,79))
    while True:
        try:
            number = int(number)
            break
        except ValueError:
            number = (random.randint(0,79))
    print('Name                                              Artist              Genre               Streams on spotify')
    for music in results:
        if music[0] == number:
            print(f"{music[1]:<50}{music[3]:<20}{music[4]:<20}{music[2]:<20}")

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



def main_code():
    '''main code'''
    userinput = input("1. See all songs\n2. Enter genre to find song\n3. Enter artist to find song\n4. Don't know what you want? \n5. Enter song name to find details\n6. EXIT\n")
    global quit
    while True:
        try:
            userinput = int(userinput)
            if userinput == 1:
                print_all_songs()
                break
            elif userinput == 2:
                find_song_using_genre()
                break
            elif userinput == 3:
                find_song_using_artist()
                break
            elif userinput == 4:
                print_random_song()
                break
            elif userinput == 5:
                enter_song_to_print()
                break
            elif userinput == 6:    
                quit = 'yes'
                break
            else:
                userinput = input("Please enter a valid number\n")
        except ValueError:
            userinput = input('Please enter a valid number\n')


#main code

quit = "no"
while quit =="no":
    main_code()
    