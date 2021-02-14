print("The Quarterly Sales program")

def main():
    sales = []
    total = 0
    
    for i in range(4):
        sale = round(float(input("Enter sales for Q" + str(i+1) + ": ")),2)
        sales.append(sale)
        total += sale
    
    average = round(total / len(sales),2)
    sales.sort()
    print("\nTotal: " + str(total))
    print("Average Quarter: " + str(average))
    print("Lowest Quarter: " + str(sales[0]))
    print("Highest Quarter: " + str(sales[-1]))
    

        

if __name__ == "__main__":
    main()