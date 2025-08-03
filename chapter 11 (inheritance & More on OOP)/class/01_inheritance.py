class Employee:
    company = "ITC"
    name = "Default Name"

    def show(self):
        print(f"The name of employee is {self.name} and the company is {self.company}")

# class Programmer:
#     company = "ITC Infotech"
#     name = "Default Name"
#     lang = "Python"

#     def show(self):
#         print(f"The name of employee is {self.name} and the company is {self.company}")

#     def showLanguage(self):
#         print(f"The name of the employee is {self.name} and He is good with {self.lang} language")

class Programmer(Employee):
    company = "ITC Infotech"
    lang = "Python"

    def showLanguage(self):
        print(f"The name of the employee is {self.name} and He is good with {self.lang} language")


a = Employee()
a.show()

b = Programmer()
b.show()
b.showLanguage()

# print(a.company, b.company)