def prime_number(number):
    is_prime = True

    for num in range(2, number - 1):

        if number % num == 0:
            is_prime = False

    if is_prime:
        return f'{number} Is A Prime Number'
    else:
        return f'{number} Is Not A Prime Number'


print('Prime Number Checker')

number = int(input('Number to check: '))

print(prime_number(number))
