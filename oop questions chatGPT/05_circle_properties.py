class Circle:
    def __init__(self, radius =1):
        print("constructor called")
        self.radius = radius

    @property
    def radius(self):
        print("radius property called")
        return self._radius
    
    @radius.setter
    def radius(self, value):
        print("radius setter called")
        if value <= 0:
            raise ValueError("radius must be positive number")
        self._radius = value

    @property
    def area(self):
        print("area property called")
        return 3.14 * self.radius * self.radius
    
    @property
    def circumference(self):
        print("circumference property called")
        return 2 * 3.14 * self.radius

# # Default value check
# c1 = Circle()
# print(c1.radius)
# print(c1.area)
# print(c1.circumference)

# Input value check(valid one)
c1 = Circle(7)
print(c1.radius)
print(c1.area)
print(c1.circumference)

# # Input value check(invalid one)
# c1 = Circle(-9)
# print(c1.radius)