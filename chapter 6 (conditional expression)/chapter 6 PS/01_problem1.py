num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
num3 = int(input("enter number 3: "))
num4 = int(input("enter number 4: "))

if (num1 > num2 and num1 > num3 and num1 > num4):
    print(f"num1 = {num1}, is greatest")
elif (num2 > num1 and num2 > num3 and num2 > num4):
    print(f"num2 = {num2}, is greatest")
elif (num3 > num1 and num3 > num2 and num3 > num4):
    print(f"num3 = {num3}, is greatest")
elif (num4 > num1 and num4 > num2 and num4 > num3):
    print(f"num4 = {num4}, is greatest")