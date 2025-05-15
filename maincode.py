# music database code
# import databse
import sqlite3
# Variables
global one
one = 1
global two
two = 2
global zero
zero = 0
#fuctions

# function print songs
def print_song_name_asc():
    '''Printing according to song names in alphabetical order'''
    # Variables
    Database = 'musicwithstream.db'
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id order by music asc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Printing results nicely
    print(f"{'Name':<50}{'Artist':<20}{'Genre':<20}{'Streams on spotify'}")
    for music in results:
        print(f"{music[0]:<50}{music[2]:<20}{music[3]:<20}{music[1]}")

#fuction print songs depending on name descending
def print_song_name_desc():
    '''Printing according to song name in reverse alphabetical order'''
    # Variables
    Database = 'musicwithstream.db'
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id order by music desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"{'Name':<50}{'Artist':<20}{'Genre':<20}{'Streams on spotify'}")
    # Printing results nicely
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
            # Check for invalid inputs
            if usermargin < zero:
                usermargin = input('No music can have negative streams\n')
            else:
                for music in results:
                    if music[1] >= usermargin:
                        check = check + one
                if check == zero:
                    usermargin = input(f'There are no songs that have a higher stream count then {usermargin} please input another number\n')
                # Print results nicely
                else:
                    print(f"{'Name':<50}{'Artist':<20}{'Genre':<20}{'Streams on spotify'}")
                    for music in results:
                        if music[1] >= usermargin:
                            print(f"{music[0]:<50}{music[2]:<20}{music[3]:<20}{music[1]:<20}")
                    break
        # Check for value errors
        except ValueError:
            usermargin = input('Please enter a valid integer\n')

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
    # Ask for user input
    usermargin = input('What is the maximum amount of streams a song should have?\n')
    while True:
        try:
            usermargin = int(usermargin)
            # Check for invalid inputs
            if usermargin < zero:
                usermargin = input('No songs can have negative streams\n')
            else:
                for music in results:
                    if music[1] <= usermargin:
                        check = check + one
                if check == zero:
                    usermargin = input(f'There are no songs that have a lower stream count then {usermargin} please input another number\n')
                # print results nicely
                else:
                    print(f"{'Name':<50}{'Artist':<20}{'Genre':<20}{'Streams on spotify'}")
                    for music in results:
                        if music[1] <= usermargin:
                            print(f"{music[0]:<50}{music[2]:<20}{music[3]:<20}{music[1]:<20}")
                    break
        # Check for value errors
        except ValueError:
            usermargin = input('Please enter a valid integer\n')
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

# print songs according to stream
def print_according_to_stream():
    '''Printing according to number of streams based on user input'''
    print('How should I print according to streams')
    # Ask for input
    userinput = input('1. Print from smallest to largest\n2. Print from largest to smallest\n3. Choose minimum stream count\n4. Choose maximim stream count\n')
    # act on input
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
                break
            # Check for invalid inputs
            else:
                userinput = input('Please input a valid number\n')
        # Check for value errors
        except ValueError:
            userinput = input('Please input a valid number\n')

# function to just print all songs
def print_all_songs():
    '''print all songs'''
    # Variables
    count = 0
    userinput = input('How should I print the songs?\n1. According to Name\n2. According to Number of Streams\n')
    # Loop to make the code run as long as the user wants it to
    while True:
        # Check for invalid inputs
        if count == one:
            break
        try:
            userinput = int(userinput)
            # Ask how to print the songs
            # Pring songs according to the names
            if userinput == one:
                print('How should I print the songs')
                userinput2 = input('1. Alphabetical order\n2. Reverse alphabetical order.\n')
                # Loop so that the user is asked for a valid input infinite times.
                while True:
                    try: 
                        userinput2 = int(userinput2)
                        if userinput2 == one:
                            print_song_name_asc()
                            count = count + one
                            break
                        elif userinput2 == two:
                            print_song_name_desc()
                            count = count + one
                            break
                        else:
                            userinput2 = input('plase enter a valid number\n')
                    # Check for Value errors
                    except ValueError:
                        userinput2 = input('please enter a valid number\n')
            # Print songs according to the stream count
            elif userinput == two:
                print_according_to_stream()
                break
            else:
                userinput = input('Please enter a valid number\n')
        # Check for Value errors
        except ValueError:
            userinput = input('please enter a valid number\n')

# function to find song using genre
def find_song_using_genre():
    '''Enter genre to find song'''
    # Variables
    numberofgenres = 13
    Database = 'musicwithstream.db'
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "SELECT * From music JOIN artist ON music.artist_id = artist.artist_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Ask for input on the genre of choice
    usergenre = input('What genre do you want?\n1. Hip Hop\n2. Jazz\n3. Religious\n4. Rock\n5. J-pop\n6. K-pop\n7. Classical\n8. Rap\n9. Pop\n10. EDM\n11. Alternative rock\n12. Soul\n13. Funk\n')
    # Loop until the user wants it to stop
    while True:
        # Check for invalid inputs
        try:
            usergenre = int(usergenre)
            if usergenre > numberofgenres:
                usergenre = input('please enter a valid number\n')
            elif usergenre <= zero:
                usergenre = input('please enter a valid number\n')
            else:
                # Print the results nicely
                print(f"Name                                              Artist              Streams on spotify")
                for music in results:
                    if music[3] == usergenre:
                        print(f"{music[1]:<50}{music[6]:<20}{music[4]}")
                break
        # Check for Value errors
        except ValueError:
            usergenre = input('Please enter a valid number\n')
        db.close()


#function to find song using artist
def find_song_using_artist():
    '''Enter genre to find song'''
    # Variables
    check = 0
    Database = 'musicwithstream.db'
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select * from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Ask for input on the Artist of choice
    # Capitalise all the letters 
    userartist = input('Enter your artist of choice please.\n').upper()
    # Run until the user says stop
    while True:
        # Check if the user wants the code to stop
        if userartist == 'EXIT':
            break
        # Check if the artist is in the database
        else:
            for artist in results:
                if userartist == artist[6].upper():
                    check = check + one
            if check != 0:
                # Pring results nicely
                print(f"{'Name':<50}{'Genre':<20}{'Streams on spotify'}")
                for artist in results:
                    if userartist == artist[6].upper():
                        print(f"{artist[1]:<50}{artist[6]:<20}{artist[4]}")
                break
            # Check for invalid inputs
            else:
                userartist = input('Not a valid artist please make sure you have the correct spelling.\n').upper()
                check = 0
    db.close()


#function to pring a random song
def print_random_song():
    '''output a random song'''
    import random
    # Variables
    Database = 'musicwithstream.db'
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music_id, music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Create a random number
    number = (random.randint(0,79))
    # Check if the number is a integer (I don't know how this code works so I added this just in case the number is a float)
    while True:
        try:
            number = int(number)
            break
        # Check if number is a float
        except ValueError:
            number = (random.randint(0,79))
    # Print results nicely
    print('Try this song')
    print(f"{'Name':<50}{'Artist':<20}{'Genre':<20}{'Streams on spotify'}")    
    for music in results:
        # Go through database to find result
        if music[0] == number:
            print(f"{music[1]:<50}{music[3]:<20}{music[4]:<20}{music[2]}")
    db.close()

#function to find the details of a song through the name
def enter_song_to_print():
    '''Find song details through name'''
    # Variables
    breaks = False
    check = 0
    import random
    Database = 'musicwithstream.db'
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "Select music_id, music, streams, artist, genre from music INNER JOIN artist on music.artist_id = artist.artist_id INNER JOIN genre on music.genre_id = genre.genre_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Loop until user says so
    while True:
        # Check if the loop should break
        if breaks:
            break
        # Choose the method to ask for user input depending on the past input
        while True:
            if check == zero:
                songinput = input("Please enter your song name or type in exit to exit.\n").upper()
            elif check > zero:
                    songinput = input("Song not in database\n").upper()
                    check = zero
            #Check if the user wants the loop to stop
            if songinput == 'EXIT':
                breaks = True
                break
            # If the user inputs a valid name
            else:
                # Check if there is a corresponding song 
                for music in results:
                    # Print results nicely
                    if songinput == music[1].upper():
                        print('')
                        print(f"{'Name':<50}{'Artist':<20}{'Genre':<20}{'Streams on spotify'}")
                        print(f"{music[1]:<50}{music[3]:<20}{music[4]:<20}{music[2]:<20}")
                        check = zero
                        break
                    # If there is no corresponding song then ask for a valid input
                    else:    
                        check = check + one
    db.close()

#fucntion to run all the other functions
def main_code():
    '''main code'''
    # Ask for user input
    print('What should I do?')
    userinput = input("1. See all songs\n2. Enter genre to find song\n3. Enter artist to find song\n4. Don't know what you want? \n5. Enter song name to find details\n6. EXIT\n")
    global quit
    #depending on input decide which function to run
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
            #Check for invalid inputs
            else:
                userinput = input("Please enter a valid number\n")
        # Check for value errors
        except ValueError:
            userinput = input('Please enter a valid number\n')

# main code
# Run main code until the user says to stop
print('-----------------------------')
print('Welcome to the music database')
print('-----------------------------')
quit = "no"
while quit =="no":
    main_code()
