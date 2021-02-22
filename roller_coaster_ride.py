print("Welcome to the roller coaster ride..")
height = int(input("What is your height in cms? "))

# check condition
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Ticket Price: $5")
    elif age <= 18:
        print("Ticket Price: $7")
    else:
        print("Ticket Price: $12")
else:
    print("Sorry! you have to grow taller before you can ride. :(")  