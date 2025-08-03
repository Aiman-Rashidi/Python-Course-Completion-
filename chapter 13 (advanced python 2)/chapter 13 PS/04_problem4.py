# def divisible_by_five(n):
#     if n % 5 == 0:
#         return True
#     return False

divisible_by_five = lambda n: True if n % 5 == 0 else False

num_list = [1, 5, 7, 10, 13, 15, 17, 20, 23, 24, 25, 47, 50]

multiple_of_five = filter(divisible_by_five, num_list)
print(list(multiple_of_five), type(multiple_of_five))

# multiple_of_five = list(filter(divisible_by_five, num_list))
# print(multiple_of_five, type(multiple_of_five))
# # for num in multiple_of_five:
# #     print(num)