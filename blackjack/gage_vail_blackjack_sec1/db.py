def getMoney():
    with open("money.txt") as f:
            return float(f.read())

def saveMoney(money):
    with open("money.txt","w") as f:
        f.write(str(money))
        
    
        