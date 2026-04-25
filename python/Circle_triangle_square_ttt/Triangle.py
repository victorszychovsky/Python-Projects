# Triangle
class Triangle:
    def __init__(self, a, b, c, h): 
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def area(self):
        return 0.5 * self.a * self.h
    def perimeter(self): 
        return self.a + self.b + self.c
triangle = Triangle(3, 4, 5, 2)

print("Area of the triangle is: ", triangle.area())
print("Perimeter of the triangle is: ", triangle.perimeter())
