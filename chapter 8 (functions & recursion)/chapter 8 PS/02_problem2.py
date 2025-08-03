# c/5 = (f-32)/9

def f_to_c(f):
    return ((f-32)/9)*5

f = int(input("enter F temperature: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")
