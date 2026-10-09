num = int(input("Enter a number: "))

if num % 5 == 0 and num % 3 == 0:
    print(f"{num} divisible by 5 and 3")
else:
    print(f"{num} not divisible by 5 and 3")