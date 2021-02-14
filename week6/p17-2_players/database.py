import sqlite3
from business import Player
import csv

db_path = "player_db.sqlite"
# with sqlite3.connect(db_path) as conn:
#     c = conn.cursor()
#     with open("player_db.sql") as f:
#         c.executescript(f.read())
#         conn.commit()
#     c.close()

def getPlayers():
    players = []

    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        for row in c.execute("SELECT name,wins,losses,ties FROM Player"):
            players.append(Player(row[0],row[1],row[2],row[3]))
    
    return players

def addPlayer(player):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO Player (name,wins,losses,ties) VALUES (?,?,?,?)",
        (player.name, player.wins, player.losses, player.ties))
        conn.commit()
        c.close()
        

def delPlayer(name):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM Player WHERE name = '" + name + "'")
        conn.commit()
        c.close()