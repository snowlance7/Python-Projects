import db
import sys
import random
import locale
import datetime

locale.setlocale( locale.LC_ALL, '' )

ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
suits = ["Clubs","Diamonds","Hearts","Spades"]
deck = []
money = 0
bet = float()
playerHand = []
dealerHand = []
startTime = datetime.datetime.now()

def BuildDeck():
    deck.clear()
    for suit in suits:
        for rank in ranks:
            points = 0

            if rank == "Ace":
                points = 1
            elif rank == "Jack" or rank == "Queen" or rank == "King":
                points = 10
            else:
                points = int(rank)
            card = {
                "rank": rank,
                "suit": suit,
                "points": points
            }
            deck.append(card)
    random.shuffle(deck)
    return deck

def buyMoney():
    try:
        return float(input("How many chips?: "))

    except:
        print("Please input a valid amount.")
        buyMoney()

def getBet(money):
    try:
        bet = float(input("Bet amount: "))
        if bet <= money:
            if bet >= 5 and bet <= 1000:
                return bet
            else: 
                print("Minimum bet is 5 and maximum bet is 1000")
                getBet(money)
        else:
            print("You dont have that much money.")
            getBet(money)
    except:
        print("Please input a valid amount.")
        getBet(money)

    

def getPoints(hand):
    points = 0
    for card in hand:
        points += card["points"]
    return points

def ShowCard(card):
    print(card["rank"],"of",card["suit"])

def ShowCards(hand):
    for card in hand:
        ShowCard(card)

def ShowResults():
    print("\nDEALERS CARDS:")
    ShowCards(dealerHand)
    print("\nYOUR POINTS:",str(getPoints(playerHand)))
    print("DEALER'S POINTS:",str(getPoints(dealerHand)))

def HitOrStand():
    choice = input("\nHit or stand (hit/stand): ").lower()

    if choice == "hit":
        playerHand.append(deck.pop())
        print("\nYOUR CARDS:")
        ShowCards(playerHand)

        if getPoints(playerHand) == 21:
            ShowResults()
            
            print("\nYou scored 21 points. You win!")
            return True
        elif getPoints(playerHand) > 21:
            ShowResults()
            print("\nYou busted. You lose...")
            return False
        else:
            return HitOrStand()
    
    elif choice == "stand":

        ShowResults()

        if getPoints(dealerHand) > 21:
            print("\nYay! The dealer busted. You win!")
            return True
        elif getPoints(dealerHand) < getPoints(playerHand):
            print("\nYou have more points than the dealer. You win!")
            return True
        elif getPoints(dealerHand) == getPoints(playerHand):
            print("\nYou and the dealer tied! You both win!")
            return True
        else:
            print("\nThe dealer has more points than you. You lose...")
            return False
    else:
        return HitOrStand()

def main():

    try: 
        money = db.getMoney()
    except: 
        money = 0

    if money < 5:
        if input("You don't have enough money to place a bet. Would you like to buy more chips? (y/n): ").lower() == "y":
            money += buyMoney()
            db.saveMoney(money)
        else:
            sys.exit()
    
    print("\nMoney:",str(locale.currency(money)))
    bet = getBet(money)
    money -= bet
    db.saveMoney(money)


    dealerHand.clear()
    playerHand.clear()
    deck = BuildDeck()

    while getPoints(dealerHand) < 17:
            dealerHand.append(deck.pop())

    playerHand.append(deck.pop())
    playerHand.append(deck.pop())

    print("\nDEALER'S SHOW CARD:")
    ShowCard(dealerHand[0])
    
    print("\nYOUR CARDS")
    ShowCards(playerHand)
    
    if HitOrStand():
        money += bet * 1.5

    print("Money:",str(locale.currency(money)))
    db.saveMoney(money)
    

    if input("\nPlay again? (y/n): ").lower() == "y":
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
    print("Blackjack payout is 3:2")
    print("Start time:",startTime.strftime("%I:%M:%S %p"))
    main()    