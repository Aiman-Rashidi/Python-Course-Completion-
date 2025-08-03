def myFunc():
    print("Hello World!")

myFunc()
print(__name__)

if __name__ == "__main__":
# if __name__ == "module":
    print("we are directly running this codde")
    myFunc()
    print(__name__)