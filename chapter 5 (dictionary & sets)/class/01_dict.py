emptyDict = {}

marks = {
    "Harry" : 56,
    "Aiman" : 100,
    "Rohan" : 68,
    "data" : [23, 78, 54],
    3 : "Number",
    "data" : [3, 5]     #overwriting the "data" key
}

print(marks, type(marks))

print(marks["Harry"])
print(marks["Aiman"])
print(marks["Rohan"])
print(marks["data"])
print(marks[3])