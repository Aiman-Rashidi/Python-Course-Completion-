# class Employee:
#     a = 1

#     @classmethod
#     def show(cls):
#         print(f"The class value of 'a' is: {cls.a}")

#     @property
#     def name(self):
#         # return "anything can be returned"
#         return f"{self.fname} {self.lname}"

#     @name.setter
#     def name(self, value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

#     # def showName(self):
#     #     print(f"{self.fname} {self.lname}")

# emp = Employee()
# emp.a = 33
# emp.show()

# emp.name = "Aiman Rashidi"
# print(emp.name)
# print(emp.fname, emp.lname)

# # emp.showName()





class Employee:
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

    def showName(self):
        print(f"{self.fname, self.lname}")

emp = Employee()
emp.name = "Aiman Rashidi"

print(emp.name)
print(emp.fname, emp.lname)
emp.showName()