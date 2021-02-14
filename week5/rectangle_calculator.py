class Rectangle:

    height = int()
    width = int()

    @property
    def perimeter(self):
        return (self.height + self.width) * 2

    @property
    def area(self):
        return self.height * self.width

    def draw(self):
        print(" *" * self.width)
        i = 0
        while i < (self.height - 2):
            print(" *" + ("  " * (self.width - 2)) + " *")
            i += 1
        print(" *" * self.width)
        
def main():
    rectangle = Rectangle()
    rectangle.height = int(input("\nHeight: "))
    rectangle.width = int(input("Width: "))
    print("Perimeter:",str(rectangle.perimeter))
    print("Area:",str(rectangle.area))
    rectangle.draw()

    if input("\nContinue? (y/n): ").lower() == "y":
        main()
    else:
        print("\nBye!")

    

if __name__ == "__main__":
    print("Rectangle Calculator")
    main()