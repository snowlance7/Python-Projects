contacts = list()

def main():
    with open("contacts.csv") as f1:
        contacts.clear()
        for line in f1:
            row = line.split(",")
            contacts.append(row)

    command = input("\nCommand: ")

    if command == "list":       #list
        cnt = 1
        for contact in contacts:
            print(str(cnt)+". "+contact[0])
            cnt += 1

    if command == "view":       #view
        try:
            num = int(input("Number: "))
            print("Name: "+contacts[num-1][0])
            print("Email: "+contacts[num-1][1])
            print("Phone: "+contacts[num-1][2])
            
        except:
            print("Contact does not exist.")

    if command == "add":
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        with open("contacts.csv","a") as f1:
            f1.write(name + "," + email + "," + phone + "\n")
            print(name + " was added.")

    if command == "del":
        try:
            num = int(input("Number: "))

            with open("contacts.csv","w") as f1:
                del_name = contacts.pop(num-1)[0]
                for contact in contacts:
                    f1.write(contact[0] + "," + contact[1] + "," + contact[2])
                print(del_name + " was deleted.")
        except:
            print("Contact does not exist.")
        

    if command == "exit":       #exit
        print("Bye!")
    else:
        main()

if __name__ == "__main__":
    print("Contact Manager")
    print("\nCOMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")

    main()