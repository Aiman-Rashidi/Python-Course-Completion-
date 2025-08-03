# class Number:
#     def __init__(self, n):
#         self.n = n

#     def __add__(self, num):
#         return self.n + num.n

# num1 = Number(4)
# num2 = Number(2)

# print(num1 + num2)





class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, x):
        # return self.i + x.i, self.j + x.j, self.k + x.k
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
    
v1 = Vector(1, 2, 3)
print(v1)

v2 = Vector(2, 3, 4)
print(v2)

print(v1 + v2)
print(type(v1 + v2))