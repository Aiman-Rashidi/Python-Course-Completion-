st = "Hey Aiman you are amazing\n"

f = open("myfile.txt", "w")     # if file not found it creates it and empty the file on everrun (not appending the data)
f.write(st)
f.close()