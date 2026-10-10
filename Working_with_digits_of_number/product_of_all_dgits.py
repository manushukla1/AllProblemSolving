digi = input("Enter a number: ")
product = 1

for char in digi:
    if char.isdigit():
        product = product * int(char)

print(product)

