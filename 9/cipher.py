def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


def decode(text, shift):
    deciphered_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        deciphered_text += new_letter
    print(f"The decoded text is {deciphered_text}")


print('Welcome To CipherPy')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


if direction == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)

elif direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decode(text, shift)

else:
    print('Not valid selection. App closing')
