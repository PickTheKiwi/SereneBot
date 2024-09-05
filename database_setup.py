# Imports
import sqlite3
import os
from pathlib import Path


def setup():
    with open("SereneDB.sql") as sql_file:
        script = sql_file.read()
    conn = sqlite3.connect("Serene.db")
    cur = conn.cursor()
    cur.executescript(script)
    conn.commit()
    conn.close()


def reset():
    os.remove("Serene.db")
    setup()


database = Path("Serene.db")
if database.is_file():
    reset()
else:
    setup()
