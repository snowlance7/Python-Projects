filepath = "monthly_sales.csv"
monthly_sales = list()

def main():
    monthly_sales.clear()
    with open(filepath) as f1:
        for line in f1:
            row = line.split(",")
            monthly_sales.append(row)

    command = input("\nCommand: ")

    if command == "monthly":
        for sale in monthly_sales:
            print(sale[0],"-",sale[1][:-1])
    
    if command == "yearly":
        yearly_total = 0

        for sale in monthly_sales:
            yearly_total += int(sale[1])
        
        monthly_average = round(yearly_total / 12,2)
        print("Yearly total: " + str(yearly_total))
        print("Monthly average: " + str(monthly_average))
    
    if command == "edit":
        
        try:
            month = input("Three-letter Month: ")
            if len(month) != 3:
                raise Exception
            cont = False
            for sale in monthly_sales:
                if sale[0].lower() == month.lower():
                    sales_amount = str(round(float(input("Sales Amount: "))))
                    sale[1] = sales_amount + "\n"
                    cont = True
                
            
            if not cont:
                raise ValueError
            
            
            with open(filepath,"w") as f1:
                for sale in monthly_sales:
                    f1.write(sale[0] + "," + sale[1])

            print("Sales amount for " + month + " was modified.")
                
        except ValueError:
            print("Not a valid 3 letter month.")
        except TypeError:
            print("Not a valid sales amount.")
    
    if command == "exit":       #exit
        print("Bye!")
    else:
        main()


if __name__ == "__main__":
    print("Monthly Sales program")
    print("\nCOMMAND MENU")
    print("monthly - View monthly sales")
    print("yearly - View yearly summary")
    print("edit - Edit sales for a month")
    print("exit - Exit program")

    main()