#Write a program to read three numbers and find the smallest among them.

number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))
number_3 = int(input("Enter another number: "))

# if number_1 <= number_2 and number_1 <= number_3:
#     print("number_1 is smallest of all")
# elif number_2 <= number_1 and number_2 <= number_3:
#     print("number_2 is smallest of all")
# else:
#     print("number_3 is smallest of all")

min_number = min(number_1, number_2, number_3)
print(min_number)