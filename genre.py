import sqlite3

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

find_song_using_genre()
