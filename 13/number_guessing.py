import random


def play_game():
    print('Welcome To The Number Guessing Game')
    print('I\'m Thinking of a number between 1 and 100')

    number = random.randrange(1, 100)

    print(number)

    attempts = 0
    counter = 0
    difficulty = input('Difficulty: Easy or Hard\n').lower()
    user_guess = ''

    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print('Incorrect input')

    while user_guess != number:
        user_guess = int(input('Make a guess\n'))

        if user_guess > number:
            print('Too High\nGuess Again')
            attempts -= 1
            counter += 1
            print(f'You have {attempts} attempts remaining')

        elif user_guess < number:
            print('Too Low\nGuess Again')
            attempts -= 1
            counter += 1
            print(f'You have {attempts} attempts remaining')

    print(
        f'You Win! The Answer Was {number}, it took you {counter} times before you got it right')


play_game()
