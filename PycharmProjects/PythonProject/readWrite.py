file = open("test.txt")

#Read all the contents of file
#var = file.read()
#print(var)

#read n number of characters by passing parameter
#print(file.read(3))

#read one single line at a time readline()
#print(file.readline())
#print(file.readline())

#print line by line using readline method
line = file.readline()

#while line != "":
#   print(line)
#    line = file.readline()

for line in file.readlines():
    print(line)

file.close()