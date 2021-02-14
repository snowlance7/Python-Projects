class Customer():
    def __init__(self,id,firstName,lastName,company,address,city,state,zip):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
    
    @property
    def fullAddress(self):
        address = ""
        if self.company != "":
            address += self.company + "\n"
        
        address += self.address + "\n" + self.city + ", " + self.state + " " + self.zip.rstrip("\n")
        return address


customers = []

def main():
    id = input("\nEnter customer ID: ")
    cust_found = False
    for customer in customers:
        if customer.id == id:
            print("\n" + customer.firstName,customer.lastName)
            print(customer.fullAddress)
            cust_found = True
            break

    if cust_found != True:
        print("\nNo customer with that ID.")
    
    if input("\nContinue? (y/n): ").lower() == "y":
        main()
    else:
        print("\nBye!")


if __name__ == "__main__":
    print("Customer Viewer")

    with open("customers.csv") as f:
        cnt = 1
        for line in f:
            if cnt != 1:
                c = line.split(",")
                customers.append(Customer(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7]))
                
            cnt += 1
    
    main()