class Employee:
    lang = "JavaScript"     # class attribute
    salary = 12000

harry = Employee()
harry.name = "Harry"        # instance attribute
print(harry.name, harry.lang, harry.salary)

aiman = Employee()
aiman.name = "Aiman"        # instance attribute
aiman.lang = "Python"       # instance attribute
print(aiman.name, aiman.lang, aiman.salary)