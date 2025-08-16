# class Temeprature:
#     def __init__(self, celcius=0):
#         print("constructor called")
#         self.celcius = celcius

#     @property
#     def celcius(self):
#         print("celcius property called")
#         return self._celcius
    
#     @celcius.setter
#     def celcius(self, value):
#         print("celcius setter called")
#         self._celcius = value

#     @property
#     def fahrenheit(self):
#         print("fahrenheit property called")
#         return (self.celcius * 9/5) + 32
    
#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         print("fahrenheit setter called")
#         self.celcius = (value - 32) * 5/9

# t = Temeprature()

# print(t.celcius)
# print(t.fahrenheit)

# t.celcius = 25
# print(t.celcius)
# print(t.fahrenheit)

# t.fahrenheit = 77
# print(t.fahrenheit)
# print(t.celcius)





class Temperature:
    def __init__(self, fahrenheit=32):
        print("constructor called")
        self.fahrenheit = fahrenheit

    @property
    def fahrenheit(self):
        print("fahrenheit property called")
        return self._fahrenheit
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        print("fahrenheit setter called")
        self._fahrenheit = value

    @property
    def celcius(self):
        print("celcius property called")
        return (self.fahrenheit - 32) * 5/9
    
    @celcius.setter
    def celcius(self, value):
        print("celcius setter called")
        self.fahrenheit = (value * 9/5) + 32

t = Temperature()

print(t.fahrenheit)
print(t.celcius)

t.celcius = 25
print(t.celcius)
print(t.fahrenheit)

t.fahrenheit = 77
print(t.fahrenheit)
print(t.celcius)