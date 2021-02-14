import business as b

def main():
    command = input("Command: ").lower()
    
    if command == "view":
        cname = input("Category name: ").lower()
        category = b.Category(cname)
        products = category.getProducts()
        print("Code \t Name \t\t\t Price")
        print("---------------------------------------------------------")
        for product in products:
            print(product.productCode,"\t",product.productName,"\t\t\t",product.listPrice)
        main()

    elif command == "update":
        main()
    elif command == "exit":
        print("\nBye!")
    else:
        main()

if __name__ == "__main__":
    print("Product Manager")
    print("\nCATEGORIES")
    print("Guitars | Basses | Drums")
    print("\nCOMMAND MENU")
    print("view - View products by category")
    print("update - Update product price")
    print("exit - Exit program")
    main()