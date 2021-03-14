alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# create a function called caesar which can do both encode and decode also will take shift,direction as input..
def caesar(cipher_text, shift_amount, cipher_direction):
    final_text = ''
    for letter in cipher_text:
        position = alphabet.index(letter)
        if cipher_direction == 'decode':
            shift_amount *= -1
        new_position = position + shift_amount
        final_text += alphabet[new_position]
    print(f'The {cipher_direction}d text is: {final_text}')


caesar(cipher_text=text, shift_amount=shift, cipher_direction=direction)
