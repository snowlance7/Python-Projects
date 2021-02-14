import datetime
import math


def calculate_next_bday(birthdate,now):
    delta1 = datetime.datetime(now.year, birthdate.month, birthdate.day)
    delta2 = datetime.datetime(now.year+1, birthdate.month, birthdate.day)
    
    return (delta1 if delta1 > now else delta2)

def main():
    name = input("\nEnter name: ").title()
    birthday = datetime.datetime.strptime(input("Enter birthday (MM/DD/YY): "),"%m/%d/%y")
    next_bday = calculate_next_bday(birthday,datetime.datetime.now())
    days_till_bday = (next_bday - datetime.datetime.now()).days
    age_in_days = (datetime.datetime.now() - birthday).days
    age = math.floor((datetime.datetime.now() - birthday).days / 365)
#Birthdate and todays date
    print("Birthday: " + birthday.strftime("%A") + ", " + birthday.strftime("%B") + " " + birthday.strftime("%d") + ", " + birthday.strftime("%Y"))
    print("Today: " + datetime.datetime.now().strftime("%A") + ", " + datetime.datetime.now().strftime("%B") + " " + datetime.datetime.now().strftime("%d") + ", " + datetime.datetime.now().strftime("%Y"))

#Age
    if age > 2:
        print(name,"is",str(age),"years old.")
    else:
        print(name,"is",str(age_in_days),"days old.")

# Birthday is ____
    if datetime.datetime.now().day == next_bday.day:  #Birthday is today
        print(name.title() + "'s birthday is today!")
    elif next_bday.day == (datetime.datetime.now() + datetime.timedelta(days=1)).day: #Birthday is tommorrow
        print(name.title() + "'s birthday is tommorrow!")
    elif next_bday.day == (datetime.datetime.now() + datetime.timedelta(days=-1)).day: #Birthday is yesterday
        print(name.title() + "'s birthday was yesterday!")
    else: #any other day
        print(name + "'s birthday is in " + str(days_till_bday) + " days.")

    if input("\nContinue? (y/n): ").lower() == "y":
        main()

if __name__ == "__main__":
    print("Birthday Calculator")
    main()