marks1 = int(input("enter marks 1: "))
marks2 = int(input("enter maeks 2: "))
marks3 = int(input("enter maeks 3: "))

total_percentage = ((marks1 + marks2 + marks3) / 300) * 100
print(total_percentage)

if (total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("Passed!")
else:
    print("Failed!")