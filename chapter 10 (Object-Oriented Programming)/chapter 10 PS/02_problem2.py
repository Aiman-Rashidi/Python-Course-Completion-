class Calculator:
    def __init__(self, n):
        self.n = n
        print(f"Input Number: {self.n}")

    def square(self):
        square_of_n = self.n * self.n
        print(f"Sqaure in Function: {square_of_n}")
        return square_of_n
    
    def cube(self):
        cube_of_n = self.n * self.n * self.n
        print(f"Cube in Function: {cube_of_n}")
        return cube_of_n
    
    def square_root(self):
        square_root_of_n = self.n ** (1/2)
        print(f"Square Root in Function: {square_root_of_n}")
        return square_root_of_n

num = Calculator(4)

square_of_n_returned = num.square()
print(f"Square Returned: {square_of_n_returned}")

cube_of_n_returned = num.cube()
print(f"Cube Returned: {cube_of_n_returned}")

square_root_of_n_returned = num.square_root()
print(f"Square Root Returned: {square_root_of_n_returned}")