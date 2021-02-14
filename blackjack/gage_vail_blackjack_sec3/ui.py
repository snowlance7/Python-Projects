from objects import Card, Deck, Hand
import db
import sys
import locale
import blackjack

locale.setlocale( locale.LC_ALL, '' )

deck = Deck()
dealer = Hand()
player = Hand()

def Start():
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

    deck.Build()
    dealer.clear()
    player.clear()

    dealer.Draw(deck)
    player.Draw(deck)
    dealer.Draw(deck)
    player.Draw(deck)

    print("\nDEALER'S SHOW CARD:")
    print(dealer[0].__string__)
    print("\nYOUR CARDS:")
    player.ShowCards()
    
    if HitOrStand():
        money += bet * 1.5

    print("Money:",str(locale.currency(money)))
    db.saveMoney(money)

def ShowResults():
    print("\nDEALERS CARDS:")
    dealer.ShowCards()
    print("\nYOUR POINTS:",str(player.points))
    print("DEALER'S POINTS:",str(dealer.points))

def HitOrStand():
    choice = input("\nHit or stand (hit/stand): ").lower()

    if choice == "hit":
        player.Draw(deck)
        print("\nYOUR CARDS:")
        player.ShowCards()

        if player.points == 21:
            ShowResults()
            
            print("\nYou scored 21 points. You win!")
            return True
        elif player.points > 21:
            ShowResults()
            print("\nYou busted. You lose...")
            return False
        else:
            return HitOrStand()
    
    elif choice == "stand":
        while dealer.points < 17:
            dealer.Draw(deck)

        ShowResults()

        if dealer.points > 21:
            print("\nYay! The dealer busted. You win!")
            return True
        elif dealer.points < player.points:
            print("\nYou have more points than the dealer. You win!")
            return True
        elif dealer.points == player.points:
            print("\nYou and the dealer tied! You both win!")
            return True
        else:
            print("\nThe dealer has more points than you. You lose...")
            return False
    else:
        return HitOrStand()

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

if __name__ == "__main__":
    blackjack.main()