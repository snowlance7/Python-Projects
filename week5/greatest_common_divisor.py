def main():
    x = int(input("\nNumber 1: "))
    y = int(input("Number 2: "))
    gcd = y
    remainder = x % y
    
    if x > y:
        while remainder != 0:
            gcd -= 1
            remainder = (x % gcd) + (y % gcd)
        print("Greatest common divisor:",str(gcd))
    else:
        print("Number 1 must be greater than number 2. Please try again.")
        main()
    
    if input("\nContinue? (y/n): ").lower() == "y":
        main()
    else:
        print("\nBye!")
        


if __name__ == "__main__":
    print("Greatest Common Divisor")
    main()