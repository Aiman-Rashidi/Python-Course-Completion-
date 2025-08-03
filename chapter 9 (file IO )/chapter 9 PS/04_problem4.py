word = "Donkey"

with open("file_4_donkey.txt", "r") as f:
    content = f.read()

new_content = content.replace(word, "######")

with open("file_4_donkey.txt", "w") as f:
    f.write(new_content)