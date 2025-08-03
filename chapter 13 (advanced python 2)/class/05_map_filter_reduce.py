# # Map
# num_list = [1, 2, 3, 4, 5]

# square = lambda n: n * n

# square_map = map(square, num_list)
# print(list(square_map), type(square_map))

# # square_list = list(map(square, num_list))
# # print(square_list, type(square_list))
# # for num in square_list:
# #     print(num)





# # Filter
# # def even(n):
# #     if n % 2 == 0:
# #         return True
# #     return False

# even = lambda n: True if n % 2 == 0 else False

# num_list = [1, 2, 3, 4, 5]

# # only_even_filter = filter(even, num_list)
# # print(list(only_even_filter), type(only_even_filter))

# only_even_list = list(filter(even, num_list))
# print(only_even_list, type(only_even_list))
# for num in only_even_list:
#     print(num)





# Reduce 
from functools import reduce

def add_list_items(num1, num2):
    return num1 + num2

def multiply_list_items(num1, num2):
    return num1 * num2

num_list = [1, 2, 3, 4, 5]

reduce_add = reduce(add_list_items, num_list)
reduce_mul = reduce(multiply_list_items, num_list)
print(reduce_add, type(reduce_add))
print(reduce_mul, type(reduce_mul))





# map(): Applies a function to each item in an iterable and returns a new iterable with the results.
# filter(): Applies a function to each item and keeps only those for which the function returns True.
# reduce(): Repeatedly applies a function to pairs of items, reducing the iterable to a single cumulative value.