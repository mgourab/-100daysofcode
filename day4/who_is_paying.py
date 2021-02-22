# Import the random module
import random

# Do the seed
test_seed = input("Please enter a seed number: ")
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_names = len(names)
random_choice = random.randint(0, total_names - 1)
person_who_pay = names[random_choice]

# Print our random name
print(f'{person_who_pay} is going to buy the meal today!')