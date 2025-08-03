a = 77

def fun():
    global a
    a = 33
    print(a)

fun()
print(a)