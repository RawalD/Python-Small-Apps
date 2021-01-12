# Random password

import random
passlen = int(input("Please enter the length of password\n"))

while passlen < 8:
    print('Password too short please aim for 8 characters or higher')

    passlen = int(input("Please enter the length of password\n"))

string_pass = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(string_pass, passlen))
print(password)
