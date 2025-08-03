marks = {
    "Harry" : 56,
    "Aiman" : 100,
    "Rohan" : 68,
    "data" : [23, 78, 54],
    3 : "Number"
}

# print(marks)
# print(type(marks))
# print(len(marks))

# print(marks.items())
# print(type(marks.items()))

# print(marks.values())
# print(type(marks.values()))

# print(marks.keys())
# print(type(marks.keys()))

# marks.update({"Aiman": 99, "Anushka": 68})  # update and can add new values
# print(marks)

print(marks.get("Aiman"))
print(marks.get("Shivika")) # return none when key not available 
print(marks["Aiman"])
# print(marks["Shivika"]) # return error when key not available 