print('Welcome To Treasure Island\nYour mission is to find the treasure')

direction = input('Do you dare go left or right ?\n').lower()

if direction == 'right':
    print('Oh no! A pit!\nGame Over')

else:
    print('You survive! Now...')
    swim_wait = input('Do you dare to swim or wait\n').lower()

    if swim_wait == 'swim':
        print('You drown!\nGame Over')

    else:
        print('Wise choice!')
        door = input(
            'Which door dare thee enter ?\nRed ,Blue or Yellow ?\n').lower()

        if door == 'red':
            print('A beast!\nGame Over')
        elif door == 'blue':
            print('Creatures!\nGame Over')
        else:
            print('You win!\nThe treasure is yours!')
