class Demo:
    a = 3

obj = Demo()

print(obj.a)    #prints class attribute cos instance attribute is not present
obj.a = 0   #instance attribute updated
print(obj.a)    #hence, prints instance attribute (instance_attribute >preferred class_attribute)
print(Demo.a)   #here class attribute is unchaged

Demo.a = 333    #here class attribute will be changed
print(obj.a)    #obj.a is set to be 0. So, prints 0
print(Demo.a)   #here class is changed proof