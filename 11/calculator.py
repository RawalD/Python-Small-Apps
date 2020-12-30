from typing import NamedTuple
from calc_art import logo

print(logo)


def calculate(number_one, number_two, operation):

    if operation == '+':
        return number_one + number_two
    elif operation == '-':
        return number_one - number_two
    elif operation == '/':
        return round((number_one / number_two), 2)
    elif operation == '*':
        return number_one * number_two


memory_number = 0

run = True

while run:

    number_one = float(input('Please enter your number:\n'))
    print('+\n-\n/\n*')
    operation = input('Enter type of operation\n')
    number_two = float(input('Please enter your second number:\n'))

    memory_number = calculate(number_one, number_two, operation)

    print(
        f'The answer for {number_one} {operation} {number_two} is {memory_number}')

    use_memory = input(
        'To calculate with old value type y or to start a new calculation type n , to quit type q\n')

    if use_memory == 'n':
        memory_number = 0

    elif use_memory == 'y':
        operation = input('Enter type of operation\n')
        number_two = float(input('Please enter your second number:\n'))
        memory_number_two = calculate(memory_number, number_two, operation)

        print(
            f'The answer for {memory_number} {operation} {number_two} is {memory_number_two}\n')

    elif use_memory == 'q':
        run = False
