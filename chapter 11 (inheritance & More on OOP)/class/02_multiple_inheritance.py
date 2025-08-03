class Employee:
    company = "ITC"
    name = "Default Name"

    def show(self):
        print(f"The name of employee is {self.name} and the company is {self.company}")

class Coder:
    lang = "Python"

    def printLanguage(self):
        print(f"Out of all languages here is your language: {self.lang}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name of the employee is {self.name} and He is good with {self.lang} language")

a = Programmer()

a.show()
a.printLanguage()
a.showLanguage()

# b = Employee()
# b.show()
# print(b.company)