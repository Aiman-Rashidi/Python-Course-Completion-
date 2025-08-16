while (number := input("enter: ").strip().lower()) != "stop":
    if number.isdigit():
        if int(number) % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
    else:
        print("please enter a valid number or 'stop'.")