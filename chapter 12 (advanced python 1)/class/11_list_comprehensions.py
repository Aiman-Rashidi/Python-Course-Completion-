number_list = [1, 2, 9, 5, 3, 5]

# squared_list = []
# for number in number_list:
#     squared_list.append(number*number)

squared_list = [number*number for number in number_list]

print(squared_list)





# marks_list = [33, 85, 42, 39, 90, 27, 58]
# passed = [mark for mark in marks_list if mark >= 40]
# print(passed)





# marks_list = [33, 85, 42, 39, 90, 27, 58]
# results = ['Pass' if mark >= 40 else 'Fail' for mark in marks_list]
# print(results)