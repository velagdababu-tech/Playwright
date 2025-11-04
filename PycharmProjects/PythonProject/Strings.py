str = "babuvelagada@gmail.com"
str1 = "babu"

print(str[1]) # character

print(str[0:4]) #substring

print(str + str1) #concatenation

print(str1 in str) #includes

var = str.split(".")  #split string
print(var)

print(var[0])   # )th value print
print(var[1])   # 1st value print

str4 = "   babu    "
print(str4.strip())   # trim spaces
print(str4.lstrip())  # left trim spaces
print(str4.rstrip())  # right trim spaces