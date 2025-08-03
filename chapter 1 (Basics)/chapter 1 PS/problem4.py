import os

# dir location specifier
dir_path = '/Users/'

# list all files and dirs in the specified path
contents = os.listdir(dir_path)

# print each file and dir name in the given path
for item in contents:
    print(item)