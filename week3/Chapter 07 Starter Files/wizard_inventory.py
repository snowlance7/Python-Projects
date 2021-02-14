import random

all_items = []

def main():
    command = input("\nCommand: ")
     
     #walk
    if command == "walk":
        rand_item = random.randint(0,len(all_items)-1)
        
        print("While walking down a path, you see " + all_items[rand_item] + ".")
        
        if input("Do you want to grab it? (y/n): ").lower() == "y":
            f = open("inventory.txt","r")
            cnt = 0
            for l in f:
                if l != "\n":
                    cnt += 1
            f.close()
            
            if cnt < 4:
                f = open("inventory.txt","a")
                f.write(all_items[rand_item])
                print("You picked up a " + all_items[rand_item] + ".")
            else:
                print("You can't carry any more items. Drop something first.")
            f.close()

    #show
    if command == "show":
        cnt = 1

        try:
            f = open("inventory.txt")
            for line in f:
                print(str(cnt) + ". " + line[:-1])
                cnt += 1
        except:
            print("You dont have any items.")
        
        f.close()
    
    #drop
    if command == "drop":
        item_num = int(input("Number: "))
        try:
            f = open("inventory.txt")
            lines = f.readlines()
            item = lines[item_num-1]
            del lines[item_num-1]

            f = open("inventory.txt","w")
            for line in lines:
                f.write(line)
            print("You dropped " + item)
            f.close()
        except:
            print("That item doesnt exist.")

        

    if command == "exit":
        print("Bye!")
    else:
        main()
        

if __name__ == "__main__":
    f = open("wizard_all_items.txt")
    for l in f:
        all_items.append(l)
    f.close()
    
    print("The Wizard Inventory program")
    print("\nCOMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    
    main()
