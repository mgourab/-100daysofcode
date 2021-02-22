print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

bill_with_tip = total_bill * (1 + tip_percent/100)
#print(bill_with_tip)
bill_per_person = round(bill_with_tip / no_of_people, 2)
print(f'each person should pay: ${bill_per_person}')