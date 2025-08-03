class Vector:
    def __init__(self, vector_list):
        self.vector_list = vector_list

    def __len__(self):
        return len(self.vector_list)
    
v1 = Vector([1, 2, 3, 4, 5])
print(len(v1))



# class Name:
#     def __init__(self, a_list):
#         self.a_list = a_list

#     def __len__(self):
#         return len(self.a_list)
    
# obj = Name([1, 2, 3, 4, 5])
# print(len(obj))