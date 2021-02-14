print("Even or Odd Checker\n")

def main():
    num = int(input("Enter an integer: "))
    print("This is an " + str(calc(num)) + " number.")

def calc(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == "__main__":
    main()