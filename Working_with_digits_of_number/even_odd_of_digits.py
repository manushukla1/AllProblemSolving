num = input("Enter a number: ")
Even1 = []
odd1 = []
for i in range(len(num)):
    if int(num[i])%2==0:

        Even1.append(num[i])
    else:
        odd1.append(num[i])

print(Even1)
print(odd1)