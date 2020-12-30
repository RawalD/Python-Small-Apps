import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_choice = random.randrange(0, 3)
symbols = [rock, paper, scissors]
computer_play = symbols[computer_choice]

user_choice = int(input('Enter your selection:\n0:Rock 1:Paper 2:Scissors\n'))
user_play = symbols[user_choice]

winner = ''

if computer_choice == 0 and user_choice == 1:
    print('Computer plays...')
    print(computer_play)

    print('You played...')
    print(user_play)

    winner = 'You Win'

elif computer_choice == 0 and user_choice == 2:
    print('Computer plays...')
    print(computer_play)

    print('You played...')
    print(user_play)

    winner = 'Computer Wins'

elif computer_play == 0 and user_choice == 0:
    print('Computer plays...')
    print(computer_play)

    print('You played...')
    print(user_play)

    winner = 'It\s a draw'

elif computer_choice == 1 and user_choice == 0:
    print('Computer plays...')
    print(computer_play)

    print('You played...')
    print(user_play)

    winner = 'You Lose'

elif computer_choice == 1 and user_choice == 1:
    print('Computer plays...')
    print(computer_play)

    print('You played...')
    print(user_play)

    winner = 'It\s a draw'

elif computer_play == 1 and user_choice == 2:
    print('Computer plays...')
    print(computer_play)

    print('You played...')
    print(user_play)

    winner = 'You win'

elif computer_choice == 2 and user_choice == 0:
    print('Computer plays...')
    print(computer_play)

    print('You played...')
    print(user_play)

    winner = 'You Win'

elif computer_choice == 2 and user_choice == 1:
    print('Computer plays...')
    print(computer_play)

    print('You played...')
    print(user_play)

    winner = 'Computer wins'

elif computer_play == 2 and user_choice == 2:
    print('Computer plays...')
    print(computer_play)

    print('You played...')
    print(user_play)

    winner = 'It\'s a draw'

print(winner)
