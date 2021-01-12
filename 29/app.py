# Acronym maker

user_text = input('Please enter a string to convert:\n')
user_text = user_text.split()
acronym = ''

for letter in user_text:
    acronym = acronym + str(letter[0]).upper()

print(acronym)
