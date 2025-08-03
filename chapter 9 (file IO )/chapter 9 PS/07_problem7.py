with open("log.txt", "r") as f:
    lines = f.readlines()

line_number = 1
for line in lines:
    if "python" in line:
        print(f"python: Present, Line number: {line_number}")
        break
    line_number += 1
else:
    print("Python: Absent")



# with open("log.txt", "r") as f:
#     lines = f.readlines()

# line_number = 1
# for line in lines:
#     if "python" in line:
#         print(f"Python: Present, Line number: {line_number}")
#         # break
#     line_number += 1
# # else:
# #     print("Python: Absent")
# else:
#     print("...file end here...")