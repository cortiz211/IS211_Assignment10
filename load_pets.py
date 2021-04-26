import sqlite3 as lite


def pet_data():
    con = lite.connect('pets.db')

    with con:
        cur = con.cursor()

        cur.execute("INSERT INTO person VALUES(1,'James', 'Smith', 41)")
        cur.execute("INSERT INTO person VALUES(2,'Diana', 'Greene', 23)")
        cur.execute("INSERT INTO person VALUES(3,'Sara', 'White', 27)")
        cur.execute("INSERT INTO person VALUES(4,'William', 'Gibson', 23)")

        cur.execute("INSERT INTO pet VALUES(1,'Rusty', 'Dalmation', 4, 1)")
        cur.execute("INSERT INTO pet VALUES(2,'Bella', 'Alaskan Malamute', 3, 0)")
        cur.execute("INSERT INTO pet VALUES(3,'Max', 'Cocker Spaniel', 1, 0)")
        cur.execute("INSERT INTO pet VALUES(4,'Rocky', 'Beagle', 7, 0)")
        cur.execute("INSERT INTO pet VALUES(5,'Rufus', 'Cocker Spaniel', 1, 0)")
        cur.execute("INSERT INTO pet VALUES(6,'Spot', 'Bloodhound', 2, 1)")

        cur.execute("INSERT INTO person_pet VALUES(1, 1)")
        cur.execute("INSERT INTO person_pet VALUES(1, 2)")
        cur.execute("INSERT INTO person_pet VALUES(2, 3)")
        cur.execute("INSERT INTO person_pet VALUES(2, 4)")
        cur.execute("INSERT INTO person_pet VALUES(3, 5)")
        cur.execute("INSERT INTO person_pet VALUES(4, 6)")

