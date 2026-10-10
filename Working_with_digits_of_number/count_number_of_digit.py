digi = str(input("Enter a number: "))
count = 0
for char in digi:
    if char.isdigit():
     count = count + 1
print(count)