import random

word_list = ["aardvark", "baboon", "camel"]

# randomly choose a word from the list and assign it to a variable "chosen_word"
chosen_word = random.choice(word_list)

# ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
guess = input("Guess a letter: ").lower()

# check if the letter the user guessed (guess) is one of the letters in the chosen_word
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")