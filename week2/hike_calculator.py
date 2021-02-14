print("Hike Calculator\n")

def calc_feet(m):
    feet = round(m * 1520)
    return feet

def main():
    miles = float(input("How many miles did you walk?: "))

    print("You walked " + str(calc_feet(miles)) + " feet.")

if __name__ == "__main__":
    main()