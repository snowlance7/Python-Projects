import math
import random

random_numbers = []

def searchList(target,start_index,end_index):
    if start_index == end_index:
        if target == random_numbers[start_index]:
            return True
        print("returning false")
        return False
    
    middle_index = math.floor((end_index + start_index) / 2)
    print("Middle Index:",str(middle_index)) #delete this
    number = random_numbers[middle_index]
    
    if number == target:
        print("returning true")
        return True
    elif number > target:
        print("go lower")
        return searchList(target,start_index,middle_index-1)
    else:
        print("go higher")
        return searchList(target,middle_index+1,end_index)
     

def main():
    target = input("\nEnter a number from 1 to 100: ")
    if target.lower() != "x":
        if searchList(int(target),0,len(random_numbers)-1) == True:
            print(str(target),"is in random numbers.")
        else:
            print(str(target),"is NOT in random numbers.")
        main()
    else:
        print("Bye!")
    

    

if __name__ == "__main__":
    print("Binary Search")
    print("\nEnter 'x' to exit")

    while len(random_numbers) < 10:
        random_numbers.append(random.randint(1,100))

    random_numbers.sort()
    print("\nRandom numbers:",random_numbers)
    main()
