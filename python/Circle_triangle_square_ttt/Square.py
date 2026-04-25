# Square
class Square:
    def __init__(self, a):
        self.a = a
    def area(self):
        return self.a * self.a
    def perimeter(self): 
        return 4 * self.a
square = Square(3)
print("Area of the square is: ", square.area())
print("Perimeter of the square is: ", square.perimeter())
