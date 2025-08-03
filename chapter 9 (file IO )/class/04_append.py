st = "another line added because file is opend in append mode\n"

f = open("myfile.txt", "a")

f.write(st)

f.close()