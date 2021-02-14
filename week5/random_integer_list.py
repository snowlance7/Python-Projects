import random

class RandomIntList(list):
    def __init__(self,count):
        cnt = 0
        while cnt < count:
            self.append(random.randint(1,100))
            cnt += 1

    @property
    def count(self):
        return len(self)

    @property
    def total(self):
        sum = 0
        for num in self:
            sum += num
        return sum

    @property
    def average(self):
        return self.total / self.count

    def __str__(self):
        ints = ""
        for num in self:
            ints += str(num) + ", "
        
        ints = ints.rstrip(", ")
        return ints

int_list = []

def main(cnt):
    int_list = RandomIntList(cnt)


    print("\nRandom Integers")
    print("===============")
    print("Integers:",int_list.__str__())
    print("Count:",int_list.count)
    print("Total:",int_list.total)
    print("Average:",int_list.average)

    if input("\nContinue? (y/n): ").lower() == "y":
        main(cnt)
    else:
        print("\nBye!")

if __name__ == "__main__":
    print("Random Integer List")
    cnt = int(input("How many random integers should the list contain?: "))

    main(cnt)