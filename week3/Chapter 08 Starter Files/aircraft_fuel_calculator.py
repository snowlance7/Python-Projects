import math

def main():
    miles = int(input("\nDistance in nautical miles: "))

    time = miles / 120
    gallons = math.ceil((((miles / 120) + 0.5) * 8.4) * 10) / 10
    hours = math.floor(time)
    minutes = round(((miles % 120) / 120)*60) 


    print("Flight time:",str(hours),"hour(s) and",str(minutes),"minute(s)")
    print("Required fuel:",str(gallons),"gallons")

    if input("\nContinue? (y/n): ").lower() == "y":
        main()
    else:
        print("\nBye!")
    



if __name__ == "__main__":
    print("Aircraft Fuel Calculator")
    main()