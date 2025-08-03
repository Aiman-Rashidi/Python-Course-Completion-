'''
sum(1) = 1
sum(2) = 2 + 1
sum(3) = 3 + 2 + 1
sum(4) = 4 + 3 + 2 + 1
sum(5) = 5 + 4 + 3 + 2 + 1

sum(n) = (n) + (n-1) + ... + 3 + 2 + 1
sum(n) = n + sum(n-1)
'''

def naturalSum(n):
    if n == 1:
        return 1
    return n + naturalSum(n-1)

n = int(input("enter the number: "))
print(naturalSum(n))