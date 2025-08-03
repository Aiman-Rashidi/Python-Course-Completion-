with open("log.txt", "r") as f:
    content = f.read()

if "python" in content:
    print("python: Present")
else:
    print("python: Absent")