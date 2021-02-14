players = {
    "elizabeth": {
        "wins": 41,
        "losses": 3,
        "ties": 22
    },
    "john": {
        "wins": 32,
        "losses": 14,
        "ties": 17
    },
    "mike": {
        "wins": 8,
        "losses": 19,
        "ties": 11
    }
}

def main():
    name = input("\nEnter a player name: ").lower()

    print("Wins:",players[name]["wins"])
    print("Losses:",players[name]["losses"])
    print("Ties:",players[name]["ties"])

    if input("\nContinue? (y/n): ").lower() == "y":
        main()
    else:
        print("\nBye!")


if __name__ == "__main__":
    print("Game Stats program")
    print("\nALL PLAYERS:")
    player_list = list(players.keys())
    player_list.sort()
    for player in player_list:
        print(player.title())
    main()