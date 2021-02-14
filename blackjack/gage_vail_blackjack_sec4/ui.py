from objects import Card, Deck, Hand, Session
import locale
import sys
import tkinter as tk
from tkinter import ttk
import datetime

# Window Construction
root = tk.Tk()
root.title("Blackjack")
root.geometry("400x300")
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

#text variables
moneyOutput = tk.StringVar()
betInput = tk.StringVar()
DealerCardsOutput = tk.StringVar()
DealerPointsOutput = tk.StringVar()
PlayerCardsOutput = tk.StringVar()
PlayerPointsOutput = tk.StringVar()
RESULT = tk.StringVar()



locale.setlocale( locale.LC_ALL, '' )

deck = Deck()
dealer = Hand()
player = Hand()
session = Session()
active = False
bet = float()

def Startup():
    global session
    session.startTime = datetime.datetime.now()

    try: 
        session.GetMoney()
    except: 
        session.startMoney = 0

    if session.startMoney < 5:
        if input("You don't have enough money to place a bet. Would you like to buy more chips? (y/n): ").lower() == "y":
            session.startMoney += buyMoney()
        else:
            sys.exit()
    
    session.stopMoney = session.startMoney
    moneyOutput.set(str(locale.currency(session.stopMoney)))

def Play():
    global active
    global session
    global player
    global dealer
    global deck
    global bet

    PlayerCardsOutput.set("")
    DealerPointsOutput.set("")
    PlayerCardsOutput.set("")
    PlayerPointsOutput.set("")
    RESULT.set("")

    active = True
    bet = getBet()
    

    if RESULT.get() == "":
        session.stopMoney -= bet
        moneyOutput.set(str(locale.currency(session.stopMoney)))

        deck.Build()
        dealer.clear()
        player.clear()

        dealer.Draw(deck)
        player.Draw(deck)
        dealer.Draw(deck)
        player.Draw(deck)

        #show dealers show card and points
        DealerCardsOutput.set(dealer[0].rank)
        DealerPointsOutput.set(dealer[0].points)
        
        #show players cards and points
        PlayerCardsOutput.set("")
        output = ""
        for card in player:
            output += card.rank + " "
        
        PlayerCardsOutput.set(output)
        PlayerPointsOutput.set(str(player.points))
        
        # if HitOrStand():
        #     money += bet * 1.5

        # print("Money:",str(locale.currency(money)))
        # db.saveMoney(money)

def Hit():

    global active
    global bet
    global session
    global player
    global dealer
    global deck

    if active:

        player.Draw(deck)
        #show players cards and points
        output = ""
        for card in player:
            output += card.rank + " "
        
        PlayerCardsOutput.set(output)
        PlayerPointsOutput.set(str(player.points))

        if player.points == 21:
            ShowResults()
            RESULT.set("You scored 21 points. You win!")
            session.stopMoney += bet * 1.5
            session.addedMoney += bet * 1.5
            moneyOutput.set(session.stopMoney)
            active = False
        elif player.points > 21:
            ShowResults()
            RESULT.set("You busted. You lose...")
            active = False
    

def Stand():
    global active

    if active:
        global player
        global bet
        global dealer
        global deck
        global session

        while dealer.points < 17:
            dealer.Draw(deck)

        ShowResults()

        if dealer.points > 21:
            RESULT.set("Yay! The dealer busted. You win!")
            session.stopMoney += bet * 1.5
            session.addedMoney += bet * 1.5
            moneyOutput.set(session.stopMoney)
            active = False
        elif dealer.points < player.points:
            RESULT.set("You have more points than the dealer. You win!")
            session.stopMoney += bet * 1.5
            session.addedMoney += bet * 1.5
            moneyOutput.set(session.stopMoney)
            active = False
        elif dealer.points == player.points:
            RESULT.set("You and the dealer tied! You both win!")
            session.stopMoney += bet * 1.5
            session.addedMoney += bet * 1.5
            moneyOutput.set(session.stopMoney)
            active = False
        else:
            RESULT.set("The dealer has more points than you, you lose...")
            active = False
    

def ShowResults():
    #show dealers cards and points
    output = ""
    for card in dealer:
        output += card.rank + " "

    DealerCardsOutput.set(output)
    DealerPointsOutput.set(str(dealer.points))
    
    #show players cards and points
    output = ""
    for card in player:
        output += card.rank + " "
    
    PlayerCardsOutput.set(output)
    PlayerPointsOutput.set(str(player.points))

def buyMoney():
    try:
        return float(input("How many chips?: "))

    except:
        print("Please input a valid amount.")
        buyMoney()

def getBet():
    global session

    try:
        bet = int(betInput.get())
        if bet <= session.stopMoney:
            if bet >= 5 and bet <= 1000:
                return bet
            else: 
                RESULT.set("Minimum bet is 5 and maximum bet is 1000")
        else:
            RESULT.set("You dont have that much money to bet.")
    except:
        RESULT.set("Please input a valid bet amount.")

def Exit():
    session.stopTime = datetime.datetime.now()
    session.SaveSession()

    root.destroy()

#labels
lblMoney = ttk.Label(frame,text="Money:").grid(column=0,row=0,sticky=tk.E)
lblBet = ttk.Label(frame,text="Bet:").grid(column=0,row=1,sticky=tk.E)
lblDEALER = ttk.Label(frame,text="DEALER").grid(column=0,row=2)
lblCards = ttk.Label(frame,text="Cards:").grid(column=0,row=3,sticky=tk.E)
lblPoints = ttk.Label(frame,text="Points:").grid(column=0,row=4,sticky=tk.E)
lblYOU = ttk.Label(frame,text="YOU").grid(column=0,row=5)
lblCards = ttk.Label(frame,text="Cards:").grid(column=0,row=6,sticky=tk.E)
lblPoints = ttk.Label(frame,text="Points:").grid(column=0,row=7,sticky=tk.E)
lblBlank1 = ttk.Label(frame,text="").grid(column=0,row=8)
lblRESULT = ttk.Label(frame,text="RESULT:").grid(column=0,row=9,sticky=tk.E)
lblBlank2 = ttk.Label(frame,text="").grid(column=0,row=10)

#entries/Output
lblMoneyOutput = ttk.Label(frame,textvariable=moneyOutput,width=25,borderwidth=2,relief="groove").grid(column=1,row=0,sticky=tk.W,columnspan=2)
txtBet = ttk.Entry(frame,textvariable=betInput,width=25).grid(column=1,row=1,sticky=tk.W,columnspan=2)
lblDealerCardsOutput = ttk.Label(frame,textvariable=DealerCardsOutput,width=50,borderwidth=2,relief="groove").grid(column=1,row=3,sticky=tk.W,columnspan=4)
lblDealerPointsOutput = ttk.Label(frame,textvariable=DealerPointsOutput,width=25,borderwidth=2,relief="groove").grid(column=1,row=4,sticky=tk.W,columnspan=2)
lblPlayerCardsOutput = ttk.Label(frame,textvariable=PlayerCardsOutput,width=50,borderwidth=2,relief="groove").grid(column=1,row=6,sticky=tk.W,columnspan=4)
lblPlayerPointsOutput = ttk.Label(frame,textvariable=PlayerPointsOutput,width=25,borderwidth=2,relief="groove").grid(column=1,row=7,sticky=tk.W,columnspan=2)
lblRESULT = ttk.Label(frame,textvariable=RESULT,width=50,borderwidth=2,relief="groove").grid(column=1,row=9,sticky=tk.W,columnspan=4)

btnHit = ttk.Button(frame, text="Hit",command=Hit).grid(column=1,row=8,sticky=tk.W)
btnStand = ttk.Button(frame, text="Stand",command=Stand).grid(column=2,row=8,sticky=tk.W) #cant get these closer to each other, find out later if i have time
btnPlay = ttk.Button(frame, text="Play",command=Play).grid(column=1,row=10,sticky=tk.W)
btnExit = ttk.Button(frame, text="Exit",command=Exit).grid(column=2,row=10,sticky=tk.W)


for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3) 


Startup()
root.mainloop()