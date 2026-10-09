take_input = int(input("Enter a number: "))
sum = 0
for num in range(0,take_input+1):
    if num % 2 == 0:
        sum += num
print(sum)

