f = open("file.txt", "r")

# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))
# line2 = f.readline()
# print(line2, type(line2))
# line3 = f.readline()
# print(line3, type(line3))
# line4 = f.readline()
# print(line4, type(line4))
# line5 = f.readline()
# print(line5 == "", type(line5))   # returns empty string (cos no value in file at this line)
# # line6 = f.readline()
# # print(line6 == "", type(line6))

i = 1
line = f.readline()
while (line != ""):
    print(f"{i}){line}")
    line = f.readline()
    i += 1

f.close()