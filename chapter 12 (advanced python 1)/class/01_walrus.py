# Without walrus
value = input("Enter: ")
n = len(value)
if n > 5:
    print(f"Long input of length {n}")

# With walrus
if (n := len(value := input("Enter: "))) > 5:
    print(f"Long input of length {n}")





# Without walrus
my_list = [1, 2, 3, 4, 5]
n = len(my_list)

if n > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
    
# With walrus
if (n := len(my_list := [1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")