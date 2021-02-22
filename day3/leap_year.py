print("Welcome to the leap year checker!")
year = int(input("Please enter your desired year: "))

# check if it is a leap year or not
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"The year {year} is a leap year.. :)")
        else:
            print(f"The year {year} is not a leap year.. :(")
    else:
        print(f"The year {year} is a leap year.. :)")
else:
    print(f"The year {year} is not a leap year.. :(")