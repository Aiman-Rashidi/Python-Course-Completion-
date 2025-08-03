p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

comment = input("enter your comment here: ")

if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("spam comment!")
else:
    print(comment)