import datetime

def main():
    monthly_invest = float(input("\nEnter monthly investment: "))
    yearly_interest = float(input("Enter yearly interest rate: "))
    yrs = int(input("Enter number of years: "))
    
    months = yrs * 12
    monthly_interest = yearly_interest / 12 / 100

    future_value = round(monthly_invest*((1+monthly_interest)**months-1) / monthly_interest,2)
    print("Future value:",str("{:,}".format(future_value)))

    with open("FVL_log.txt","a") as f:
        log = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - " + str(monthly_invest) + "|" + str(yearly_interest) + "|" + str(yrs) + "|" + str(future_value) + "\n"
        f.write(log)
    
    if input("\nContinue? (y/n): ").lower() == "y":
        main()
    else:
        print("\nBye!")



if __name__ == "__main__":
    print("Future Value Calculator")
    main()