class Employee:
    def __init__(self):
        print("Constructor of Employee")
    # a = 1

class Programmer(Employee):
    def __init__(Self):
        super().__init__()
        print("Constructor of Programmer")
    # b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    # c = 3

emp = Employee()
prog = Programmer()
mgr  = Manager()

# print(emp.a)
# print(prog.a, prog.b)
# print(mgr.a, mgr.b, mgr.c)