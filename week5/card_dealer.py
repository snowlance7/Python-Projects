import random

class Card():
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    @property
    def card_type(self):
        return self.rank + " of " + self.suit

class Deck():
    cards = []
    ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    suits = ["Clubs","Diamonds","Hearts","Spades"]

    def Shuffle(self):
        random.shuffle(self.cards)

    
    def Card_Count(self):
        return len(self.cards)

    def Deal(self):
        print(self.cards.pop(-1).card_type)





print("Card Dealer")
deck = Deck()
for suit in deck.suits:
    for rank in deck.ranks:
        deck.cards.append(Card(rank,suit))
deck.Shuffle()

print("\nI have shuffled a deck of 52 cards")
card_amt = int(input("\nHow many cards would you like?: "))
print("\nHere are your cards:")

i = 0
while i < card_amt:
    deck.Deal()
    i += 1

print("\nThere are",deck.Card_Count(),"cards left in the deck.")
print("\nGood luck!")

