print("Contact Manager")
print("\nCOMMAND MENU")
print("list - Display all contacts")
print("view - View a contact")
print("add - Add a contact")
print("del - Delete a contact")
print("exit - Exit program")

contacts = [["Guido van Rossum","guido@gmail.com","262-158-4568"],["Eric Idle","eric@ericidle.com","+44 20 7946 0958"]]

def main():
    command = input("\nCommand: ")

    if command == "list":
        cnt = 1

        for c in contacts:
            print(str(cnt) + ". " + c[0])
            cnt += 1
    
    if command == "view":
        try:
            num = int(input("Number: "))
            c = contacts[num-1]
            
            print("Name: " + c[0])
            print("Email: " + c[1])
            print("Phone: " + c[2])
        except:
            print("Contact does not exist.")
    
    if command == "add":
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        c = [name,email,phone]
        contacts.append(c)
        print(c[0] + " was added.")

    if command == "del":
        try:
            num = int(input("Number: "))
            print(contacts.pop(num-1)[num-1] + " was deleted.")
        except:
            print("Contact does not exist.")
    
    if command == "exit":
        print("Bye!")
        contacts.clear()
    else:
        main()

if __name__ == "__main__":
    main()