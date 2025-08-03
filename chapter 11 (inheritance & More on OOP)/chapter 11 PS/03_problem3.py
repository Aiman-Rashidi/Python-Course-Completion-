class Employee:
    salary = 234
    # increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + (self.salary * (self.increment / 100)))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salaryAfterIncrement):
        self.increment = (((salaryAfterIncrement / self.salary) - 1) * 100)
        return self.increment
        
e = Employee()
# print(e.salary)
# print(e.increment)
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.8
print(e.salary)
print(e.increment)
print(e.salaryAfterIncrement)