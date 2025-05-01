import sqlite3

def find_song_using_artist():
    '''Enter genre to find song'''
    Database = 'music.db'
    number = 1
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "SELECT * FROM music;"
    sqlartist = "SELECT * FROM artist"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.execute(sqlartist)
    resultartist = cursor.fetchall()

    print(results)
    print(resultartist)

    userartist = input('Enter your artist of choice please.')
    while True:
        for artist in resultartist:
            if userartist == artist[1]:
                for music in results:
                    if music[3] == artist[0]:
                        print(music[1])
                break
            else:
                print('no such artist')


                
        
    db.close()

find_song_using_artist()