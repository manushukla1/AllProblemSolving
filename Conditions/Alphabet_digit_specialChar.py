take_input = input("Enter a character: ")

if take_input.isdigit():
    print(f"{take_input} is digit")
elif take_input.isalpha():
    print(f"{take_input} is alphabet")
elif take_input.isalnum():
    print(f"{take_input} is alphanumeric")
else:
    print(f"{take_input} is special Character")
