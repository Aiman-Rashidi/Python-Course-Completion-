class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin_code):
        self.name = name
        self.salary = salary
        self.pin_code = pin_code

    @staticmethod
    def greet():
        print("Good Morning!")

    def getInfo(self):
        print(f"name: {self.name}, company: {self.company}, salary: {self.salary}, pin code: {self.pin_code}")

programmer1 = Programmer("Aiman", 12000, 110086)
programmer2 = Programmer("Harry", 13000, 110087)

programmer1.greet()
programmer1.getInfo()
programmer2.greet()
programmer2.getInfo()

Programmer.greet()
Programmer.getInfo(programmer1)
Programmer.greet()
Programmer.getInfo(programmer2)