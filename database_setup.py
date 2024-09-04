if __name__ != "__main__":
    print("This file is not meant to be imported!")
    exit(-1)

# Imports
import sqlite3

with open("SereneDB.sql", "r") as sql_file:
    script = sql_file.read()
conn = sqlite3.connect("Serene.db")
cur = conn.cursor()
cur.executescript(script)
conn.commit()
conn.close()
