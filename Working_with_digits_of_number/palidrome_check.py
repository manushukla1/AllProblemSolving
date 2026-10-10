num = (input("Please enter a number: "))

for i in range(len(num)):
    if num[i] == num[len(num) - 1 - i]:
        continue
    else:
        print(f"{num} is not a palindrome")
        break

else:
    print(f"{num} is a palindrome")