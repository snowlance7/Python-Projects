def main():
    loan_amount = round(float(input("\nEnter loan amount: ")),2)
    interest_rate = round(float(input("Enter interest rate: ")),3)
    interest_amount = round(loan_amount * (interest_rate / 100),2)

    print("\nLoan amount: $" + str(loan_amount))
    print("Interest rate: " + str(interest_rate) + "%")
    print("Interest amount: $" + str(interest_amount))

    if input("Continue (y/n): ").lower() == "y":
        main()
    else:
        print("\nBye!")

if __name__ == "__main__":
    print("Interest Calculator")
    main()