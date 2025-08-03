# class Employee:
#     lang = "Python"
#     salary = 12000

#     def __init__(self, name, lang, salary):
#         self.name = name
#         self.lang = lang
#         self.salary = salary

#     def getInfo(self):
#         print(f"name: {self.name}, lang: {self.lang}, salary: {self.salary}")

#     @staticmethod
#     def greet():
#         print("Good Morning!")

# harry = Employee("Harry", "Python", 13000)

# harry.greet()
# harry.getInfo()
# Employee.greet()
# Employee.getInfo(harry)

# print(harry.name, harry.lang, harry.salary)





# class Employee:
#     def __init__(self, name, lang, salary):
#         self.name = name
#         self.lang = lang
#         self.salary = salary

#     @staticmethod
#     def greet():
#         print("Good Morning!")

#     def getInfo(self):
#         print(f"Name: {self.name}, Language: {self.lang}, Salary: {self.salary}")

# harry = Employee("Harry", "JavaScript", 12000)
# aiman = Employee("Aiman", "Python", 13000)

# aiman.greet()
# aiman.getInfo()
# harry.greet()
# harry.getInfo()

# # Employee.greet()
# # Employee.getInfo(aiman)
# # Employee.greet()
# # Employee.getInfo(harry)





class Employee:
    def __init__(self, name, lang, salary):
        self.name = name
        self.lang = lang
        self.salary = salary

    @staticmethod
    def greet():
        print("Good Morning!")

    def getInfo(self):
        print(f"Name: {self.name}, Lang: {self.lang}, Salary: {self.salary}")

name = input("Enter the name: ")
lang = input("Enter the language: ")
salary = int(input("Enter the salary: "))

employee_details = Employee(name, lang, salary)

employee_details.greet()
employee_details.getInfo()

# Employee.greet()
# Employee.getInfo(employee_details)