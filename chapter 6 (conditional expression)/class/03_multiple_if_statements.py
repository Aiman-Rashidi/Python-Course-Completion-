age = int(input("enter your age: "))

if age > 0:
    if age % 2 == 0:
        print("even age")

if age >= 18:
    print("allowed")
elif age < 0:
    print("negative age: invalid")
elif age == 0:
    print("zero age: invalid")
else:
    print("not allowed")

print("------end of program------")