import sqlite3

def print_all_songs():
    '''print all songs'''
    Database = 'music.db'

    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "SELECT * FROM music;"
    cursor.execute(sql)
    results = cursor.fetchall()

    for music in results:
        print(f"Music: {music[1]}")

    db.close()

def find_song_using_genre():
    '''Enter genre to find song'''
    Database = 'music.db'
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
                for music in results:
                    if music[3] == usergenre:
                        print(f"{music[1]:<50}{music[5]}")
                break
        except ValueError:
            usergenre = input('Please enter a valid number\n')
        
    db.close()

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



def main_code():
    '''main code'''
    userinput = input('1. See all songs\n2. Enter genre to find song\n3. Enter artist to find song\n Exit \n')
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
                quit = "yes"
                break
            else:
                userinput = input("Please enter a valid number\n")
        except ValueError:
            userinput = input('Please enter a valid number\n')


#main code

quit = "no"
while quit =="no":
    main_code()
    