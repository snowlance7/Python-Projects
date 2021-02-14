import database as db
from business import Player

def main():
    command = input("\nCommand: ")
    
    if command.lower() == "view":
        players = db.getPlayers()
        print("Name\t Wins\t Losses\t Ties\t Games")
        print("----------------------------------------")
        for p in players:
            print(p.name.title(),"\t",p.wins,"\t",p.losses,"\t",p.ties,"\t",p.games)
        main()
    elif command.lower() == "add":
        name = input("Name: ")
        wins = int(input("Wins: "))
        losses = int(input("Losses: "))
        ties = int(input("Ties: "))

        db.addPlayer(Player(name,wins,losses,ties))

        print(name.title(),"was added to database.")
        main()
    elif command.lower() == "del":
        name = input("Name: ").lower()
        db.delPlayer(name)

        print(name.title(),"was deleted from database.")
        main()
    elif command.lower() == "exit":
        print("\nBye!")
    else:
        main()

if __name__ == "__main__":
    print("Player Manager")
    print("\nCOMMAND MENU")
    print("view - View players")
    print("add - Add a player")
    print("del - Delete a player")
    print("exit - Exit program")
    main()