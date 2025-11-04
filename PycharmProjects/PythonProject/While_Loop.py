it = 4
while it > 1:
    print(it)
    it = it - 1
print("Execution done!")

# exclude 3 in the output

it = 5
while it > 1:
    if it != 3:
        print(it)
    it = it - 1
print("Execution done!")

# break keyword to break entire loop
it = 6
while it > 1:
    if it == 3:
        break
    print(it)
    it = it -1
print("Execution done!")

# continue keyword to continue the entire loop
it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it =  it - 1
print("Execution Done!")