class Circle: 
    def __init__(self, r): 
        self.r = r 
        self.pi = 3.14 

    def area(self): 
        return self.pi * self.r * self.r 

    def perimeter(self): 
        return 2 * self.pi * self.r 


circle = Circle(4)
print("Area of the circle is: ", circle.area())
print("Perimeter of the circle is: ", circle.perimeter())