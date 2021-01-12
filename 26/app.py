# Rock paper scissors
import random

choices = ['Rock', 'Paper', 'Scissors']

computer = random.choice(choices)
player = False
computer_score = 0
player_score = 0

while True:
    player = input('Rock, Paper, Scissors ?\n').capitalize()

    if player == computer:
        print('It\'s a tie!')

    elif player == 'Rock':
        if computer == 'Paper':
            print(f'You lose! {computer} covers paper!')
            computer_score += 1
        else:
            print(f'You win! {player} smashes {computer}')
            player_score += 1

    elif player == 'Paper':
        if computer == 'Scissors':
            print(f'You lose! {computer} cuts {player}')
            computer_score += 1
        else:
            print(f'You win! {player} covers {computer}')
            player_score += 1

    elif player == 'Scissors':
        if computer == 'Rock':
            print(f'You lose! {computer} smashes {player}')
            computer_score += 1
        else:
            print(f'You win! {computer} gets cut by {player}')
            player_score += 1

    elif player == 'Exit':
        print(
            f'The final scores:\nPlayer:{player_score}\nComputer:{computer_score}')
        break

    else:
        print('Invalid entry')
        computer = random.choice(choices)
