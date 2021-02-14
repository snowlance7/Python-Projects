import random

class Player():
    def __init__(self,name):
        self.name = name
    
    roshambo = str()
    wins = int()
    losses = int()

class Bart(Player):
    def generateRoshambo(self):
        self.roshambo = "rock"

class Lisa(Player):
    def generateRoshambo(self):
        self.roshambo = random.choice(["rock","paper","scissors"])

def main(player,opponent):
    choice = input("\nRock, paper, or scissors? (r/p/s): ").lower()

    if choice == "r" or choice == "p" or choice == "s":
        if choice == "r":
            player.roshambo = "rock"
        elif choice == "p":
            player.roshambo = "paper"
        else:
            player.roshambo = "scissors"
        
        opponent.generateRoshambo()

        print("\n" + player.name + ":",player.roshambo)
        print(opponent.name + ":",opponent.roshambo)

        if player.roshambo == opponent.roshambo:
            print("Draw!")
        elif player.roshambo == "rock":
            if opponent.roshambo == "scissors":
                print(player.name,"wins!")
                player.wins += 1
            else:
                print(opponent.name,"wins!")
                player.losses += 1
        elif player.roshambo == "paper":
            if opponent.roshambo == "rock":
                print(player.name,"wins!")
                player.wins += 1
            else:
                print(opponent.name,"wins!")
                player.losses += 1
        else:
            if opponent.roshambo == "paper":
                print(player.name,"wins!")
                player.wins += 1
            else:
                print(opponent.name,"wins!")
                player.losses += 1


    if input("\nPlay again? (y/n): ").lower() == "y":
        main(player,opponent)
    else:
        print("\nWins:",str(player.wins))
        print("Losses:",str(player.losses))
        print("\nThanks for playing!")
        


if __name__ == "__main__":
    print("Roshambo Game")
    player = Player(input("\nEnter your name: "))
    choice = input("\nWould you like to play Bart or Lisa? (b/l): ").lower()

    if choice == "b":
        opponent = Bart("Bart")
    elif choice == "l":
        opponent = Lisa("Lisa")

    main(player,opponent)