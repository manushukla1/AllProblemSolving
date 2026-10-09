#Write a program to read a number and check whether it is positive, negative or zero

number_input = float(input("Enter a number: "))

if number_input == 0:
    print("It's a Zero")
elif number_input > 0:
    print("It's a Positive")
else:
    print("It's a Negative")
