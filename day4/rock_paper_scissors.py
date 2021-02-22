import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# get the three items in a list
options = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. :\n"))
print(options[choice])

print("Computer chose:\n")
computer_choice = random.randint(0, len(options) - 1)
print(computer_choice)
print(options[computer_choice])

# check if player win or loose
# - rock wins against scissors (0 win against 2)
# - scissors wins against paper (2 win against 1)
# - paper wins against rock (1 win against 0)
if (choice == 0) and (computer_choice == 1):
    print("Computer wins :(")
elif (choice == 0) and (computer_choice == 2):
    print("You win!")
elif (choice == 1) and (computer_choice == 0):
    print("You win!")
elif (choice == 1) and (computer_choice == 2):
    print("Computer wins :(")
elif (choice == 2) and (computer_choice == 0):
    print("Computer wins :(")
elif (choice == 2) and (computer_choice == 1):
    print("You win!")
else:
    print("Draw..")