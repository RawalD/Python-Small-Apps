import random
from random import shuffle

print('Welcome To The PyPasswordGenerator')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_input = int(input('How many letters in the password ?\n'))
symbols_input = int(input('How many symbols in the password ?\n'))
numbers_input = int(input('How many numbers in the password ?\n'))

length_of_password = letters_input + symbols_input + numbers_input
# print(length_of_password)

#password = ''

# Simple
# for letter in range(0, letters_input + 1):
#     password += str(random.choice(letters))

# for number in range(0, numbers_input + 1):
#     password += str(random.choice(numbers))

# for symbol in range(0, symbols_input):
#     password += random.choice(symbols)
password_list = []

for letter in range(0, letters_input):
    password_list.append(random.choice(letters))

for number in range(0, numbers_input):
    password_list.append(random.choice(numbers))

for symbol in range(0, symbols_input):
    password_list.append(random.choice(symbols))

shuffle(password_list)
# print(password_list)

password = ''

for char in password_list:
    password += char

print(password)
