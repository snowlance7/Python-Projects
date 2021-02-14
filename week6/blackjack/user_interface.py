from business import Card, Deck, Player

deck = Deck()
dealer = Player()
player = Player()

def Start():
    deck.Build()
    deck.Shuffle()
    dealer.hand.clear()
    player.hand.clear()

    dealer.Draw(deck)
    player.Draw(deck)
    dealer.Draw(deck)
    player.Draw(deck)

    print("\nDEALER'S SHOW CARD:")
    print(dealer.hand[0].card_type)
    print("\nYOUR CARDS:")
    player.ShowCards()

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
        elif player.points > 21:
            ShowResults()
            print("\nYou busted. You lose...")
        else:
            HitOrStand()
    
    elif choice == "stand":
        if dealer.points < 17:
            dealer.Draw(deck)

        ShowResults()

        if dealer.points > 21:
            print("\nYay! The dealer busted. You win!")
        elif dealer.points < player.points:
            print("\nYou have more points than the dealer. You win!")
        elif dealer.points == player.points:
            print("\nYou and the dealer tied! You both win!")
        else:
            print("\nThe dealer has more points than you. You lose...")
    else:
        HitOrStand()