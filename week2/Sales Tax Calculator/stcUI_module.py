def get_input():
    print("\nENTER ITEMS (ENTER 0 TO END)")

    item_cost = -1
    total = 0.00

    while item_cost != 0:
        item_cost = float(input("Cost of item: "))

        total += item_cost
    
    return total

def display_total(total):
    print("Total: " + str(total))
    
def display_sales_tax(sales_tax):
    print("Sales tax: " + str(sales_tax))

def display_total_after_tax(total_after_tax):
    print("Total after tax: " + str(total_after_tax))