class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

emp = Employee()
prog = Programmer()
mgr = Manager()

print(emp.a)
# print(emp.b, emp.c)   # no property named b and c niether inherited nor local property 

print(prog.a, prog.b)
# print(prog.c)           # no property named b and c niether inherited nor local property

print(mgr.a, mgr.b, mgr.c)





# class First:
#     a = 1

# class Second(First):
#     b = 2

# class Third(Second):
#     c = 3

# one = First()
# print(one.a)
# # print(one.b, one.c)

# two = Second()
# print(two.a, two.b)
# # print(two.c)

# three = Third()
# print(three.a, three.b, three.c)