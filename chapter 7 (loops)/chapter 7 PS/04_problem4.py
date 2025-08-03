n = int(input("enter the number: "))

if(n == 1):
    print("neither prime nor composite")
else:
    for i in range(2, n):
        if (n % i == 0):
            print("composite")
            break
    else:
        print("prime")