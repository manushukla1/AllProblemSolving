enter_seconds = int(input("Enter the number of seconds: "))
Hours = enter_seconds // 3600
minutes = (enter_seconds % 3600) // 60
seconds = (enter_seconds % 3600) % 60

print(Hours, minutes, seconds)

