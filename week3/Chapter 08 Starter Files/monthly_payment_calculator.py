def main():
    print("\nDATA ENTRY")
    
    loan_amount = float(input("Loan amount: "))
    formatted_yearly_interest_rate = round(float(input("Yearly interest rate: ")),1)
    years = int(input("Years: "))
    monthly_interest_rate = (formatted_yearly_interest_rate / 100) / 12
    months = years * 12
    monthly_payment = round((loan_amount * monthly_interest_rate / (1 - 1 / (1 + monthly_interest_rate) ** months)),2)

    print("\nFORMATTED RESULTS")
    print("Loan amount: $" + str(loan_amount))
    print("Yearly interest rate: " + str(formatted_yearly_interest_rate) + "%")
    print("Number of years:",str(years))
    print("Monthly payment: $" + str(monthly_payment))

    if input("\nContinue? (y/n): ").lower() == "y":
        main()
    else:
        print("\nBye!")

if __name__ == "__main__":
    print("Monthly Payment Calculator")
    main()