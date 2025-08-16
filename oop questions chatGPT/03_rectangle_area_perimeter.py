class Rectangle:
    def __init__(self, length=1, width=1):
        print("constructor called")
        self.length = length
        self.width = width

    @property
    def length(self):
        print("length property called")
        return self._length
    
    @length.setter
    def length(self, value):
        print("length setter called")
        if value <= 0:
            raise ValueError("length must be greater than 0.")
        self._length = value

    @property
    def width(self):
        print("width property called")
        return self._width
    
    @width.setter
    def width(self, value):
        print("width setter called")
        if value <= 0:
            raise ValueError("width must be greater than 0.")
        self._width = value

    @property
    def area(self):
        print("area property called")
        return (self.length * self.width)
    
    @property
    def perimeter(self):
        print("perimeter property called")
        return (self.length + self.width) * 2
    
# # Default value check
# rec1 = Rectangle()
# print(rec1.length)
# print(rec1.width)
# print(rec1.area)
# print(rec1.perimeter)

# Input value check(valid one)
rec1 = Rectangle(5, 7)
print(rec1.length)
print(rec1.width)
print(rec1.area)
print(rec1.perimeter)

# # Input value check(invalid one)
# rec1 = Rectangle(5, -7)
# print(rec1.length)
# print(rec1.width)
# print(rec1.area)
# print(rec1.perimeter)

# # setter check (valid one)
# rec1 = Rectangle()
# print(rec1.length)
# print(rec1.width)
# rec1.length = 5
# rec1.width = 7
# print(rec1.length)
# print(rec1.width)
# print(rec1.area)
# print(rec1.perimeter)