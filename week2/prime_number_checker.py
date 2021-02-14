print("Prime Number Checker")

def get_factors(num):
    factors = []
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    return factors

def get_input():
    num = int(input("\nPlease enter an integer between 1 and 5000: "))
    if num > 1 and num < 5000:
        return num
    else:
        raise Exception("Number wasnt between 1 and 5000.")

def main():
    number = get_input()
    factors = get_factors(number)

    if len(factors) == 2:
        print(str(number) + " is a prime number.")
    else:
        print(str(number) + " is NOT a prime number.")
        output = "It has " + str(len(factors)) + " factors:"
        for x in factors:
            output += " " + str(x)
        print(output)
    
    if input("\nTry again? (y/n): ").lower() == "y":
        main()
    else:
        print("\nBye!")


if __name__ == "__main__":
    main()