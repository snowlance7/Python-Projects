#x = isinstance(5, int)

class Person():
    def __init__(self,firstName,lastName,email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.fullName = firstName + " " + lastName

class Customer(Person):
    def __init__(self,firstName,lastName,email,cust_num):
        super().__init__(firstName,lastName,email)

        self.cust_num = cust_num

class Employee(Person):
    def __init__(self,firstName,lastName,email,ssn):
        super().__init__(firstName,lastName,email)

        self.ssn = ssn

def main():
    choice = input("\nCustomer or employee? (c/e): ").lower()
    print("\nDATA ENTRY")
    
    fname = input("First name: ")
    lname = input("Last name: ")
    email = input("Email: ")

    if choice == "c":
        person = Customer(fname,lname,email,input("Number: "))
    elif choice == "e":
        person = Employee(fname,lname,email,input("SSN: "))

    if isinstance(person, Employee):
        print("\nEMPLOYEE")
        print("First name:",person.firstName)
        print("Last name:",person.lastName)
        print("Email:",person.email)
        print("SSN:",person.ssn)
    elif isinstance(person, Customer):
        print("\nCUSTOMER")
        print("First name:",person.firstName)
        print("Last name:",person.lastName)
        print("Email:",person.email)
        print("Number:",person.cust_num)

    if input("\nContinue? (y/n): ").lower() == "y":
        main()
    else:
        print("\nBye!")


if __name__ == "__main__":
    print("Customer/Employee Data Entry")
    main()