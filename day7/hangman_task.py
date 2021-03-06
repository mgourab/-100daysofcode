import random
import hangman_art
import hangman_words
# import os
#
#
# def cls():
#     os.system('cls' if os.name == 'nt' else 'clear')


# randomly choose a word from the list and assign it to a variable "chosen_word"
chosen_word = random.choice(hangman_words.word_list)

lives = 6

# testing code
# print(f'the chosen word is: {chosen_word}')

# print the hangman logo
print(hangman_art.logo)

# we need to print the empty underscores now
display_underscore = []
word_length = len(chosen_word)

# for each letter in the chosen word, we need to create an underscore in this above list
for _ in range(word_length):
    display_underscore.append('_')

print(display_underscore)

end_of_game = False

while not end_of_game:
    # ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
    guess = input("Guess a letter: ").lower()
    # cls()

    # check if the player has already guessed it
    if guess in display_underscore:
        print(f"You've already guessed {guess}")

    # check if the letter the user guessed (guess) is one of the letters in the chosen_word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display_underscore[position] = letter

    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You loose a life!")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You loose :(")

    print(display_underscore)

    if ('_' not in display_underscore):
        end_of_game = True
        print("You win!")

    print(hangman_art.stages[lives])
