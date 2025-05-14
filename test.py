import sqlite3
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
    print('got here')
    while True:
        try:
            number = int(number)
            break
        # Check if number is a float
        except ValueError:
            number = (random.randint(0,79))
        # Print results nicely
    print(f"{'Name':<50}{'Artist':<20}{'Genre':<20}{'Streams on spotify'}")    
    for music in results:
        # Go through database to find result
        if music[0] == number:
            print(f"{music[1]:<50}{music[3]:<20}{music[4]:<20}{music[2]}")
    db.close()

print_random_song()