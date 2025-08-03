# with open("this.txt", "r") as f:
#     content1 = f.read()

# with open("poem.txt", "r") as f:
#     content2 = f.read()

# if content1 == content2:
#     print("Files are Same!")
# else:
#     print("Files are not same!")



with open("this.txt", "r") as f:
    content1 = f.read()

with open("this_copy.txt", "r") as f:
    content2 = f.read()

if content1 == content2:
    print("Files are Same!")
else:
    print("Files are not same!")