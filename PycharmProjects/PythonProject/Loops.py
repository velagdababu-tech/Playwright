# for loop

obj = [2,3,4,5,6]

for i in obj:
    print(i)
    print(i * 2)
print('************print first 5 natural numbers*****************')
# print first 5 natural numbers
for j in range(1, 6):
    print(j)
print('***********sum of numbers******************')
# sum of numbers
summation = 0
for j in range(1,6):
    summation = summation + j
    print(j)
print(summation)

print('************jump into 2 values by using for loop*****************')
# jump into 2 values by using for loop
for j in range(1, 10, 2):
    print(j)
print('*************print all indexes values including zero****************')
# print all indexes values including zero
for m in range(10):
    print(m)