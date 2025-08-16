class Employee:
    def __init__(self, salary=3000, designation="Employee"):
        print("constructor called")
        self.salary = salary
        self.designation = designation

    @property
    def salary(self):
        print("salary property called")
        return self._salary
    
    @salary.setter
    def salary(self, value):
        print("salary setter called")
        if not isinstance(value, int):
            raise ValueError("salary must be a number")
        if value <= 0:
            raise ValueError("salary must be greater than zero")
        self._salary = value

    @property
    def annual_salary(self):
        print("annual_salary property called")
        return self.salary * 12
    
    @property
    def designation(self):
        print("designation property called")
        return self._designation
    
    @designation.setter
    def designation(self, value):
        if not isinstance(value, str):
            raise ValueError("invalid 1")
        if value.strip() == "":
            raise ValueError("invalid 2")
        if value not in("Manager", "Developer", "CEO", "Employee"):
            raise ValueError("invalid 3")
        self._designation = value

e1 = Employee(4000)
print(e1.salary)
print(e1.annual_salary)
print(e1.designation)

e1.designation = "CEO"
print(e1.designation)