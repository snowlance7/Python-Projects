import sqlite3
from business import Task

db_path = "task_list_db.sqlite"

# with sqlite3.connect(db_path) as conn:
#     c = conn.cursor()
#     with open("task_list_db.sql") as sql:
#         c.executescript(sql)
#         conn.commit()
#         c.close()


def getTasks():
    with sqlite3.connect(db_path) as conn:
        tasks = []
        c = conn.cursor()
        for row in c.execute("SELECT taskID,description FROM Task WHERE completed = 0"):
            task = Task(row[1])
            task.taskID = row[0]
            tasks.append(task)
        c.close()
        return tasks


def getHistory():
    with sqlite3.connect(db_path) as conn:
        tasks = []
        c = conn.cursor()
        for row in c.execute("SELECT taskID,description FROM Task WHERE completed = 1"):
            task = Task(row[1])
            task.taskID = row[0]
            tasks.append(task)
        c.close()
        return tasks

def addTask(description):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO Task (description,completed) VALUES (?,?)",
        (description,0))
        conn.commit()
        c.close()

def completeTask(num):
    index = num - 1
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        tasks = getTasks()
        c.execute("UPDATE Task SET completed = 1 WHERE taskID = " + str(tasks[index].taskID))
        conn.commit()
        c.close()

def delTask(num):
    index = num - 1
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        tasks = getHistory()
        c.execute("DELETE FROM Task WHERE taskID = " + str(tasks[index].taskID))
        conn.commit()
        c.close()