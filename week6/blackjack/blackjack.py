import user_interface as ui

def main():
    ui.Start()
    ui.HitOrStand()

    if input("Play again? (y/n): ").lower() == "y":
        main()
    else:
        print("Come back soon!")

if __name__ == "__main__":
    print("Blackjack")
    main()    