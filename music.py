import sqlite3 as lite

def music_data():
    con = lite.connect('music.db')

    with con:
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS artists")
        cur.execute("CREATE TABLE artists(id INTEGER PRIMARY KEY, name TEXT);")

        cur.execute("INSERT INTO artists VALUES(1,'4 Non Blondes')")
        cur.execute("INSERT INTO artists VALUES(2,'Soundgarden')")
        cur.execute("INSERT INTO artists VALUES(3,'Pink Floyd')")
        cur.execute("INSERT INTO artists VALUES(4,'Led Zepplin')")

        cur.execute("DROP TABLE IF EXISTS albums")
        cur.execute("CREATE TABLE albums(id INTEGER PRIMARY KEY, name TEXT, artist TEXT);")

        cur.execute("INSERT INTO albums VALUES(1,'Whats Up?', '4 Non Blondes'")
        cur.execute("INSERT INTO albums VALUES(2,'Superunknown', 'Soundgarden')")
        cur.execute("INSERT INTO albums VALUES(3,'The Wall', 'Pink Floyd')")
        cur.execute("INSERT INTO albums VALUES(4,'Led Zepplin IV', 'Led Zepplin')")

        cur.execute("DROP TABLE IF EXISTS songs")
        cur.execute("CREATE TABLE songs(id INTEGER PRIMARY KEY, name TEXT, album TEXT, tracknum INTEGER, length INTEGER);")

        cur.execute("INSERT INTO albums VALUES(1,'Whats Up', 'Whats Up?', 1, 256)")
        cur.execute("INSERT INTO albums VALUES(2,'Superunknown', 'Black Hole Sun', 7, 318)")
        cur.execute("INSERT INTO albums VALUES(3,'The Wall', 'Hey You', 1, 280)")
        cur.execute("INSERT INTO albums VALUES(4,'Led Zepplin IV', 'Stairway to Heaven', 4, 482)")



def retrieve_data():
    try:
        con = lite.connect('music.db')

        cur = con.cursor()
        cur.execute('SELECT name, length from songs')
        data = cur.fetchall()

        for row in data:
            print(f"Song {row[0]} is {row[1]} seconds long.")
    except lite.Error as e:
        print(f"Error {e}:")

    finally:
        if con:
            con.close()


if __name__ == "__main__":
    insert_data()
    retrieve_data()