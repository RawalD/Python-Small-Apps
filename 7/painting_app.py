import math


def number_of_cans(height, width, coverage):
    calculation = (height * width) / coverage
    return math.ceil(calculation)


print('Welcome To The Area Paint Calculator')

wall_height = float(input('Height of wall: '))
wall_width = float(input('Width of wall: '))
coverage = int(input('Coverage of can: '))

paint_job_one = number_of_cans(wall_height, wall_width, coverage)
print(paint_job_one)
