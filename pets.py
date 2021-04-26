import sqlite3 as lite


def pet_data():
    con = lite.connect('pets.db')

    with con:
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS person")
        cur.execute("CREATE TABLE person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)")

        cur.execute("DROP TABLE IF EXISTS pet")
        cur.execute("CREATE TABLE pet(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)")

        cur.execute("DROP TABLE IF EXISTS person_pet")
        cur.execute("CREATE TABLE person(person_id INTEGER, pet_id INTEGER)")