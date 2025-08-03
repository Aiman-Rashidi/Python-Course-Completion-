# a = int(input("enter 1st number: "))
# b = int(input("enter 2nd number: "))

# if b == 0:
#     raise ZeroDivisionError("infinite")
# else:
#     print(f"Divison {a}/{b} is {a/b}")





try:
    a = int(input("enter 1st number: "))
    b = int(input("enter 2nd number: "))
    print(f"Divison {a}/{b} is {a/b}")
except ZeroDivisionError:
    print("Infinite")
except ValueError:
    print("Please enter valid integers.")
print("Thankyou")