import sqlite3 as lite

def data_connect():
    con = lite.connect('pets.db')

    with con:
        cur = con.cursor()
        cur.execute("SELECT first_name FROM person")
        cur.execute("SELECT name, breed, age FROM pet")

        #I got stuck here trying to figure out how to pull the data. I'm assuming it's meant to be an JOIN.

if __name__ == "__main__":

    req = []
    while req > 0:
        req = input("Please choose an ID 1-4, choose -1 to stop.")
        print(f"{} owned {}, a {}, that was {} years old".format(row['first_name'], row["name"], row["breed"], row["age"]))