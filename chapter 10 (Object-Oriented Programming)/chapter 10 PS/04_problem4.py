class Calculator:
    def __init__(self, n):
        self.n = n
        print(f"Input Number: {self.n}")

    def square(self):
        print(f"Square: {self.n * self.n}")

    def cube(self):
        print(f"Cube: {self.n * self.n * self.n}")

    def square_root(self):
        print(f"Square Root: {self.n ** (1/2)}")

    @staticmethod
    def greet():
        print("Thankyou for using the App!")

num = Calculator(4)
num.square()
num.cube()
num.square_root()

num.greet()