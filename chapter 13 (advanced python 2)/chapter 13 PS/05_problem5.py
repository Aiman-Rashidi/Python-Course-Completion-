from functools import reduce

# def greatest(a, b):
#     # print(a, end="   ")
#     # print(b)
#     if a > b:
#         return a
#     return b

greatest = lambda a, b: a if a > b else b

num_list = [111, 2, 65, 5553, 635, 65, 74, 45,55]

print(reduce(greatest, num_list))