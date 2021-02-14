import random

def calculateGuess(min, max, guess_count, num):
    guess = random.randint(min,max)
    guess_count += 1
    print("Guess",str(guess_count),"is",str(guess))

    if guess == num:
        if guess_count == 1:
            print("The computer found it in 1 guess!")
        else:
            print("The computer found it in " + str(guess_count) + " guesses.")
    elif num < guess:
        calculateGuess(min,guess,guess_count,num)
    elif num > guess:
        calculateGuess(guess,max,guess_count,num)

def main():
    num = input("\nEnter a number between 0 and 100: ")
    
    if num.lower() != "x":
        calculateGuess(0,100,0,int(num))
        main()
    else:
        print("Bye!")
        

if __name__ == "__main__":
    print("Number Finder")
    print("\nEnter 'x' to exit.")

    main()