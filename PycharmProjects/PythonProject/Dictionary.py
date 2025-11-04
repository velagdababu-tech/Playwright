#Dictionary is an unorder sequence of data of key value pair form.

val = { 1: "babu", 2: 143, 3: "Velagada"}
print(val) #output = {1: 'babu', 2: 143, 3: 'Velagada'}
print(val[1]) #output = babu

#Insert the value into the dictionary data type
val[4] = "Rjy"
print(val) #output = {1: 'babu', 2: 143, 3: 'Velagada', 4: 'Rjy'}

#Insert/update multple the value into the dictionary data type
val.update({2: 153, 5: "East Godavri"})
print(val)  # output = {1: 'babu', 2: 153, 3: 'Velagada', 4: 'Rjy', 5: 'East Godavri'}

#Last value removed
last_value = val.popitem()
print(last_value)  # output = (5, 'East Godavri')
print(val)

#Last value return
print(list(val.values())[-1])  #output = Rjy

#delete the specific value
del val[2]
print(val) # output = {1: 'babu', 3: 'Velagada', 4: 'Rjy'}

#create a dictionary run time add the data into that dictionary
dist= { }
print(dist) # output = {}
dist["firstName"] = "Babu"
dist["LastName"] = "Velagada"
print(dist) #output = {'firstName': 'Babu', 'LastName': 'Velagada'}
