nameList = ["aiman", "harry", "rohan", "rashidi"]

name = input("enter the name: ")

if(name in nameList):
    print("name matched!")
else:
    print(f"no {name} in database!")