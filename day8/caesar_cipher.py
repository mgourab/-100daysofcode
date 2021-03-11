alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# create a function called 'encrypt' that takes the 'text' and 'shift' as inputs
def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


# Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs
def decrypt(text_to_decrypt, shift_to_decrypt):
    decrypted_cipher = ''
    for letter in text_to_decrypt:
        position = alphabet.index(letter)
        new_position = position - shift_to_decrypt
        decrypted_cipher += alphabet[new_position]
    print(f"The decoded text is {decrypted_cipher}")


if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(text_to_decrypt=text, shift_to_decrypt=shift)
