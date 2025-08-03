a = int(input("enter the number: "))
b = int(input("enter the number: "))

if b == 0:
    # print("Denominator cannot be zero.")
    # raise ZeroDivisionError
    raise ZeroDivisionError("Denominator cannot be zero.")
else:
    print(f"Division {a}/{b} is {a/b}")

print("Thankyou")