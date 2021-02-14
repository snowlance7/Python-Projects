import random

class Card():
    def __init__(self,rank,suit,points):
        self.rank = rank
        self.suit = suit
        self.points = points

    @property
    def __string__(self):
        return self.rank + " of " + self.suit

class Deck():

    def __init__(self):
        self.cards = []
        self.ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        self.suits = ["Clubs","Diamonds","Hearts","Spades"]
    
    @property
    def cardCount(self):
        return len(self.cards)

    def Build(self):
        self.cards.clear()
        for suit in self.suits:
            for rank in self.ranks:
                if rank == "Ace":
                    p = 1
                elif rank == "Jack" or rank == "Queen" or rank == "King":
                    p = 10
                else:
                    p = int(rank)
                self.cards.append(Card(rank,suit,p))
        random.shuffle(self.cards)

    def Deal(self):
        return self.cards.pop()

class Hand(list):
    def __init__(self):
        self = []

    @property
    def points(self):
        p = 0
        for card in self:
            p += card.points
        return p
            
    def ShowCards(self):
        for card in self:
            print(card.__string__)

    def Draw(self,deck):
        self.append(deck.Deal())