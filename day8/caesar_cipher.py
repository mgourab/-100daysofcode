import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# create a function called caesar which can do both encode and decode also will take shift,direction as input..
def caesar(cipher_text, shift_amount, cipher_direction):
    final_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f'The {cipher_direction}d text is: {final_text}')


# print the logo
print(art.logo)

# take a flag for should end the program or not
should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # this is for the user input if shift is more than the no:of alphabets in the alphabet's list
    shift %= 26

    caesar(cipher_text=text, shift_amount=shift, cipher_direction=direction)

    # ask the user if he/she wants to continue or not
    restart = input('Type "yes" if you want to go again. Otherwise type "no".\n')
    if restart == 'no':
        should_end = True
        print('GoodBye!')
