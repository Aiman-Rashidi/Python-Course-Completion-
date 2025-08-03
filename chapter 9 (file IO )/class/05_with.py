# f = open("file.txt", "r")

# print(f.read())

# # f.read() moves the file pointer to the end, so f.readlines() finds nothing left to read and returns an empty list.
# # lines = f.readlines()
# # print(lines)

# f.close()



#          both same but in below one no tension to close the file



with open("file.txt", "r") as f:

    # print(f.read())

    lines = f.readlines()
    print(lines)
    # # f.read() moves the file pointer to the end, so f.readlines() finds nothing left to read and returns an empty list.