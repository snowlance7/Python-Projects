import famc_module

def display_title():
    print("Feet and Meters Converter")

def display_menu():
    print("\nConversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

def main():
    display_menu()
    menu_item = input("Select a conversion (a/b): ")

    if menu_item.lower() == "a":
        feet = float(input("\nEnter feet: "))
        print(str(round(famc_module.feet_to_meters(feet),2)) + " meters")
    elif menu_item.lower() == "b":
        meters = float(input("\nEnter meters: "))
        print(str(round(famc_module.meters_to_feet(meters),2)) + " feet")
    
    if input("\nWould you like to perform another conversion? (y/n): ").lower() == "y":
        main()

if __name__ == "__main__":
    display_title()
    main()