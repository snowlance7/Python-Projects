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
        
class Square(Rectangle):
    def __init__(self, length):
        self.lenght = length
        Rectangle.height = length
        Rectangle.width = length

def main():
    choice = input("\nRectangle or square? (r/s): ").lower()
    
    if choice == "r":
        rectangle = Rectangle()
        rectangle.height = int(input("Height: "))
        rectangle.width = int(input("Width: "))
        print("Perimeter:",str(rectangle.perimeter))
        print("Area:",str(rectangle.area))
        rectangle.draw()
    elif choice == "s":
        square = Square(int(input("Length: ")))
        print("Perimeter:",str(square.perimeter))
        print("Area:",str(square.area))
        square.draw()

    if input("\nContinue? (y/n): ").lower() == "y":
        main()
    else:
        print("\nBye!")

    

if __name__ == "__main__":
    print("Rectangle Calculator")
    main()