digi = input("Enter a number: ")
sum = 0

for char in digi:
    if char.isdigit():
        sum = sum + int(char)

print(sum)

