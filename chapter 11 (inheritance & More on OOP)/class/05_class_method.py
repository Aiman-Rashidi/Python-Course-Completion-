# class Employee:
#     a = 1

#     @classmethod    # it will give more preference to class_attribute than instance_attribute
#     def show(cls):
#         print(f"The class value of 'a' is: {cls.a}")

# emp = Employee()
# emp.a = 33  # instance attribute (instance_attribute >preference over class_attribute) 
# emp.show()

# # print(emp.a)
# # print(Employee.a)





class Employee:
    a = 1

    @classmethod    # it will give more preference to class_attribute than instance_attribute
    def show(cls):
        print(f"The class value of 'a' is: {cls.a}")

    def show(self):
        print(f"The instance value of 'a' is: {self.a}")

emp = Employee()
emp.a = 33  # instance attribute (instance_attribute >preference over class_attribute) 
emp.show()

# print(emp.a)
# print(Employee.a)





# class Employee:
#     a = 1

#     def show(self):
#         print(f"The instance value of 'a' is: {self.a}")

#     @classmethod    # it will give more preference to class_attribute than instance_attribute
#     def show(cls):
#         print(f"The class value of 'a' is: {cls.a}")

# emp = Employee()
# emp.a = 33  # instance attribute (instance_attribute >preference over class_attribute) 
# emp.show()

# print(emp.a)
# print(Employee.a)