def main():
    try:
        a = int(input("enter the number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("Finally block is executed")

main()