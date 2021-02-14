import sqlite3

conn = sqlite3.connect("customers.sqlite")
c = conn.cursor()

#c.execute("DROP TABLE IF EXISTS Customer;")
#c.execute("CREATE TABLE Customer(customerID  INTEGER PRIMARY KEY     NOT NULL,firstName   TEXT                    NOT NULL,lastName    TEXT                    NOT NULL,companyName TEXT                    NULL,address     TEXT                    NULL,city        TEXT                    NULL,state       TEXT                    NULL,zip         TEXT                    NULL);")
with open("customers.sql") as f:
    c.executescript(f.read())
    conn.commit()

with open("customers.csv") as f1:
    for line in f1:
        values = line.split(",")
        c.execute("INSERT INTO Customer (firstName, lastName, companyName, address, city, state, zip) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (values[0], values[1], values[2], values[3], values[4], values[5], values[6]))
        conn.commit()

conn.close()

print("Done!")