num = (input("Enter a number: "))
smallest = num[0]

for i in range(len(num)):
    if num[i] < smallest:
        smallest = num[i]

print(smallest)