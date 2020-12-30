print('Welcome to the tip calculator')
bill_total = float(input('What was the total bill ?\n'))
people = int(input('How many people to split the bill by ?\n'))
tip_percentage = int(
    input('What percentage tip would you like to give ?\n10, 12, 15 ?\n'))
tip_calc = bill_total / people + (bill_total * (tip_percentage / 100 / people))
print(f'Each person should pay: {tip_calc}')
