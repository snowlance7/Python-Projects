import sqlite3
# from objects import Session

dbPath = "database.sqlite"

def getMoney():
    with sqlite3.connect(dbPath) as conn:
        c = conn.cursor()
        result = c.execute("SELECT stopMoney FROM Session WHERE sessionID = ( SELECT MAX(sessionID) FROM Session )")
        
        return result.fetchone()[0]
        #SELECT * FROM Session WHERE sessionID = ( SELECT MAX(sessionID) FROM Session )
        

def saveSession(session):
    with sqlite3.connect(dbPath) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO Session (startTime,startMoney,addedMoney,stopTime,stopMoney) VALUES (?,?,?,?,?)",
        (session.startTime,session.startMoney,session.addedMoney,session.stopTime,session.stopMoney))
        conn.commit()
        c.close()


# #c.execute("INSERT INTO Task (description,completed) VALUES (?,?)",
#         (description,0))
#         conn.commit()
#         c.close()