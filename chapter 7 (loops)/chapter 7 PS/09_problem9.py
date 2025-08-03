n = int(input("enter the number: "))

for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")

# for i in range(1, n+1):
#     if (i == 1 or i == n):
#         print("*" * n)
#     else:
#         print("*", end="")
#         print(" " * (n-2), end="")
#         print("*")

# n = 5
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print("* ", end="")
#     print("")