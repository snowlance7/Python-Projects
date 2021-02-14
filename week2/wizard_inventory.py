print("The Wizard Inventory program")
print("\nCOMMAND MENU")
print("show - Show all items")
print("grab - Grab an item")
print("edit - Edit an item")
print("drop - Drop an item")
print("exit - Exit program")

inventory = ["wooden staff","wizard hat","cloth shoes"]
max_inv = 4

def main():
    command = input("\nCommand: ")

    if command == "show":
        count = 1
        for x in inventory:
            print(str(count) + ". " + str(x))
            count += 1
    
    if command == "grab":
        if len(inventory) < max_inv:
            name = input("Name: ")
            inventory.append(name)
            print(name + " was added.")
        else:
            print("You can't carry any more items. Drop something first.")
    
    if command == "edit":
        try:
            number = int(input("Number: ")) - 1
            inventory[number] = input("Updated name: ")
            print("Item number " + str((number + 1)) + " was updated.")
        except:
            print("Error: Item does not exist.")
    
    if command == "drop":
        try:
            number = int(input("Number: "))
            print(inventory.pop(number - 1) + " was dropped.")
        except:
            print("Error: Item does not exist.")
    
    if command == "exit":
        print("Bye!")
        inventory.clear()
    else:
        main()
        
        

if __name__ == "__main__":
    main()