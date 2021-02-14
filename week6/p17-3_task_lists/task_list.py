import database as db
from business import Task

def main():
    command = input("\nCommand: ")

    if command.lower() == "view":
        tasks = db.getTasks()
        cnt = 0
        for task in tasks:
            print(str(cnt+1) + ". " + task.description)
            cnt += 1
        main()
    elif command.lower() == "history":
        tasks = db.getHistory()
        cnt = 0
        for task in tasks:
            print(str(cnt+1) + ". " + task.description + "(DONE!)")
            cnt += 1
        main()
    elif command.lower() == "add":
        description = input("Description: ")
        db.addTask(description)
        main()
    elif command.lower() == "complete":
        number = int(input("Number: "))
        db.completeTask(number)
        main()
    elif command.lower() == "delete":
        number = int(input("Number: "))
        db.delTask(number)
        main()
    elif command.lower() == "exit":
        print("\nBye!")
    else:
        main()
        

if __name__ == "__main__":
    print("Task List")
    print("\nCOMMAND MENU")
    print("view - View pending tasks")
    print("history - View completed tasks")
    print("add - Add a task")
    print("complete - Complete a task")
    print("delete - Delete a task")
    print("exit - Exit program")
    main()
    