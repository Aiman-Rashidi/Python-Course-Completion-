userName = input("enter username: ")

# print(userName, len(userName))
if(len(userName) < 10):
    print("username contains LESS THAN 10 characters!")
else:
    print("username contains MORE THAN or EQUAL to 10 characters!")