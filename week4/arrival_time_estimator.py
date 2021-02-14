import datetime
import math

def main():
    date_of_dep = input("\nEstimated date of departure (YYYY-MM-DD): ")
    time_of_dep = input("Estimated time of departure (HH:MM AM/PM): ")
    departure = datetime.datetime.strptime(date_of_dep + " " + time_of_dep,"%Y-%m-%d %I:%M %p")
    miles = int(input("Enter miles: "))
    mph = int(input("Enter miles per hour: "))
    
    hrs = math.floor(miles / mph)
    min = round(((miles / mph) - hrs) * 60)
    arrival = departure + datetime.timedelta(hours=hrs,minutes=min)
    
    print("\nEstimated travel time")
    print("Hours:",str(hrs))
    print("Minutes: ",str(min))
    print("Estimated date of arrival:",arrival.strftime("%Y-%m-%d"))
    print("Estimated time of arrival:",arrival.strftime("%I:%M %p"))

    if input("\nContinue? (y/n): ").lower() == "y":
        main()
    else:
        print("\nBye!")



if __name__ == "__main__":
    print("Arrival Time Estimator")
    main()