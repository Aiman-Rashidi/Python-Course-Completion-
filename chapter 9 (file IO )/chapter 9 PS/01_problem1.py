f = open("poem.txt", "r")

content = f.read()

if ("Twinkle" in content):
    print("Twinkle present!")
else:
    print("Twinkle absent!")

f.close()