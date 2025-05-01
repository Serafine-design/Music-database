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
    sql = "SELECT * FROM music;"
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
                        print(music[1])
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
    cursor.execute(sql)
    results = cursor.fetchall()

    userartist = input('Enter your artist of choice please.\n').upper()
    while True:
        print('')
        for artist in results:
            if userartist == artist[5].upper():
                print(artist[1])
                artistcheck = artistcheck + 1
        
        if artistcheck == 0:
            userartist =  input('Not a valid artist please make sure you have the correct spelling.\n').upper()
        else:
            break
    db.close()

# Main code

userinput = int(input('1 or 2 or 3'))
if userinput == 1:
    print_all_songs()
elif userinput == 2:
    find_song_using_genre()
elif userinput == 3:
    find_song_using_artist()