class Employee:
    lang = "Python"
    salary = 12000

    def getInfo(self):
        print(f"Language is {self.lang}, and Salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning!")

harry = Employee()
# print(harry.lang, harry.salary)

harry.greet()
harry.getInfo()

# Employee.greet()
# Employee.getInfo(harry)