num = (input("Enter a number: "))
largest = num[0]

for i in range(len(num)):
    if num[i] > largest:
        largest = num[i]

print(largest)