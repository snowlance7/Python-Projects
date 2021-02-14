import sqlite3

dbPath = "database.sqlite"
with open("script.sql") as f1:
    with sqlite3.connect(dbPath) as conn:
        c = conn.cursor()

        c.executescript(f1.read())
        conn.commit()
        c.close()
