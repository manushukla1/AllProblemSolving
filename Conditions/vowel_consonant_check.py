take_character = input("Enter your character:")
if take_character.lower() in "aeiou":
    print(f"{take_character.lower()} is vowel")
else:
    print(f"{take_character.lower()} is consonant")