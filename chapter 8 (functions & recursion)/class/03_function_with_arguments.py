def goodDay(name, ending):
    print("Have a good day, " + name)
    print(ending)

goodDay("Aiman", "Tanks")
goodDay("Divya", "Thanks")
goodDay("Harry", "Thankyou!")
goodDay("Rohan", "Thankyou so much")
# goodDay(name = "Rohan", ending= "Thankyou so much")

# returns none because no value is returned from the function
returnedValue = goodDay("Aiman", "Tanks")
print(returnedValue)



def returnSomething(name):
    print(f"{name}, How are you?")
    return "task completed"

# returnSomething("Aiman")
returnedValue = returnSomething("Aiman")
print(returnedValue)