import ui
import datetime

startTime = datetime.datetime.now()

def main():
    ui.Start()

    if input("Play again? (y/n): ").lower() == "y":
        main()
    else:
        endTime = datetime.datetime.now()
        elapsedTime = str(endTime - startTime).split('.',2)[0]
        print("Stop time:",endTime.strftime("%I:%M:%S %p"))
        print(elapsedTime)
        print("Come back soon!")
        print("Bye!")

if __name__ == "__main__":
    print("Blackjack")
    main()    