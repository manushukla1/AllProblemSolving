#check a year is leap year or not
enter_year = int(input("Enter a year: "))\

if (enter_year % 400 == 0) and (enter_year % 100 != 0 or enter_year % 4 == 0):
    print(f"{enter_year} is leap year")
else:
    print(f"{enter_year} is not leap year")
