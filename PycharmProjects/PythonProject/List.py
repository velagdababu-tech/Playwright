# List is data type that allows multiple values and can be different datatypes (Not immutable - we can update the values)
# By declaration we can easily understand because list values declare inside square brackets

values = [1, 2, 3, "babu", 4, 5, "velagada"]
# print the list values
print(values)

# print the specific index value
print(values[2]) # output = 3

# print the last value
print(values[-1]) # output = velagada

# print the specific values inbetween
print(values[1:4]) #output = 2, 3, babu

#Insert a value into specific index
values.insert(3, 143) # output = [1, 2, 3, 143, 'babu', 4, 5, 'velagada']
print(values)

#Apped the value into the list
values.append("end")
print(values)  # output = [1, 2, 3, 143, 'babu', 4, 5, 'velagada', 'end']

#del the specific index value
del values[0]
print(values)  # output = [2, 3, 143, 'babu', 4, 5, 'velagada', 'end']
