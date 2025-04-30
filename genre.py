import sqlite3

def find_song_using_genre():
    '''Enter genre to find song'''
    Database = 'music.db'
    number = 1
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "SELECT * FROM music;"
    cursor.execute(sql)
    results = cursor.fetchall()

    usergenre = input('What genre do you want?\n1. Hip Hop\n2. Jazz\n3. Religious\n4. Rock\n5. J-pop\n6. K-pop\n7. Classical\n8. Rap\n9. Pop\n10. EDM\n12. Alternative rock\n13. Soul\n14. Funk\n')
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

find_song_using_genre()
import sqlite3

def find_song_using_genre():
    '''Enter genre to find song'''
    Database = 'music.db'
    number = 1
    db = sqlite3.connect(Database)
    cursor = db.cursor()
    sql = "SELECT * FROM music;"
    cursor.execute(sql)
    results = cursor.fetchall()

    usergenre = input('What genre do you want?\n1. Hip Hop\n2. Jazz\n3. Religious\n4. Rock\n5. J-pop\n6. K-pop\n7. Classical\n8. Rap\n9. Pop\n10. EDM\n12. Alternative rock\n13. Soul\n14. Funk\n')
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

find_song_using_genre()